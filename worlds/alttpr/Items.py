from __future__ import annotations

import logging
from typing import List, TYPE_CHECKING

from BaseClasses import Item, ItemClassification

from .ALttPDoorRandomizer.Items import ItemFactory, item_table
from .Regions import get_event_locations

if TYPE_CHECKING:
    from .World import ALttPRWorld


logger = logging.getLogger("alttpr")

# TODO: This feels inefficient to run every time, there must be a way to store the result without copy/pasting code from Door Rando
item_name_to_id = {}
for item_name, item_data in item_table.items():
    id = item_data[3]
    if id == 999 or type(id) is not int or id == 0x6A:  # 0x6A is the Triforce
        id = None
    item_name_to_id[item_name] = id

# TODO: Pretty sure this can be deleted? Maybe?
default_items_dict = {
    "bow": 0,
    "progressivebow": 2,
    "boomerang": 1,
    "redmerang": 1,
    "hookshot": 1,
    "mushroom": 1,
    "powder": 1,
    "firerod": 1,
    "icerod": 1,
    "bombos": 1,
    "ether": 1,
    "quake": 1,
    "lamp": 1,
    "hammer": 1,
    "shovel": 1,
    "flute": 1,
    "bugnet": 1,
    "book": 1,
    "bottle": 4,
    "somaria": 1,
    "byrna": 1,
    "cape": 1,
    "mirror": 1,
    "boots": 1,
    "powerglove": 0,
    "titansmitt": 0,
    "progressiveglove": 2,
    "flippers": 1,
    "pearl": 1,
    "heartpiece": 24,
    "heartcontainer": 10,
    "sancheart": 1,
    "sword1": 0,
    "sword2": 0,
    "sword3": 0,
    "sword4": 0,
    "progressivesword": 4,
    "shield1": 0,
    "shield2": 0,
    "shield3": 0,
    "progressiveshield": 3,
    "mail2": 0,
    "mail3": 0,
    "progressivemail": 2,
    "halfmagic": 1,
    "quartermagic": 0,
    "bombsplus5": 0,
    "bombsplus10": 0,
    "arrowsplus5": 0,
    "arrowsplus10": 0,
    "arrow1": 1,
    "arrow10": 12,
    "bomb1": 0,
    "bomb3": 16,
    "bomb10": 1,
    "rupee1": 2,
    "rupee5": 4,
    "rupee20": 28,
    "rupee50": 7,
    "rupee100": 1,
    "rupee300": 5,
    "blueclock": 0,
    "greenclock": 0,
    "redclock": 0,
    "silversupgrade": 0,
    "generickeys": 0,
    "triforcepieces": 0,
    "triforcepiecesgoal": 0,
    "triforce": 0,
    "rupoor": 0,
    "rupoorcost": 10
}

# Some of the internal Door Randomizer names for items are not the community standard names for items (e.g. Ocarina instead of Flute),
# we should try to keep names as standardized as possible to avoid confusion.
# TODO: Better name.
# TODO: Should have two separate dicts/functions, one for dr_to_ap and one for ap_to_dr
dr_ap_different_names = {
    "Cape": "Magic Cape",
    "Flute": "Ocarina",
    "Magic Cape": "Cape",
    "Ocarina": "Flute",
    "Progressive Armor": "Progressive Mail",
    "Progressive Mail": "Progressive Armor",
}

