import asyncio

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from worlds.poe.Client import PathOfExileContext
    from worlds.poe import PathOfExileWorld
from . import itemFilter
from . import baseItemTypes
from . import gggAPI
from . import fileHelper
from . import inputHelper
from . import tts

import worlds.poe.Items as Items
import worlds.poe.Locations as Locations

character_name = "DefaultCharacter"
found_items_dict = {}
found_items_set = set()
save_path = "found_items.txt"
total_items = set()
is_char_in_logic = True
_debug = True
total_items.update(baseItemTypes.get_base_item_types())



async def when_enter_new_zone(line: str):
    """
    Callback function that is called when a new zone is entered.
    It validates the character and updates the item filter accordingly.

    Args:
        line (str): The line from the log file indicating the new zone entry.
    """
    global is_char_in_logic
    await validate_and_update(character_name)
    await asyncio.sleep(0.5)  # Allow some time for the filter to update
    await inputHelper.send_poe_text("/itemfilter __ap")

async def validate_and_update(character_name: str = character_name, ctx: "PathOfExileContext" = None) -> bool:
    if ctx is None:
        # something is wrong, are we not connected?
        print("Context is None, cannot validate character.")
        return False
    
    char = {}
    try: 
        char = await gggAPI.get_character(character_name)
    except Exception as e:
        print(f"Error fetching character {character_name}: {e}")
        return False
    
    global is_char_in_logic
    try:
        is_char_in_logic = await validate_char(char)
    except Exception as e:
        print(f"Error validating character: {e}")
        return False
    found_items_set = await get_found_items(char)
    # for each item in found_items_set: send locations via ctx
    if is_char_in_logic:
        for item in found_items_set:
            if _debug:
                print(f"[DEBUG] Found item: {item}")
            location_id = Locations.get_location_id_from_item_name(item)
            await ctx.check_locations(location_id)
        await update_filter(ctx)
    
    await fileHelper.write_set_to_file(found_items_set, save_path)
    await update_filter(ctx.missing_locations)



async def validate_char(character: gggAPI.Character, ctx: "PathOfExileContext") -> bool:
    # Perform validation logic here

    if character is None:
        print("Character is None, cannot validate.")
        return False

    valid = True
    
    total_recieved_items = list()
    for item in ctx.items_received:
        total_recieved_items.append(Items.item_table.get(item))

    simple_equipment_slots = ["BodyArmour","Amulet","Belt","Boots","Gloves","Helmet"]
    
    for equipped_item in character.equipment:
        rarity = equipped_item.get("rarity")
        
        # simple checks.
        for slot in simple_equipment_slots:
            if equipped_item.inventoryId == slot:
                valid = rarity_check(total_recieved_items, rarity, slot)
                
        if equipped_item.inventoryId == "Ring":
            valid = rarity_check(total_recieved_items, rarity, "Ring (left)")
        if equipped_item.inventoryId == "Ring2":
            valid = rarity_check(total_recieved_items, rarity, "Ring (right)")
        if equipped_item.inventoryId == "Offhand":
            if equipped_item.baseType in Items.quiver_base_types:
                valid = rarity_check(total_recieved_items, rarity, "Quiver")
            else:
                valid = rarity_check(total_recieved_items, rarity, "Shield")
        if equipped_item.inventoryId == "Weapon":
            for prop in equipped_item.properties:
                prop_name = prop.get("name") 
                for weapon_base_type in Items.weapon_base_types:
                    if prop_name.lower().endswith(weapon_base_type.lower()):
                        valid = rarity_check(total_recieved_items, rarity, weapon_base_type)
                        
        normal_flask_count = 0            
        magic_flask_count = 0
        unique_flask_count = 0
        if equipped_item.inventoryId == "Flask":
            flask_rarity = equipped_item.get("rarity")
            if flask_rarity == "Normal":
                normal_flask_count += 1
            elif flask_rarity == "Magic":
                magic_flask_count += 1
            elif flask_rarity == "Unique":
                unique_flask_count += 1
                
    if normal_flask_count > total_recieved_items.count("Normal Flask"):
        valid = False
    if magic_flask_count > total_recieved_items.count("Magic Flask"):
        valid = False
    if unique_flask_count > total_recieved_items.count("Unique Flask"):
        valid = False

    return valid

def rarity_check(total_recieved_items, rarity: str, equipmentId: str) -> bool:
    if rarity == "Unique":
        valid = True if f"Unique {equipmentId}" in total_recieved_items else False
    elif rarity == "Rare":
        valid = True if f"Rare {equipmentId}" in total_recieved_items else False
    elif rarity == "Magic":
        valid = True if f"Magic {equipmentId}" in total_recieved_items else False
    else:
        valid = True if f"Normal {equipmentId}" in total_recieved_items else False
    return valid

async def update_filter(ctx: "PathOfExileContext") -> bool:
    item_filter_string = ""
    missing_location_ids = ctx.missing_locations
    for base_item_location_id in missing_location_ids:
        item_text = ctx.location_to_item_name.get(base_item_location_id, "Unknown Item")
        filename =  f"{item_text.lower()}_{tts.WPM}.wav"
        base_item_location_name = ctx.location_names.lookup_in_game(base_item_location_id)
        await tts.text_to_speech_if_doesnt_exist(
            text=f"{item_text}",
            filename=itemFilter.filter_sounds_path / filename,
            tts_rate_wpm=tts.WPM
        )
        item_filter_string += itemFilter.generate_item_filter_block(base_item_location_name, f"{itemFilter.filter_sounds_dir_name}/{filename}.wav") + "\n\n"

    if item_filter_string:
        itemFilter.write_item_filter(item_filter_string)
        print(f"Item filter updated with {len(missing_location_ids)} items.")
    return True


async def update_filter_to_invalid_char_filter():
    invalid_alert_sound = "apsound/invalid.wav"
    invalid_item_filter_string = f""""Show
{itemFilter.invalid_style_string}
{invalid_alert_sound}"""
    itemFilter.write_item_filter(invalid_item_filter_string, item_filter_import=None)


async def get_found_items(char: gggAPI.Character) -> set:
    """
    Fetches the found items for a given character from the GGG API.

    Args:
        character_name (str): The name of the character to fetch items for.

    Returns:
        dict: A dictionary containing the found items.
    """
    try:
        for item in char.inventory:
            found_items_set.add(item.baseType)
            if _debug:
                print(f"[DEBUG] Item in inventory: {item.baseType}")
    except Exception as e:
        print(f"Error fetching found items: {e}")
        raise e
    return found_items_set

async def load_found_items_from_file(file_path: str = save_path ) -> set:
    """
    Loads the found items from a file.
    Returns:
        set: A set containing the found items.
    """
    global found_items_set
    found_set = set()
    try:
        found_set = await fileHelper.read_set_from_file(file_path)
    except Exception as e:
        print(f"Error loading found items: {e}")

    found_items_set.update(found_set)
    return found_items_set