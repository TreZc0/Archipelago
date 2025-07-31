import typing
if typing.TYPE_CHECKING:
    from worlds.poe import PathOfExileWorld
    from worlds.poe.Options import PathOfExileOptions

from BaseClasses import Item, ItemClassification
from typing import TypedDict, Dict, Set

from worlds.poe.data import ItemTable
from worlds.poe import Locations

import logging
logger = logging.getLogger("poe.Items")

class ItemDict(TypedDict, total=False): 
    classification: ItemClassification 
    count: int | None
    id : int
    name: str 
    category: list[str]
    reqLevel: int | None
    reqToUse: list[str] | None

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
memoize_cache: Dict[str, list[ItemDict]] = {}

def deprioritize_non_logic_gems(world: "PathOfExileWorld", table: Dict[int, ItemDict]) -> Dict[int, ItemDict]:
    opt: PathOfExileOptions = world.options
    
    still_required_gem_ids = set()
    
    for act in range(1, world.goal_act + 1):
        main_gems_for_act = [item for item in get_main_skill_gem_items() if item["reqLevel"] <= Locations.acts[act]["maxMonsterLevel"]]
        support_gems_for_act = [item for item in get_support_gem_items() if item["reqLevel"] <= Locations.acts[act]["maxMonsterLevel"]]
        utility_gems_for_act = [item for item in get_utility_skill_gem_items() if item["reqLevel"] <= Locations.acts[act]["maxMonsterLevel"]]
        
        if main_gems_for_act:  
            selected_gems = world.random.sample(main_gems_for_act, k=min(opt.skill_gems_per_act.value, len(main_gems_for_act)))
            selected_gems.extend(world.random.sample(support_gems_for_act, k=min(opt.skill_gems_per_act.value, len(support_gems_for_act))))
            selected_gems.extend(world.random.sample(utility_gems_for_act, k=min(opt.skill_gems_per_act.value, len(utility_gems_for_act))))


            still_required_gem_ids.update(item["id"] for item in selected_gems)
    
    for item in table.values():
        if "MainSkillGem" in item["category"]\
            or "SupportGem" in item["category"] \
            or "UtilSkillGem" in item["category"] \
                :
            if item["id"] in still_required_gem_ids:
                item["classification"] = ItemClassification.progression
            else:
                item["classification"] = ItemClassification.filler
                
    return table

def cull_items_to_place(world: "PathOfExileWorld", items: Dict[int, ItemDict], locations: Dict[int, ItemDict]) -> Dict[int, ItemDict]:
    total_items_count = sum(item.get("count", 1) for item in items.values())
    total_locations_count = len(locations)
    amount_to_cull = total_items_count - total_locations_count

    remove_items_ids = set()
    
    filler_items = [item_id for item_id, item in items.items() if item["classification"] == ItemClassification.filler]
    if not filler_items:
        logger.error("[ERROR] No filler items found to remove. This should not happen.")
    item_to_remove = world.random.sample(filler_items, k=amount_to_cull)
    remove_items_ids.update(item_to_remove)

    for item_id in remove_items_ids:
        items.pop(item_id, None)


def get_flask_items(table: Dict[int, ItemDict] = item_table) -> list[ItemDict]:
    if table is item_table and "Flask" in memoize_cache:
        return memoize_cache["Flask"]
    result = [item for item in table.values() if "Flask" in item["category"]]
    if table is item_table: memoize_cache["Flask"] = result
    return result

def get_character_class_items(table: Dict[int, ItemDict] = item_table) -> list[ItemDict]:
    if table is item_table and "Character Class" in memoize_cache:
        return memoize_cache["Character Class"]
    result = [item for item in table.values() if "Character Class" in item["category"]]
    if table is item_table: memoize_cache["Character Class"] = result
    return result