progressive_items = [
    "Big Key (Escape)",
    "Big Key (Eastern Palace)",
    "Big Key (Desert Palace)",
    "Big Key (Tower of Hera)",
    "Big Key (Palace of Darkness)",
    "Big Key (Swamp Palace)",
    "Big Key (Skull Woods)",
    "Big Key (Thieves Town)",
    "Big Key (Ice Palace)",
    "Big Key (Misery Mire)",
    "Big Key (Turtle Rock)",
    "Big Key (Ganons Tower)",
    "Bombos",
    "Book of Mudora",
    "Bottle",
    "Bottle (Red Potion)",
    "Bottle (Green Potion)",
    "Bottle (Blue Potion)",
    "Bottle (Fairy)",
    "Bottle (Bee)",
    "Bottle (Good Bee)",
    "Cane of Byrna",
    "Cane of Somaria",
    "Ether",
    "Fire Rod",
    "Flippers",
    "Flute",
    "Hammer",
    "Hookshot",
    "Ice Rod",
    "Lamp",
    "Magic Cape",
    "Magic Mirror",
    "Magic Powder",
    "Magic Upgrade (1/2)",
    "Moon Pearl",
    "Mushroom",
    "Pegasus Boots",
    "Progressive Bow",
    "Progressive Glove",
    "Progressive Shield",
    "Progressive Sword",
    "Quake",
    "Shovel",
    "Small Key (Escape)",
    "Small Key (Eastern Palace)",
    "Small Key (Desert Palace)",
    "Small Key (Tower of Hera)",
    "Small Key (Agahnims Tower)",
    "Small Key (Palace of Darkness)",
    "Small Key (Swamp Palace)",
    "Small Key (Skull Woods)",
    "Small Key (Thieves Town)",
    "Small Key (Ice Palace)",
    "Small Key (Misery Mire)",
    "Small Key (Turtle Rock)",
    "Small Key (Ganons Tower)",
    "Triforce Piece",
    "Green Clock",  # Placeholder for progressive AP items
]

useful_items = [
    "Blue Boomerang",
    "Boss Heart Container",
    "Progressive Mail",
    "Red Boomerang",
    "Rupees (300)",
    "Sanctuary Heart Container",
    "Blue Clock",  # Placeholder for useful AP items
]

filler_items = [
    "Bug Catching Net",
    "Rupee (1)",
    "Rupees (5)",
    "Rupees (20)",
    "Rupees (50)",
    "Rupees (100)",
    "Single Arrow",
    "Arrows (10)",
    "Bombs (3)",
    "Bombs (10)",
    "Piece of Heart",
    "Map (Escape)",
    "Map (Eastern Palace)",
    "Map (Desert Palace)",
    "Map (Tower of Hera)",
    "Map (Palace of Darkness)",
    "Map (Swamp Palace)",
    "Map (Skull Woods)",
    "Map (Thieves Town)",
    "Map (Ice Palace)",
    "Map (Misery Mire)",
    "Map (Turtle Rock)",
    "Map (Ganons Tower)",
    "Compass (Eastern Palace)",
    "Compass (Desert Palace)",
    "Compass (Tower of Hera)",
    "Compass (Palace of Darkness)",
    "Compass (Swamp Palace)",
    "Compass (Skull Woods)",
    "Compass (Thieves Town)",
    "Compass (Ice Palace)",
    "Compass (Misery Mire)",
    "Compass (Turtle Rock)",
    "Compass (Ganons Tower)",
    "Red Clock",  # Placeholder for filler AP items
]


class ALttPRItem(Item):
    game = "The Legend of Zelda: A Link to the Past"


def get_dungeon_items(world: ALttPRWorld) -> List[str]:
    dungeon_items = []
    if not world.options.map_shuffle.value:
        dungeon_items.extend([item for item in filler_items if item.startswith("Map")])
    if not world.options.compass_shuffle.value:
        dungeon_items.extend([item for item in filler_items if item.startswith("Compass")])

    # TODO: Key drop shuffle + keysanity should remove this line
    dungeon_items.extend([item for item in progressive_items if item.startswith("Small Key")])

    if not world.options.big_key_shuffle.value:
        dungeon_items.extend([item for item in progressive_items if item.startswith("Big Key")])
    #elif not world.options.key_drop_shuffle.value:
    else:
        dungeon_items.append("Big Key (Escape)")

    return dungeon_items


def get_random_filler_item_name(world: ALttPRWorld) -> str:
    raise NotImplementedError("get_random_filler_item_name is not implemented yet")


def create_item(world: ALttPRWorld, name: str, classification: ItemClassification) -> ALttPRItem:
    door_rando_item = ItemFactory(name, 1)
    item_name_to_id[name] = door_rando_item.code
    new_name = dr_ap_different_names[name] if name in dr_ap_different_names else name
    return ALttPRItem(new_name, classification, door_rando_item.code, world.player)


