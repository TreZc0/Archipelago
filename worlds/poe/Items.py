from BaseClasses import Item, ItemClassification
from typing import TypedDict, Dict, Set

from worlds.poe.data import ItemTable

class ItemDict(TypedDict, total=False): 
    classification: ItemClassification 
    count: int | None
    id : int
    name: str 
    category: list[str]
    reqLevel: int | None

class PathOfExileItem(Item):
    """
    Represents an item in the Path of Exile world.
    This class can be extended to include specific item properties and methods.
    """
    game = "Path of Exile"
    itemInfo: ItemDict
    category = list[str]()
    
    def create_item(self, item: str):
        # this is called when AP wants to create an item by name (for plando, start inventory, item links) or when you call it from your own code
        
        # get the item from the item table, by name
        id = self.item_name_to_id.get(item)
        item = ItemTable.item_table.get(id)
        classification = item.get("classification", None) # default to progression, but none for developing
        return PathOfExileItem(item, classification, self.item_name_to_id[item], self.player)



#def get_items():
#    """
#    Returns a list of all items available in the Path of Exile world.
#    This function can be extended to include specific item definitions.
#    """
#    return items



item_table: Dict[int, ItemDict] = ItemTable.item_table

def get_flask_items(table: Dict[int, ItemDict] = item_table) -> list[ItemDict]:
    """
    Returns a set of all flask items available in the Path of Exile world.
    """
    return [item for item in table.values() if "Flask" in item["category"]]

def get_character_class_items(table: Dict[int, ItemDict] = item_table) -> list[ItemDict]:
    """
    Returns a set of all character class items available in the Path of Exile world.
    """
    return [item for item in table.values() if "Character Class" in item["category"]] 

def get_ascendancy_items(table: Dict[int, ItemDict] = item_table) -> list[ItemDict]:
    """
    Returns a set of all ascendancy items available in the Path of Exile world.
    """
    return [item for item in table.values() if "Ascendancy" in item["category"]]

def get_ascendancy_class_items(class_name: str, table: Dict[int, ItemDict] = item_table) -> list[ItemDict]:
    """
    Returns a set of all ascendancy items available for a specific class in the Path of Exile world.
    """
    return [item for item in table.values() if "Ascendancy" in item["category"] and class_name in item["category"]]

def get_main_skill_gem_items(table: Dict[int, ItemDict] = item_table) -> list[ItemDict]:
    """
    Returns a set of all main skill gem items available in the Path of Exile world.
    """
    return [item for item in table.values() if "MainSkillGem" in item["category"]]

def get_main_skill_gem_items_under_level(level: int, table: Dict[int, ItemDict] = item_table) -> list[ItemDict]:
    """
    Returns a list of all Main skill gem items available under a specific level in the Path of Exile world.
    """
    return [item for item in table.values() if "MainSkillGem" in item["category"] and (item["reqLevel"] is None or item["reqLevel"] < level)]

def get_gear_items(table: Dict[int, ItemDict] = item_table) -> list[ItemDict]:    
    """
    Returns a list of all gear items available in the Path of Exile world.
    """
    return [item for item in table.values() if "Gear" in item["category"]]

def get_max_links_items(table: Dict[int, ItemDict] = item_table) -> list[ItemDict]:
    """
    Returns a list of all max links items available in the Path of Exile world.
    """
    return [item for item in table.values() if "max links" in item["category"]]