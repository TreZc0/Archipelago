from typing import Dict, TypedDict
from BaseClasses import Location
from worlds.poe.data import LocationTable


class PathOfExileLocation(Location):
    game = "Path of Exile"

def get_base_item_locations ():
    """
    Returns a list of all locations based on base items types in the Path of Exile world.

    """
    return base_item_types


def get_location_id_from_item_name(item_name: str) -> int | None:
    """
    Returns the location ID for a given item name.
    
    Args:
        item_name (str): The name of the item to find the location ID for.
    
    Returns:
        int | None: The location ID if found, otherwise None.
    """
    for loc_id, loc in base_item_types.items():
        if loc['baseItem'] == item_name:
            return loc_id
    return None

class LocationDict(TypedDict, total=False):
    baseItem: str
    dropLevel: int
    act: int
    id: int

# based off of baseItemTypes.json
base_item_types: Dict[int, LocationDict] = LocationTable.location_table