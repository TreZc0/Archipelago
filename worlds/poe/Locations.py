from typing import Dict, TypedDict
from BaseClasses import Location
from worlds.poe.data import LocationTable


class PathOfExileLocation(Location):
    game = "Path of Exile"

def get_base_item_locations ():
    """
    Returns a list of all locations based on base items types in the Path of Exile world.

    """
    return base_item_type_locations


def get_location_id_from_item_name(item_name: str) -> int | None:
    """
    Returns the location ID for a given item name.
    
    Args:
        item_name (str): The name of the item to find the location ID for.
    
    Returns:
        int | None: The location ID if found, otherwise None.
    """
    for loc_id, loc in base_item_type_locations.items():
        if loc['baseItem'] == item_name:
            return loc_id
    return None

class LocationDict(TypedDict, total=False):
    baseItem: str|None
    dropLevel: int|None
    level: int|None
    name: str
    act: int
    id: int

goal_items = {
    "shaper": [
        "Shaper's Touch",
        "Voidwalker",
        "Solstice Vigil",
        "Dying Sun",
    ],
    "uber_shaper": [
        "Echoes of Creation",
        "Entropic Devastation",
        "The Tides of Time",
        "Starforge",
    ],
    "elder":[
        "Cyclopean Coil",
        "Blasphemer's Grasp"
        "Nebuloch",
        "Hopeshredder",
        "Shimmeron",
        "Impresence",
    ],
    "uber_elder": [
        "Mark of the Shaper",
        "Mark of the Elder",
        "Voidfletcher",
        "Indigon",
        "Disintegrator",
    ],
    "uber_uber_elder": [
        "Call of the Void",
        "The Devourer of Minds",
        "Soul Ascension",
        "The Eternity Shroud",
        "Voidforge",
    ],
    "atziri":[
        "The Vertex",
        "Atziri's Splendour",
        "Atziri's Rule",
        "Triumvirate Authority",
        "Atziri's Acuity",
        "Atziri's Reflection",
        "Atziri's Disfavour",
    ],
    "sirus":[
        "Crown of the Inward Eye"
        "Hands of the High Templar"
        "The Burden of Truth"
        "Thread of Hope"
    ],
    "uber_sirus":[
        "Thread of Hope",
        "The Tempest Rising",
        "Oriath's End",
        "The Saviour",
    ],
    "maven":[
        "Legacy of Fury",
        "Graven's Secret",
        "Arn's Anguish",
        "Olesya's Delight",
        "Doppelgänger Guise",
        "Echoforge",
    ],
    "uber_maven":[
        "Viridi's Veil",
        "Impossible Escape",
        "Grace of the Goddess",
        "Progenesis",
    ],
    "exarch":[
        "Dawnbreaker",
        "Dawnstrider",
        "Dissolution of the Flesh",
    ],
    "uber_exarch":[
        "The Annihilating Light",
        "Annihilation's Approach",
        "Crystallised Omniscience",
        "The Celestial Brace",
    ],
    "eater":[
        "Inextricable Fate",
        "The Gluttonous Tide",
        "Melding of the Flesh",
    ],
    "uber_eater":[
        "Ravenous Passion",
        "Ashes of the Stars",
        "Nimis",
    ],
    "incarnation_of_neglect":[
        "The Arkhon's Tools",
        "Venarius' Astrolabe",
        "Legacy of the Rose",
    ],
    "incarnation_of_fear":[
        "Servant of Decay",
        "Coiling Whisper",
        "Enmity's Embrace",
    ],
    "incarnation_of_dread":[
        "The Dark Monarch",
        "Seven Teachings",
        "Wine of the Prophet",
    ]
}

acts = [
    {"act": 0.2, "maxMonsterLevel": 2}, # man these roas are tough lol.
    {"act": 1, "maxMonsterLevel": 13},
    {"act": 2, "maxMonsterLevel": 23},
    {"act": 3, "maxMonsterLevel": 33},
    {"act": 4, "maxMonsterLevel": 40},
    {"act": 5, "maxMonsterLevel": 45},
    {"act": 6, "maxMonsterLevel": 50},
    {"act": 7, "maxMonsterLevel": 54},
    {"act": 8, "maxMonsterLevel": 60},
    {"act": 9, "maxMonsterLevel": 64},
    {"act": 10, "maxMonsterLevel": 67},
    {"act": 11, "maxMonsterLevel": 86},
]

def get_lvl_location_name_from_lvl(level: int) -> str: return f"Reach Level {level}"
# based off of baseItemTypes.json
get_location_id_from_level_location_name = {i ['name']: i['id'] for i in LocationTable.level_location_table.values() if 'name' in i}
base_item_names_set = LocationTable.base_item_set
base_item_type_locations: Dict[int, LocationDict] = LocationTable.base_item_location_table
level_locations: Dict[int, LocationDict] = LocationTable.level_location_table
full_locations = {**base_item_type_locations, **level_locations}
base_item_types_by_name: Dict[str, LocationDict] = {loc['baseItem']: loc for loc in base_item_type_locations.values()}