def get_ascendancy_items(table: Dict[int, ItemDict] = item_table) -> list[ItemDict]:
    if table is item_table and "Ascendancy" in memoize_cache:
        return memoize_cache["Ascendancy"]
    result = [item for item in table.values() if "Ascendancy" in item["category"]]
    if table is item_table: memoize_cache["Ascendancy"] = result
    return result

def get_ascendancy_class_items(class_name: str, table: Dict[int, ItemDict] = item_table) -> list[ItemDict]:
    if table is item_table and f"{class_name} Ascendancy Class" in memoize_cache:
        return memoize_cache[f"{class_name} Ascendancy Class"]
    result = [item for item in table.values() if "Ascendancy" in item["category"] and f"{class_name} Class" in item["category"]]
    if table is item_table: memoize_cache[f"{class_name} Ascendancy Class"] = result
    return result

def get_main_skill_gem_items(table: Dict[int, ItemDict] = item_table) -> list[ItemDict]:
    if table is item_table and "MainSkillGem" in memoize_cache:
        return memoize_cache["MainSkillGem"]
    result = [item for item in table.values() if "MainSkillGem" in item["category"]]
    if table is item_table: memoize_cache["MainSkillGem"] = result
    return result

def get_support_gem_items(table: Dict[int, ItemDict] = item_table) -> list[ItemDict]:
    if table is item_table and "SupportGem" in memoize_cache:
        return memoize_cache["SupportGem"]
    result = [item for item in table.values() if "SupportGem" in item["category"]]
    if table is item_table: memoize_cache["SupportGem"] = result
    return result

def get_utility_skill_gem_items(table: Dict[int, ItemDict] = item_table) -> list[ItemDict]:
    if table is item_table and "UtilSkillGem" in memoize_cache:
        return memoize_cache["UtilSkillGem"]
    result = [item for item in table.values() if "UtilSkillGem" in item["category"]]
    if table is item_table: memoize_cache["UtilSkillGem"] = result
    return result

def get_all_gems(table: Dict[int, ItemDict] = item_table) -> list[ItemDict]:
    if table is item_table and "AllGems" in memoize_cache:
        return memoize_cache["AllGems"]
    result = get_main_skill_gem_items(table) + get_support_gem_items(table) + get_utility_skill_gem_items(table)
    if table is item_table: memoize_cache["AllGems"] = result
    return result

def get_main_skill_gems_by_required_level(level_minimum:int=0, level_maximum:int=100, table: Dict[int, ItemDict] = item_table) -> list[ItemDict]:
    key = f"MainSkillGems_{level_minimum}_{level_maximum}"
    if table is item_table and key in memoize_cache:
        return memoize_cache[key]
    result = [item for item in table.values() if "MainSkillGem" in item["category"] and (item["reqLevel"] is not None and (level_minimum <= item["reqLevel"] <= level_maximum))]
    if table is item_table: memoize_cache[key] = result
    return result

def get_main_skill_gems_by_required_level_and_useable_weapon(available_weapons: set[str], level_minimum:int=0, level_maximum:int=100, table: Dict[int, ItemDict] = item_table) -> list[ItemDict]:
    return [item for item in table.values() if "MainSkillGem" in item["category"] and (item["reqLevel"] is not None and (level_minimum <= item["reqLevel"] <= level_maximum))
            and (any(weapon in available_weapons for weapon in item.get("reqToUse", [])) or not item.get("reqToUse", []))] # we have the weapon, or there are no reqToUse

def get_support_gems_by_required_level(level_minimum:int=0, level_maximum:int=100, table: Dict[int, ItemDict] = item_table) -> list[ItemDict]:
    key = f"SupportGems_{level_minimum}_{level_maximum}"
    if table is item_table and key in memoize_cache:
        return memoize_cache[key]
    result = [item for item in table.values() if "SupportGem" in item["category"] and (item["reqLevel"] is not None and (level_minimum <= item["reqLevel"] <= level_maximum))]
    if table is item_table: memoize_cache[key] = result
    return result

