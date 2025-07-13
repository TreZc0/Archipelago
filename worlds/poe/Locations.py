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


class LocationDict(TypedDict, total=False):
    baseItem: str
    dropLevel: int
    act: int

# based off of baseItemTypes.json
base_item_types: Dict[int, LocationDict] = LocationTable.location_table