def create_all_items(world: ALttPRWorld) -> None:
    # If we're playing Standard mode with keysanity, we need to manually place the escape small key to prevent
    # getting BK'd in the escape sequence. This key is placed later in the pre_fill() stage of generation.
    dr_itempool = world.door_rando_world.itempool.copy()
    if world.options.world_mode.value == "standard" and world.options.small_key_shuffle.value:
        escape_key = [item for item in world.door_rando_world.get_items() if item.name == "Small Key (Escape)"][0]
        dr_itempool.remove(escape_key)

    # Itempool will not include dungeon items unless keysanity is enabled.
    # Key drop keys are also not in the item pool unless key drop in enabled.
    itempool = []
    for item in dr_itempool:
        ap_item_name = item.name if item.name not in dr_ap_different_names else dr_ap_different_names[item.name]

        if ap_item_name in progressive_items:
            classification = ItemClassification.progression
        elif ap_item_name in useful_items:
            classification = ItemClassification.useful
        elif ap_item_name in filler_items:
            classification = ItemClassification.filler
        else:
            logger.error(f"Item {item.name} not found in any item list, cannot determine classification.")
            raise Exception()

        ap_item = ALttPRItem(ap_item_name, classification, item.code, world.player)
        itempool.append(ap_item)

    world.multiworld.itempool += itempool


def place_pre_fill_items(world: ALttPRWorld) -> None:
    # Place all items that cannot be randomized into any world, such as pendants/crystals, dungeon items, and special events like killing Agahnim
    event_locations = get_event_locations(world)
    for event_location_name, event_item_name in event_locations.items():
        ap_item = ALttPRItem(event_item_name, ItemClassification.progression, None, world.player)
        event_location = world.multiworld.get_location(event_location_name, world.player)
        event_location.place_locked_item(ap_item)

    prize_locations = [location for location in world.multiworld.get_unfilled_locations(world.player) if " - Prize" in location.name]
    for prize_location in prize_locations:
        dr_prize_location = world.door_rando_world.get_location(prize_location.name, 1)
        ap_item = ALttPRItem(dr_prize_location.item.name, ItemClassification.progression, None, world.player)
        target_location = world.multiworld.get_location(prize_location.name, world.player)
        target_location.place_locked_item(ap_item)

    for dungeon_item in get_dungeon_items(world):
        dr_item_name = dungeon_item if dungeon_item not in dr_ap_different_names else dr_ap_different_names[dungeon_item]

        # All dungeon items should already be placed in a location. If keysanity is enabled but not key drop shuffle, then
        # small keys dropped by pots/enemies will already be placed, but other small keys won't.
        item_locations = world.door_rando_world.find_items(dr_item_name, 1)
        if not item_locations:
            if world.options.small_key_shuffle.value and dr_item_name.startswith("Small Key"):
                continue
            else:
                logger.error(f"Could not find dungeon item {dungeon_item} in door rando item list.")
                raise Exception()

        for location in item_locations:
            dr_dungeon_item = location.item
            if dr_dungeon_item.smallkey or dr_dungeon_item.bigkey:
                classification = ItemClassification.progression
            else:
                classification = ItemClassification.filler
            ap_item = ALttPRItem(dungeon_item, classification, dr_dungeon_item.code, world.player)
            target_location = world.multiworld.get_location(dr_dungeon_item.location.name, world.player)
            target_location.place_locked_item(ap_item)

    if world.options.world_mode.value == "standard":
        # In Standard mode, Link's Uncle will always have a weapon which was not added to the multiworld itempool,
        # unless the player starts with a sword or hammer.
        uncle_item = world.door_rando_world.get_location("Link's Uncle", 1).item
        if uncle_item is not None:
            ap_item = ALttPRItem(uncle_item.name, ItemClassification.progression, uncle_item.code, world.player)
            links_uncle_location = world.multiworld.get_location("Link's Uncle", world.player)
            links_uncle_location.place_locked_item(ap_item)

        # TODO: Key drop
        # The small key for the escape sequence should be sphere 0, to prevent the player
        # from being near-instantly BK'd.
        if world.options.small_key_shuffle.value:
            small_key_locations = ["Link's Uncle", "Secret Passage", "Hyrule Castle - Map Chest",
                                   "Hyrule Castle - Boomerang Chest", "Hyrule Castle - Zelda's Chest", "Sewers - Dark Cross"]
            world.random.shuffle(small_key_locations)
            for key_location_name in small_key_locations:
                key_location = world.multiworld.get_location(key_location_name, world.player)
                if key_location.item is None:
                    key_item = ALttPRItem("Small Key (Escape)", ItemClassification.progression, ItemFactory("Small Key (Escape)", 0).code, world.player)
                    key_location.place_locked_item(key_item)
                    break
