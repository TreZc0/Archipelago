import asyncio
import logging

from typing import TYPE_CHECKING

from NetUtils import ClientStatus
if TYPE_CHECKING:
    from worlds.poe.Client import PathOfExileContext
    from worlds.poe import PathOfExileWorld
from . import itemFilter
from . import gggAPI
from . import fileHelper
from . import inputHelper
from . import tts
from . import textUpdate

import worlds.poe.Items as Items
import worlds.poe.Locations as Locations

import worlds.poe.Options as Options

found_items_dict = {}
found_items_set = set()
save_path = "found_items.txt"
is_char_in_logic = True

_debug = True
_verbose_debug = False

logger = logging.getLogger("poeClient.validationLogic")

async def when_enter_new_zone(ctx: "PathOfExileContext", line: str):
    zone = textUpdate.get_zone_from_line(ctx, line)
    if not zone:
        return
    victory_task = check_for_victory(ctx, zone)
    skip_load_filter = True if victory_task else False
       
    await validate_and_update(ctx)
    #await asyncio.sleep(0.1)  # Allow some time for the game to load
    if not skip_load_filter:
        await inputHelper.important_send_poe_text("/itemfilter __ap", retry_times=40, retry_delay=0.5)

def check_for_victory(ctx: "PathOfExileContext", zone: str) -> asyncio.Task | None:
    goal = ctx.game_options.get("goal", -1)
    if goal == -1:
        logger.info("ERROR: No goal set in client options.")

    def send_goal():
        asyncio.create_task(ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}]))
        ctx.finished_game = True
        ctx.victory = True
    

    if \
    (goal == Options.Goal.option_complete_act_1 and zone == "The Southern Forest") or \
    (goal == Options.Goal.option_complete_act_2 and zone == "The City of Sarn") or \
    (goal == Options.Goal.option_complete_act_3 and zone == "The Aqueduct") or \
    (goal == Options.Goal.option_complete_act_4 and zone == "The Slave Pens") or \
    (goal == Options.Goal.option_kauri_fortress_act_6 and zone == "The Karui Fortress") or \
    (goal == Options.Goal.option_complete_act_6 and zone == "The Bridge Encampment") or \
    (goal == Options.Goal.option_complete_act_7 and zone == "The Sarn Ramparts") or \
    (goal == Options.Goal.option_complete_act_8 and zone == "The Blood Aqueduct") or \
    (goal == Options.Goal.option_complete_act_9 and zone == "Oriath Docks") or \
    (goal == Options.Goal.option_complete_the_campaign and zone == "Karui Shores"):
        return asyncio.create_task(textUpdate.callback_if_valid_char(ctx, send_goal))
    
    return None


async def validate_and_update(ctx: "PathOfExileContext" = None) -> bool:
    global is_char_in_logic
    validate_errors = []
    if ctx is None:
        # something is wrong, are we not connected?
        logger.info("Context is None, cannot validate character.")
        validate_errors.append("Context is None, cannot validate character.")
        
    character_name = ctx.character_name
    if character_name is None or character_name == "":
        logger.info("Character name is not set, cannot validate.")
        validate_errors.append("Character name is not set, cannot validate.")
        
    
    else: # we have a character name, and ctx is not None -- because we get the character name from ctx
        char = {}
        try:
            char = (await gggAPI.get_character(character_name)).character
            ctx.last_response_from_api.setdefault("character",{})[ctx.character_name] = char
            ctx.last_character_level = char.level
        except Exception as e:
            logger.info(f"Error fetching character {character_name}: {e}")
            raise e
        validate_errors = await validate_char(char, ctx)

    is_char_in_logic = True if len(validate_errors) == 0 else False


    if is_char_in_logic:
        locations_to_check = set()
        #add items to locations_to_check
        found_items_set = get_found_items(char)
        for item in found_items_set:
            if _debug and _verbose_debug:
                logger.info(f"[DEBUG] Found item: {item}")
            location_id = Locations.get_location_id_from_item_name(item)
            if location_id is not None:
                locations_to_check.add(location_id)
        itemFilter.update_item_filter_from_context(ctx)

        #add levels to locations_to_check
        if ctx.game_options.get("add_leveling_up_to_location_pool", True):
            for level in range(2, ctx.last_character_level + 1):
                if _debug and _verbose_debug:
                    logger.info(f"[DEBUG] Adding level {level} to locations to check.")
                level_location_name = Locations.get_lvl_location_name_from_lvl(level)
                location_id = Locations.get_location_id_from_level_location_name[level_location_name]
                if location_id is not None:
                    locations_to_check.add(location_id)

        if len(locations_to_check) > 0:
            if _debug:
                logger.info(f"[DEBUG] Locations to check: {locations_to_check}")
            locations_to_check = await ctx.check_locations(locations_to_check)
        else:
            if _debug:
                logger.info("[DEBUG] No locations to check, skipping check_locations.")
        itemFilter.update_item_filter_from_context(ctx, recently_checked_locations=locations_to_check)
        return True

    else:
        await update_filter_to_invalid_char_filter(validate_errors, ctx.tts_options.enable, ctx.tts_options.speed)
        full_error_text = f"@{ctx.character_name} you are out of logic: {", and".join(validate_errors)}"
        await inputHelper.send_poe_text(full_error_text)
        return False