def get_utility_skill_gems_by_required_level(level_minimum:int=0, level_maximum:int=100, table: Dict[int, ItemDict] = item_table) -> list[ItemDict]:
    key = f"UtilitySkillGems_{level_minimum}_{level_maximum}"
    if table is item_table and key in memoize_cache:
        return memoize_cache[key]
    result = [item for item in table.values() if "UtilityGem" in item["category"] and (item["reqLevel"] is not None and (level_minimum <= item["reqLevel"] <= level_maximum))]
    if table is item_table: memoize_cache[key] = result
    return result

def get_all_gems_by_required_level(level_minimum:int=0, level_maximum:int=100, table: Dict[int, ItemDict] = item_table) -> list[ItemDict]:
    return get_main_skill_gems_by_required_level(level_minimum, level_maximum, table) + \
           get_support_gems_by_required_level(level_minimum, level_maximum, table) + \
           get_utility_skill_gems_by_required_level(level_minimum, level_maximum, table)

def get_gear_items(table: Dict[int, ItemDict] = item_table) -> list[ItemDict]:
    if table is item_table and "Gear" in memoize_cache:
        return memoize_cache["Gear"]
    result = [item for item in table.values() if "Gear" in item["category"]]
    if table is item_table: memoize_cache["Gear"] = result
    return result

def get_armor_items(table: Dict[int, ItemDict] = item_table) -> list[ItemDict]:
    if table is item_table and "Armor" in memoize_cache:
        return memoize_cache["Armor"]
    result = [item for item in table.values() if "Armor" in item["category"]]
    if table is item_table: memoize_cache["Armor"] = result
    return result

def get_weapon_items(table: Dict[int, ItemDict] = item_table) -> list[ItemDict]:
    if table is item_table and "Weapon" in memoize_cache:
        return memoize_cache["Weapon"]
    result = [item for item in table.values() if "Weapon" in item["category"]]
    if table is item_table: memoize_cache["Weapon"] = result
    return result

def get_max_links_items(table: Dict[int, ItemDict] = item_table) -> list[ItemDict]:
    if table is item_table and "max links" in memoize_cache:
        return memoize_cache["max links"]
    result = [item for item in table.values() if "max links" in item["category"]]
    if table is item_table: memoize_cache["max links"] = result
    return result

def get_by_category(category: str, table: Dict[int, ItemDict] = item_table) -> list[ItemDict]:
    key = f"category_{category}"
    if table is item_table and key in memoize_cache:
        return memoize_cache[key]
    result = [item for item in table.values() if category in item["category"]]
    if table is item_table: memoize_cache[key] = result
    return result

def get_by_has_every_category(categories: Set[str], table: Dict[int, ItemDict] = item_table) -> list[ItemDict]:
    key = f"has_every_category_{'_'.join(sorted(categories))}"
    if table is item_table and key in memoize_cache:
        return memoize_cache[key]
    result = [item for item in table.values() if all(cat in item["category"] for cat in categories)]
    if table is item_table: memoize_cache[key] = result
    return result

def get_by_has_any_category(categories: Set[str], table: Dict[int, ItemDict] = item_table) -> list[ItemDict]:
    key = f"has_any_category_{'_'.join(sorted(categories))}"
    if table is item_table and key in memoize_cache:
        return memoize_cache[key]
    result = [item for item in table.values() if any(cat in item["category"] for cat in categories)]
    if table is item_table: memoize_cache[key] = result
    return result

def get_by_name(name: str, table: Dict[int, ItemDict] = item_table) -> ItemDict | None:
    return next((item for item in table.values() if item["name"] == name), None)

# used to check offhands

quiver_base_types = ItemTable.quiver_base_type_array.copy()  # Copy the list to avoid modifying the original data
shield_base_types = ItemTable.shield_base_type_array.copy() 

# used to check weapon base types
weapon_base_types = [
"Axe",
"Bow",
"Claw",
"Dagger",
"Mace",
"Sceptre",
"Staff",
"Sword",
"Wand",
"Fishing Rod",
]