async def validate_char(character: gggAPI.Character, ctx: "PathOfExileContext") -> list[str]:
    # Perform validation logic here

    if character is None:
        return ["Character name is not set, cannot validate."]

    errors = list()

    total_recieved_items = list()
    for network_item in ctx.items_received:
        total_recieved_items.append(Items.item_table.get(network_item.item))

    if not total_recieved_items:
        return ["No items received from the server... are you sure you are connected?"]

    simple_equipment_slots = ["BodyArmour","Amulet","Belt","Boots","Gloves","Helmet"]

    normal_flask_count = 0
    magic_flask_count = 0
    unique_flask_count = 0

    # --------- VALIDATION LOGIC STARTS HERE ---------
    if ctx.game_options.get("passivePointsAsItems", True):
        passive_points = len([i["name"] for i in total_recieved_items if i["name"] == 'Progressive passive point'])
        passives_used = len(character.passives.hashes) # number of passives allocated
        ctx.passives_available = passive_points
        ctx.passives_used = passives_used
        if passives_used > passive_points:
            errors.append(f"{passives_used - passive_points} Over-allocated passive points")


    if character.class_ not in [i["name"] for i in total_recieved_items]:
        errors.append(f"Class {character.class_}")

    gucci_rarity_check = {}
    for equipped_item in character.equipment:
        rarity = equipped_item.rarity
        gucci_rarity_check.setdefault(rarity, 0)
        gucci_rarity_check[rarity] += 1
        # simple checks.
        for slot in simple_equipment_slots:
            if equipped_item.inventoryId == slot:
                errors.append(rarity_check(total_recieved_items, rarity, slot))
                
        if equipped_item.inventoryId == "Ring":
            errors.append(rarity_check(total_recieved_items, rarity, "Ring (left)"))
        if equipped_item.inventoryId == "Ring2":
            errors.append(rarity_check(total_recieved_items, rarity, "Ring (right)"))
        if equipped_item.inventoryId == "Offhand":
            if equipped_item.baseType in Items.quiver_base_types:
                errors.append(rarity_check(total_recieved_items, rarity, "Quiver"))
            else:
                errors.append(rarity_check(total_recieved_items, rarity, "Shield"))
        if equipped_item.inventoryId == "Weapon":
            for prop in equipped_item.properties:
                prop_name = prop.name
                for weapon_base_type in Items.weapon_base_types:
                    if prop_name.lower().endswith(weapon_base_type.lower()):
                        errors.append(rarity_check(total_recieved_items, rarity, weapon_base_type))

        equipped_sockets = 0
        if equipped_item.socketedItems is not None:
            for socketed_item in equipped_item.socketedItems:
                if socketed_item.support:
                    equipped_sockets += 1
                if socketed_item.baseType not in [i["name"] for i in total_recieved_items]:
                    errors.append(f"Socketed {socketed_item.baseType} in {equipped_item.inventoryId}")

        links = [i["name"] for i in total_recieved_items if i["name"] == f"Progressive max links - {equipped_item.baseType}"]
        if len(links) < equipped_sockets - 1: # -1 for the skill gem
            errors.append(f"Too many links for {equipped_item.baseType}")

        if equipped_item.inventoryId == "Flask":
            flask_rarity = equipped_item.rarity
            if flask_rarity == "Normal":
                normal_flask_count += 1
            elif flask_rarity == "Magic":
                magic_flask_count += 1
            elif flask_rarity == "Unique":
                unique_flask_count += 1
                
    # get count of items.name that match the progressive unlocks
    if normal_flask_count > len([i["name"] for i in total_recieved_items if i["name"] == 'Progressive Flask Unlock Slot']):
        errors.append("Normal Flasks")
    if magic_flask_count > len([i["name"] for i in total_recieved_items if i["name"] == 'Progressive Magic Flask Unlock']):
        errors.append("Magic Flasks")
    if unique_flask_count > len([i["name"] for i in total_recieved_items if i["name"] == 'Progressive Unique Flask Unlock']):
        errors.append("Unique Flasks")

    gucci_hobo_mode = ctx.game_options.get("gucciHobo", False)
    if gucci_hobo_mode == 1 or gucci_hobo_mode == 2 or gucci_hobo_mode ==3:
        normal_gear = gucci_rarity_check.setdefault("Normal", 0)
        magic_gear = gucci_rarity_check.setdefault("Magic", 0)
        rare_gear = gucci_rarity_check.setdefault("Rare", 0)
        if gucci_hobo_mode == Options.GucciHoboMode.option_allow_one_slot_of_any_rarity and  normal_gear + magic_gear + rare_gear > 1: #options_allow_one_slot_of_any_rarity
            errors.append("Gucci Hobo Mode - Only one item allowed of any rarity")
        if gucci_hobo_mode == Options.GucciHoboMode.option_allow_one_slot_of_normal_rarity and (normal_gear > 1 or magic_gear + rare_gear > 0):  # options_allow_one_slot_of_normal_rarity
            errors.append("Gucci Hobo Mode - Only one normal item allowed")
        if gucci_hobo_mode == Options.GucciHoboMode.option_no_non_unique_items and (normal_gear + magic_gear + rare_gear > 0): # option_no_non_unique_items
            errors.append("Gucci Hobo Mode - No non-unique items allowed")

    errors = [x for x in errors if x]  # filter out empty strings
    if _debug and errors:
        logger.info("YOU ARE OUT OF LOGIC: " + ", ".join(errors))
        logger.info("YOU ARE OUT OF LOGIC: " + ", ".join(errors))
        logger.info("YOU ARE OUT OF LOGIC: " + ", ".join(errors))
        logger.info("YOU ARE OUT OF LOGIC: " + ", ".join(errors))
        logger.info("YOU ARE OUT OF LOGIC: " + ", ".join(errors))
    return errors
    

def rarity_check(total_recieved_items, rarity: str, equipmentId: str) -> str | None:
    valid = True
    if rarity == "Unique":
        valid = True if f"Unique {equipmentId}" in [i["name"] for i in total_recieved_items] else False
    elif rarity == "Rare":
        valid = True if f"Rare {equipmentId}" in [i["name"] for i in total_recieved_items] else False
    elif rarity == "Magic":
        valid = True if f"Magic {equipmentId}" in [i["name"] for i in total_recieved_items] else False
    else:
        valid = True if f"Normal {equipmentId}" in [i["name"] for i in total_recieved_items] else False
    
    if not valid:
        return equipmentId
    else: 
        return None


#async def update_filter(ctx: "PathOfExileContext") -> bool:
#    item_filter_string = ""
#    missing_location_ids = ctx.missing_locations
#    for base_item_location_id in missing_location_ids:
#
##        item_text = Items.get(base_item_location_id, "Unknown Item") # this needs to be the scouted item name, unless the options specify otherwise
#        network_item = ctx.locations_info[base_item_location_id]
#        item_text = tts.get_item_name_tts_text(ctx, network_item)
#        filename =  f"{item_text.lower()}_{tts.WPM}.wav"
#        base_item_location_name = ctx.location_names.lookup_in_game(base_item_location_id)
#        item_filter_string += itemFilter.generate_item_filter_block(base_item_location_name, f"{itemFilter.filter_sounds_dir_name}/{fileHelper.safe_filename(filename)}")+ "\n\n"
#
#    if item_filter_string:
#        itemFilter.write_item_filter(item_filter_string)
#        logger.info(f"Item filter updated with {len(missing_location_ids)} items.")
#    return True

async def update_filter_to_invalid_char_filter(errors: list[str], enable_tts: bool = True, tts_speed: int = 250) -> None:

    if enable_tts:
        if len(errors) > 1:
            error_text = " and ... ".join(errors)
        else:
            error_text = errors[0]
        filename = f"{fileHelper.short_hash(error_text)}_{tts.WPM}.wav" # this could be a long text, so we use a hash
        full_error_text = f"YOU ARE OUT OF LOGIC: {error_text}"
        await tts.safe_tts_async(
            text=full_error_text,
            filename=itemFilter.filter_sounds_path / f"{filename}",
            rate=tts_speed
        )
        invalid_item_filter_string = itemFilter.generate_invalid_item_filter_block(f"{itemFilter.filter_sounds_dir_name}/{filename}")
        itemFilter.write_item_filter(invalid_item_filter_string, item_filter_import=None)
    else:
        invalid_item_filter_string = itemFilter.generate_invalid_item_filter_block_without_sound()
        itemFilter.write_item_filter(invalid_item_filter_string, item_filter_import=None)


def get_found_items(char: gggAPI.Character) -> set:
    try:
        full_list = char.inventory + char.equipment
        for item in full_list:
            found_items_set.add(item.baseType)
            if _debug and _verbose_debug:
                logger.info(f"[DEBUG] Item in inventory: {item.baseType}")
    except Exception as e:
        logger.info(f"Error fetching found items: {e}")
        raise e
    return found_items_set