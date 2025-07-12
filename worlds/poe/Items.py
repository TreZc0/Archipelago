from BaseClasses import Item, ItemClassification
from typing import TypedDict, Dict, Set 

class ItemDict(TypedDict, total=False): 
    classification: ItemClassification 
    count: int | None
    name: str 
    category: list[str]
    reqLevel: int | None

class PathOfExileItem(Item):
    """
    Represents an item in the Path of Exile world.
    This class can be extended to include specific item properties and methods.
    """
    game = "Path of Exile"
    category = list[str]()


#def get_items():
#    """
#    Returns a list of all items available in the Path of Exile world.
#    This function can be extended to include specific item definitions.
#    """
#    return items

def get_flask_items() -> Set[ItemDict]:
    """
    Returns a set of all flask items available in the Path of Exile world.
    """
    return {item for item in item_table.values() if "Flask" in item["category"]}

def get_character_class_items() -> Set[ItemDict]:
    """
    Returns a set of all character class items available in the Path of Exile world.
    """
    return {item for item in item_table.values() if "Character Class" in item["category"]}

def get_ascendancy_items() -> Set[ItemDict]:
    """
    Returns a set of all ascendancy items available in the Path of Exile world.
    """
    return {item for item in item_table.values() if "Ascendancy" in item["category"]}

def get_ascendancy_class_items(class_name: str) -> Set[ItemDict]:
    """
    Returns a set of all ascendancy items available for a specific class in the Path of Exile world.
    """
    return {item for item in item_table.values() if "Ascendancy" in item["category"] and class_name in item["category"]}

def get_main_skill_gem_items() -> Set[ItemDict]:
    """
    Returns a set of all main skill gem items available in the Path of Exile world.
    """
    return {item for item in item_table.values() if "MainSkillGem" in item["category"]}

def get_main_skill_gem_items_under_level(level: int) -> Set[ItemDict]:
    """
    Returns a set of all Main skill gem items available under a specific level in the Path of Exile world.
    """
    return {item for item in item_table.values() if "MainSkillGem" in item["category"] and (item["reqLevel"] is None or item["reqLevel"] < level)}

def get_gear_items() -> Set[ItemDict]:
    """
    Returns a set of all gear items available in the Path of Exile world.
    """
    return {item for item in item_table.values() if "Gear" in item["category"]}

def get_max_links_items() -> Set[ItemDict]:
    """
    Returns a set of all max links items available in the Path of Exile world.
    """
    return {item for item in item_table.values() if "max links" in item["category"]}

item_table: Dict[int, ItemDict] = {
   1: {
    "category": [
      "Flask",
      "Normal"
    ],
    "classification": ItemClassification.progression,
    "name": "Normal Flask in Slot 1"
  },
   2: {
    "category": [
      "Flask",
      "Normal"
    ],
    "classification": ItemClassification.progression,
    "name": "Normal Flask in Slot 2"
  },
   3: {
    "category": [
      "Flask",
      "Normal"
    ],
    "classification": ItemClassification.progression,
    "name": "Normal Flask in Slot 3"
  },
   4: {
    "category": [
      "Flask",
      "Normal"
    ],
    "classification": ItemClassification.progression,
    "name": "Normal Flask in Slot 4"
  },
   5: {
    "category": [
      "Flask",
      "Normal"
    ],
    "classification": ItemClassification.progression,
    "name": "Normal Flask in Slot 5"
  },
   6: {
    "category": [
      "Flask",
      "Magic"
    ],
    "classification": ItemClassification.progression,
    "name": "Magic Flask in Slot 1"
  },
   7: {
    "category": [
      "Flask",
      "Magic"
    ],
    "classification": ItemClassification.progression,
    "name": "Magic Flask in Slot 2"
  },
   8: {
    "category": [
      "Flask",
      "Magic"
    ],
    "classification": ItemClassification.progression,
    "name": "Magic Flask in Slot 3"
  },
   9: {
    "category": [
      "Flask",
      "Magic"
    ],
    "classification": ItemClassification.progression,
    "name": "Magic Flask in Slot 4"
  },
   10: {
    "category": [
      "Flask",
      "Magic"
    ],
    "classification": ItemClassification.progression,
    "name": "Magic Flask in Slot 5"
  },
   11: {
    "category": [
      "Character Class",
      "Base Class"
    ],
    "classification": ItemClassification.progression,
    "name": "Scion"
  },
   12: {
    "category": [
      "Character Class",
      "Base Class"
    ],
    "classification": ItemClassification.progression,
    "name": "Marauder"
  },
   13: {
    "category": [
      "Character Class",
      "Base Class"
    ],
    "classification": ItemClassification.progression,
    "name": "Duelist"
  },
   14: {
    "category": [
      "Character Class",
      "Base Class"
    ],
    "classification": ItemClassification.progression,
    "name": "Ranger"
  },
   15: {
    "category": [
      "Character Class",
      "Base Class"
    ],
    "classification": ItemClassification.progression,
    "name": "Shadow"
  },
   16: {
    "category": [
      "Character Class",
      "Base Class"
    ],
    "classification": ItemClassification.progression,
    "name": "Witch"
  },
   17: {
    "category": [
      "Character Class",
      "Base Class"
    ],
    "classification": ItemClassification.progression,
    "name": "Templar"
  },
   18: {
    "category": [
      "Character Class",
      "Ascendancy",
      "Scion Class"
    ],
    "classification": ItemClassification.progression,
    "name": "Ascendant"
  },
   19: {
    "category": [
      "Character Class",
      "Ascendancy",
      "Marauder Class"
    ],
    "classification": ItemClassification.progression,
    "name": "Berserker"
  },
   20: {
    "category": [
      "Character Class",
      "Ascendancy",
      "Marauder Class"
    ],
    "classification": ItemClassification.progression,
    "name": "Chieftain"
  },
   21: {
    "category": [
      "Character Class",
      "Ascendancy",
      "Marauder Class"
    ],
    "classification": ItemClassification.progression,
    "name": "Juggernaut"
  },
   22: {
    "category": [
      "Character Class",
      "Ascendancy",
      "Duelist Class"
    ],
    "classification": ItemClassification.progression,
    "name": "Champion"
  },
   23: {
    "category": [
      "Character Class",
      "Ascendancy",
      "Duelist Class"
    ],
    "classification": ItemClassification.progression,
    "name": "Gladiator"
  },
   24: {
    "category": [
      "Character Class",
      "Ascendancy",
      "Duelist Class"
    ],
    "classification": ItemClassification.progression,
    "name": "Slayer"
  },
   25: {
    "category": [
      "Character Class",
      "Ascendancy",
      "Ranger Class"
    ],
    "classification": ItemClassification.progression,
    "name": "Deadeye"
  },
   26: {
    "category": [
      "Character Class",
      "Ascendancy",
      "Ranger Class"
    ],
    "classification": ItemClassification.progression,
    "name": "Pathfinder"
  },
   27: {
    "category": [
      "Character Class",
      "Ascendancy",
      "Ranger Class"
    ],
    "classification": ItemClassification.progression,
    "name": "Warden"
  },
   28: {
    "category": [
      "Character Class",
      "Ascendancy",
      "Shadow Class"
    ],
    "classification": ItemClassification.progression,
    "name": "Assassin"
  },
   29: {
    "category": [
      "Character Class",
      "Ascendancy",
      "Shadow Class"
    ],
    "classification": ItemClassification.progression,
    "name": "Saboteur"
  },
   30: {
    "category": [
      "Character Class",
      "Ascendancy",
      "Shadow Class"
    ],
    "classification": ItemClassification.progression,
    "name": "Trickster"
  },
   31: {
    "category": [
      "Character Class",
      "Ascendancy",
      "Witch Class"
    ],
    "classification": ItemClassification.progression,
    "name": "Elementalist"
  },
   32: {
    "category": [
      "Character Class",
      "Ascendancy",
      "Witch Class"
    ],
    "classification": ItemClassification.progression,
    "name": "Necromancer"
  },
   33: {
    "category": [
      "Character Class",
      "Ascendancy",
      "Witch Class"
    ],
    "classification": ItemClassification.progression,
    "name": "Occultist"
  },
   34: {
    "category": [
      "Character Class",
      "Ascendancy",
      "Templar Class"
    ],
    "classification": ItemClassification.progression,
    "name": "Guardian"
  },
   35: {
    "category": [
      "Character Class",
      "Ascendancy",
      "Templar Class"
    ],
    "classification": ItemClassification.progression,
    "name": "Hierophant"
  },
   36: {
    "category": [
      "Character Class",
      "Ascendancy",
      "Templar Class"
    ],
    "classification": ItemClassification.progression,
    "name": "Inquisitor"
  },
   37: {
    "category": [
      "Gear",
      "Normal"
    ],
    "classification": ItemClassification.progression,
    "name": "Magic Axes"
  },
   38: {
    "category": [
      "Gear",
      "Normal"
    ],
    "classification": ItemClassification.progression,
    "name": "Magic Bows"
  },
   39: {
    "category": [
      "Gear",
      "Normal"
    ],
    "classification": ItemClassification.progression,
    "name": "Magic Claws"
  },
   40: {
    "category": [
      "Gear",
      "Normal"
    ],
    "classification": ItemClassification.progression,
    "name": "Magic Daggers"
  },
   41: {
    "category": [
      "Gear",
      "Normal"
    ],
    "classification": ItemClassification.progression,
    "name": "Magic Maces"
  },
   42: {
    "category": [
      "Gear",
      "Normal"
    ],
    "classification": ItemClassification.progression,
    "name": "Magic Sceptres"
  },
   43: {
    "category": [
      "Gear",
      "Normal"
    ],
    "classification": ItemClassification.progression,
    "name": "Magic Staves"
  },
   44: {
    "category": [
      "Gear",
      "Normal"
    ],
    "classification": ItemClassification.progression,
    "name": "Magic Swords"
  },
   45: {
    "category": [
      "Gear",
      "Normal"
    ],
    "classification": ItemClassification.progression,
    "name": "Magic Wands"
  },
   46: {
    "category": [
      "Gear",
      "Normal"
    ],
    "classification": ItemClassification.progression,
    "name": "Magic Body Armour"
  },
   47: {
    "category": [
      "Gear",
      "Normal"
    ],
    "classification": ItemClassification.progression,
    "name": "Magic Boots"
  },
   48: {
    "category": [
      "Gear",
      "Normal"
    ],
    "classification": ItemClassification.progression,
    "name": "Magic Gloves"
  },
   49: {
    "category": [
      "Gear",
      "Normal"
    ],
    "classification": ItemClassification.progression,
    "name": "Magic Helmet"
  },
   50: {
    "category": [
      "Gear",
      "Normal"
    ],
    "classification": ItemClassification.progression,
    "name": "Magic Amulet"
  },
   51: {
    "category": [
      "Gear",
      "Normal"
    ],
    "classification": ItemClassification.progression,
    "name": "Magic Belt"
  },
   52: {
    "category": [
      "Gear",
      "Normal"
    ],
    "classification": ItemClassification.progression,
    "name": "Magic Ring (left)"
  },
   53: {
    "category": [
      "Gear",
      "Normal"
    ],
    "classification": ItemClassification.progression,
    "name": "Magic Ring (right)"
  },
   54: {
    "category": [
      "Gear",
      "Normal"
    ],
    "classification": ItemClassification.progression,
    "name": "Magic Quiver"
  },
   55: {
    "category": [
      "Gear",
      "Normal"
    ],
    "classification": ItemClassification.progression,
    "name": "Magic Shield"
  },
   56: {
    "category": [
      "Gear",
      "Rare"
    ],
    "classification": ItemClassification.progression,
    "name": "Rare Axes"
  },
   57: {
    "category": [
      "Gear",
      "Rare"
    ],
    "classification": ItemClassification.progression,
    "name": "Rare Bows"
  },
   58: {
    "category": [
      "Gear",
      "Rare"
    ],
    "classification": ItemClassification.progression,
    "name": "Rare Claws"
  },
   59: {
    "category": [
      "Gear",
      "Rare"
    ],
    "classification": ItemClassification.progression,
    "name": "Rare Daggers"
  },
   60: {
    "category": [
      "Gear",
      "Rare"
    ],
    "classification": ItemClassification.progression,
    "name": "Rare Maces"
  },
   61: {
    "category": [
      "Gear",
      "Rare"
    ],
    "classification": ItemClassification.progression,
    "name": "Rare Sceptres"
  },
   62: {
    "category": [
      "Gear",
      "Rare"
    ],
    "classification": ItemClassification.progression,
    "name": "Rare Staves"
  },
   63: {
    "category": [
      "Gear",
      "Rare"
    ],
    "classification": ItemClassification.progression,
    "name": "Rare Swords"
  },
   64: {
    "category": [
      "Gear",
      "Rare"
    ],
    "classification": ItemClassification.progression,
    "name": "Rare Wands"
  },
   65: {
    "category": [
      "Gear",
      "Rare"
    ],
    "classification": ItemClassification.progression,
    "name": "Rare Body Armour"
  },
   66: {
    "category": [
      "Gear",
      "Rare"
    ],
    "classification": ItemClassification.progression,
    "name": "Rare Boots"
  },
   67: {
    "category": [
      "Gear",
      "Rare"
    ],
    "classification": ItemClassification.progression,
    "name": "Rare Gloves"
  },
   68: {
    "category": [
      "Gear",
      "Rare"
    ],
    "classification": ItemClassification.progression,
    "name": "Rare Helmet"
  },
   69: {
    "category": [
      "Gear",
      "Rare"
    ],
    "classification": ItemClassification.progression,
    "name": "Rare Amulet"
  },
   70: {
    "category": [
      "Gear",
      "Rare"
    ],
    "classification": ItemClassification.progression,
    "name": "Rare Belt"
  },
   71: {
    "category": [
      "Gear",
      "Rare"
    ],
    "classification": ItemClassification.progression,
    "name": "Rare Ring (left)"
  },
   72: {
    "category": [
      "Gear",
      "Rare"
    ],
    "classification": ItemClassification.progression,
    "name": "Rare Ring (right)"
  },
   73: {
    "category": [
      "Gear",
      "Rare"
    ],
    "classification": ItemClassification.progression,
    "name": "Rare Quiver"
  },
   74: {
    "category": [
      "Gear",
      "Rare"
    ],
    "classification": ItemClassification.progression,
    "name": "Rare Shield"
  },
   75: {
    "category": [
      "Gear",
      "Unique"
    ],
    "classification": ItemClassification.progression,
    "name": "Unique Axes"
  },
   76: {
    "category": [
      "Gear",
      "Unique"
    ],
    "classification": ItemClassification.progression,
    "name": "Unique Bows"
  },
   77: {
    "category": [
      "Gear",
      "Unique"
    ],
    "classification": ItemClassification.progression,
    "name": "Unique Claws"
  },
   78: {
    "category": [
      "Gear",
      "Unique"
    ],
    "classification": ItemClassification.progression,
    "name": "Unique Daggers"
  },
   79: {
    "category": [
      "Gear",
      "Unique"
    ],
    "classification": ItemClassification.progression,
    "name": "Unique Maces"
  },
   80: {
    "category": [
      "Gear",
      "Unique"
    ],
    "classification": ItemClassification.progression,
    "name": "Unique Sceptres"
  },
   81: {
    "category": [
      "Gear",
      "Unique"
    ],
    "classification": ItemClassification.progression,
    "name": "Unique Staves"
  },
   82: {
    "category": [
      "Gear",
      "Unique"
    ],
    "classification": ItemClassification.progression,
    "name": "Unique Swords"
  },
   83: {
    "category": [
      "Gear",
      "Unique"
    ],
    "classification": ItemClassification.progression,
    "name": "Unique Wands"
  },
   84: {
    "category": [
      "Gear",
      "Unique"
    ],
    "classification": ItemClassification.progression,
    "name": "Unique Body Armour"
  },
   85: {
    "category": [
      "Gear",
      "Unique"
    ],
    "classification": ItemClassification.progression,
    "name": "Unique Boots"
  },
   86: {
    "category": [
      "Gear",
      "Unique"
    ],
    "classification": ItemClassification.progression,
    "name": "Unique Gloves"
  },
   87: {
    "category": [
      "Gear",
      "Unique"
    ],
    "classification": ItemClassification.progression,
    "name": "Unique Helmet"
  },
   88: {
    "category": [
      "Gear",
      "Unique"
    ],
    "classification": ItemClassification.progression,
    "name": "Unique Amulet"
  },
   89: {
    "category": [
      "Gear",
      "Unique"
    ],
    "classification": ItemClassification.progression,
    "name": "Unique Belt"
  },
   90: {
    "category": [
      "Gear",
      "Unique"
    ],
    "classification": ItemClassification.progression,
    "name": "Unique Ring (left)"
  },
   91: {
    "category": [
      "Gear",
      "Unique"
    ],
    "classification": ItemClassification.progression,
    "name": "Unique Ring (right)"
  },
   92: {
    "category": [
      "Gear",
      "Unique"
    ],
    "classification": ItemClassification.progression,
    "name": "Unique Quiver"
  },
   93: {
    "category": [
      "Gear",
      "Unique"
    ],
    "classification": ItemClassification.progression,
    "name": "Unique Shield"
  },
   94: {
    "category": [
      "max links"
    ],
    "classification": ItemClassification.progression,
    "name": "Progressive max links - Helm",
    "count": 3,
  },
   95: {
    "category": [
      "max links"
    ],
    "classification": ItemClassification.progression,
    "name": "Progressive max links - Glove",
    "count": 3,
  },
   96: {
    "category": [
      "max links"
    ],
    "classification": ItemClassification.progression,
    "name": "Progressive max links - Boot",
    "count": 3,
  },
   97: {
    "category": [
      "max links"
    ],
    "classification": ItemClassification.progression,
    "name": "Progressive max links - Body",
    "count": 5,
  },
   98: {
    "category": [
      "max links"
    ],
    "classification": ItemClassification.progression,
    "name": "Progressive max links - Weapon",
    "count": 5,
  },
   99: {
    "category": [
      "max links"
    ],
    "classification": ItemClassification.progression,
    "name": "Progressive max links - Offhand",
    "count": 3,
  },
   100: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Focused Channelling Support"
  },
   101: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.progression,
    "name": "Crushing Fist"
  },
   102: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.useful,
    "name": "Vengeful Cry"
  },
   103: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 6,
    "classification": ItemClassification.progression,
    "name": "Eviscerate"
  },
   104: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 6,
    "classification": ItemClassification.progression,
    "name": "Swordstorm"
  },
   105: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 6,
    "classification": ItemClassification.progression,
    "name": "Glacial Shield Swipe"
  },
   106: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 6,
    "classification": ItemClassification.progression,
    "name": "Divine Retribution"
  },
   107: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Overexertion Support"
  },
   108: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Expert Retaliation Support"
  },
   109: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Rupture Support"
  },
   110: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.progression,
    "name": "Animate Weapon"
  },
   111: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Artillery Ballista"
  },
   112: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Barrage"
  },
   113: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.progression,
    "name": "Bear Trap"
  },
   114: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 16,
    "classification": ItemClassification.progression,
    "name": "Blade Blast"
  },
   115: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Blade Flurry"
  },
   116: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Blade Trap"
  },
   117: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Blade Vortex"
  },
   118: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Bladefall"
  },
   119: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Blast Rain"
  },
   120: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.progression,
    "name": "Burning Arrow"
  },
   121: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.progression,
    "name": "Caustic Arrow"
  },
   122: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Charged Dash"
  },
   123: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.progression,
    "name": "Cobra Lash"
  },
   124: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Cremation"
  },
   125: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Cyclone"
  },
   126: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.progression,
    "name": "Detonate Dead"
  },
   127: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.progression,
    "name": "Double Strike"
  },
   128: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.progression,
    "name": "Dual Strike"
  },
   129: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Elemental Hit"
  },
   130: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 16,
    "classification": ItemClassification.progression,
    "name": "Ensnaring Arrow"
  },
   131: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.progression,
    "name": "Ethereal Knives"
  },
   132: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Explosive Arrow"
  },
   133: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Explosive Concoction"
  },
   134: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.progression,
    "name": "Explosive Trap"
  },
   135: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Fire Trap"
  },
   136: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Flamethrower Trap"
  },
   137: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 10,
    "classification": ItemClassification.progression,
    "name": "Flicker Strike"
  },
   138: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 16,
    "classification": ItemClassification.progression,
    "name": "Frenzy"
  },
   139: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.progression,
    "name": "Frost Blades"
  },
   140: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.progression,
    "name": "Galvanic Arrow"
  },
   141: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.progression,
    "name": "Ice Shot"
  },
   142: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Ice Trap"
  },
   143: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Lacerate"
  },
   144: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Lancing Steel"
  },
   145: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Lightning Arrow"
  },
   146: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Lightning Strike"
  },
   147: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Pestilent Strike"
  },
   148: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Poisonous Concoction"
  },
   149: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.progression,
    "name": "Puncture"
  },
   150: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Rain of Arrows"
  },
   151: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Reave"
  },
   152: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Scourge Arrow"
  },
   153: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Seismic Trap"
  },
   154: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Shattering Steel"
  },
   155: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.progression,
    "name": "Shrapnel Ballista"
  },
   156: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Siege Ballista"
  },
   157: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 34,
    "classification": ItemClassification.progression,
    "name": "Snipe"
  },
   158: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Spectral Helix"
  },
   159: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Spectral Shield Throw"
  },
   160: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.progression,
    "name": "Spectral Throw"
  },
   161: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.progression,
    "name": "Split Arrow"
  },
   162: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.progression,
    "name": "Splitting Steel"
  },
   163: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Storm Rain"
  },
   164: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 34,
    "classification": ItemClassification.progression,
    "name": "Tornado"
  },
   165: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Tornado Shot"
  },
   166: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Toxic Rain"
  },
   167: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 10,
    "classification": ItemClassification.progression,
    "name": "Unearth"
  },
   168: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Venom Gyre"
  },
   169: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.progression,
    "name": "Viper Strike"
  },
   170: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Volatile Dead"
  },
   171: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 10,
    "classification": ItemClassification.progression,
    "name": "Whirling Blades"
  },
   172: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Wild Strike"
  },
   173: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Arc"
  },
   174: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.progression,
    "name": "Arcanist Brand"
  },
   175: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Armageddon Brand"
  },
   176: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Ball Lightning"
  },
   177: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.progression,
    "name": "Bane"
  },
   178: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Blazing Salvo"
  },
   179: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.progression,
    "name": "Blight"
  },
   180: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 10,
    "classification": ItemClassification.progression,
    "name": "Bodyswap"
  },
   181: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Bone Offering"
  },
   182: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 16,
    "classification": ItemClassification.progression,
    "name": "Cold Snap"
  },
   183: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.progression,
    "name": "Contagion"
  },
   184: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.progression,
    "name": "Conversion Trap"
  },
   185: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Crackling Lance"
  },
   186: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Creeping Frost"
  },
   187: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Divine Ire"
  },
   188: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.progression,
    "name": "Energy Blade"
  },
   189: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Essence Drain"
  },
   190: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Eye of Winter"
  },
   191: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.progression,
    "name": "Fireball"
  },
   192: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Firestorm"
  },
   193: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Flame Surge"
  },
   194: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.progression,
    "name": "Flame Wall"
  },
   195: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Flameblast"
  },
   196: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 16,
    "classification": ItemClassification.progression,
    "name": "Forbidden Rite"
  },
   197: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.progression,
    "name": "Freezing Pulse"
  },
   198: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.progression,
    "name": "Frost Bomb"
  },
   199: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.progression,
    "name": "Frostbolt"
  },
   200: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 16,
    "classification": ItemClassification.progression,
    "name": "Galvanic Field"
  },
   201: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Glacial Cascade"
  },
   202: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 34,
    "classification": ItemClassification.progression,
    "name": "Hydrosphere"
  },
   203: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Ice Nova"
  },
   204: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Ice Spear"
  },
   205: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Icicle Mine"
  },
   206: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Incinerate"
  },
   207: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Kinetic Blast"
  },
   208: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.progression,
    "name": "Kinetic Bolt"
  },
   209: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Lightning Conduit"
  },
   210: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Lightning Spire Trap"
  },
   211: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.progression,
    "name": "Lightning Tendrils"
  },
   212: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Lightning Trap"
  },
   213: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Manabond"
  },
   214: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.progression,
    "name": "Orb of Storms"
  },
   215: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Penance Brand"
  },
   216: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Power Siphon"
  },
   217: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.progression,
    "name": "Purifying Flame"
  },
   218: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Pyroclast Mine"
  },
   219: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Raise Spectre"
  },
   220: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.progression,
    "name": "Raise Zombie"
  },
   221: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 16,
    "classification": ItemClassification.progression,
    "name": "Righteous Fire"
  },
   222: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.progression,
    "name": "Rolling Magma"
  },
   223: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Scorching Ray"
  },
   224: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Shock Nova"
  },
   225: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Soulrend"
  },
   226: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.progression,
    "name": "Spark"
  },
   227: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.progression,
    "name": "Spellslinger"
  },
   228: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Storm Brand"
  },
   229: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Storm Burst"
  },
   230: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Storm Call"
  },
   231: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Stormbind"
  },
   232: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.progression,
    "name": "Stormblast Mine"
  },
   233: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 34,
    "classification": ItemClassification.progression,
    "name": "Summon Carrion Golem"
  },
   234: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 34,
    "classification": ItemClassification.progression,
    "name": "Summon Chaos Golem"
  },
   235: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 34,
    "classification": ItemClassification.progression,
    "name": "Summon Lightning Golem"
  },
   236: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.progression,
    "name": "Summon Raging Spirit"
  },
   237: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Summon Reaper"
  },
   238: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 10,
    "classification": ItemClassification.progression,
    "name": "Summon Skeletons"
  },
   239: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 16,
    "classification": ItemClassification.progression,
    "name": "Summon Skitterbots"
  },
   240: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 34,
    "classification": ItemClassification.progression,
    "name": "Void Sphere"
  },
   241: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Voltaxic Burst"
  },
   242: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Vortex"
  },
   243: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 16,
    "classification": ItemClassification.progression,
    "name": "Wave of Conviction"
  },
   244: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Winter Orb"
  },
   245: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Wintertide Brand"
  },
   246: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Absolution"
  },
   247: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.progression,
    "name": "Ancestral Protector"
  },
   248: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Ancestral Warchief"
  },
   249: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Animate Guardian"
  },
   250: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Bladestorm"
  },
   251: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Boneshatter"
  },
   252: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Chain Hook"
  },
   253: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.progression,
    "name": "Cleave"
  },
   254: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Consecrated Path"
  },
   255: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Dominating Blow"
  },
   256: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Earthquake"
  },
   257: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Earthshatter"
  },
   258: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Exsanguinate"
  },
   259: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 34,
    "classification": ItemClassification.progression,
    "name": "Frozen Legion"
  },
   260: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.progression,
    "name": "Glacial Hammer"
  },
   261: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.progression,
    "name": "Ground Slam"
  },
   262: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.progression,
    "name": "Heavy Strike"
  },
   263: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.progression,
    "name": "Holy Flame Totem"
  },
   264: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Ice Crash"
  },
   265: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Infernal Blow"
  },
   266: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.progression,
    "name": "Infernal Cry"
  },
   267: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.progression,
    "name": "Molten Strike"
  },
   268: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.progression,
    "name": "Perforate"
  },
   269: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Rage Vortex"
  },
   270: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Reap"
  },
   271: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Searing Bond"
  },
   272: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.progression,
    "name": "Shield Crush"
  },
   273: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Shockwave Totem"
  },
   274: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.progression,
    "name": "Smite"
  },
   275: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Static Strike"
  },
   276: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 34,
    "classification": ItemClassification.progression,
    "name": "Summon Flame Golem"
  },
   277: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 34,
    "classification": ItemClassification.progression,
    "name": "Summon Stone Golem"
  },
   278: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Sunder"
  },
   279: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Sweep"
  },
   280: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.progression,
    "name": "Tectonic Slam"
  },
   281: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.progression,
    "name": "Vengeance"
  },
   282: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.progression,
    "name": "Vigilant Strike"
  },
   283: {
    "category": [
      "MainSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.progression,
    "name": "Volcanic Fissure"
  },
   284: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.useful,
    "name": "Alchemist's Mark"
  },
   285: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 34,
    "classification": ItemClassification.useful,
    "name": "Ambush"
  },
   286: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.useful,
    "name": "Autoexertion"
  },
   287: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.useful,
    "name": "Automation"
  },
   288: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 16,
    "classification": ItemClassification.useful,
    "name": "Arctic Armour"
  },
   289: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 10,
    "classification": ItemClassification.useful,
    "name": "Blink Arrow"
  },
   290: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 16,
    "classification": ItemClassification.useful,
    "name": "Blood Rage"
  },
   291: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.useful,
    "name": "Dash"
  },
   292: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 16,
    "classification": ItemClassification.useful,
    "name": "Desecrate"
  },
   293: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.useful,
    "name": "Grace"
  },
   294: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.useful,
    "name": "Haste"
  },
   295: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.useful,
    "name": "Hatred"
  },
   296: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 16,
    "classification": ItemClassification.useful,
    "name": "Herald of Agony"
  },
   297: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 16,
    "classification": ItemClassification.useful,
    "name": "Herald of Ice"
  },
   298: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 34,
    "classification": ItemClassification.filler,
    "name": "Intuitive Link"
  },
   299: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 10,
    "classification": ItemClassification.useful,
    "name": "Mirror Arrow"
  },
   300: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 34,
    "classification": ItemClassification.useful,
    "name": "Phase Run"
  },
   301: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.useful,
    "name": "Plague Bearer"
  },
   302: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 16,
    "classification": ItemClassification.useful,
    "name": "Poacher's Mark"
  },
   303: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 10,
    "classification": ItemClassification.useful,
    "name": "Precision"
  },
   304: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.useful,
    "name": "Purity of Ice"
  },
   305: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.useful,
    "name": "Riposte"
  },
   306: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 10,
    "classification": ItemClassification.useful,
    "name": "Smoke Mine"
  },
   307: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.useful,
    "name": "Sniper's Mark"
  },
   308: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 34,
    "classification": ItemClassification.useful,
    "name": "Summon Ice Golem"
  },
   309: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.useful,
    "name": "Temporal Chains"
  },
   310: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 34,
    "classification": ItemClassification.useful,
    "name": "Temporal Rift"
  },
   311: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 34,
    "classification": ItemClassification.filler,
    "name": "Vampiric Link"
  },
   312: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 10,
    "classification": ItemClassification.useful,
    "name": "Withering Step"
  },
   313: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 16,
    "classification": ItemClassification.useful,
    "name": "Arcane Cloak"
  },
   314: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 16,
    "classification": ItemClassification.useful,
    "name": "Assassin's Mark"
  },
   315: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 16,
    "classification": ItemClassification.useful,
    "name": "Brand Recall"
  },
   316: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 10,
    "classification": ItemClassification.useful,
    "name": "Clarity"
  },
   317: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.useful,
    "name": "Conductivity"
  },
   318: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.useful,
    "name": "Convocation"
  },
   319: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.useful,
    "name": "Dark Pact"
  },
   320: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.useful,
    "name": "Despair"
  },
   321: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 34,
    "classification": ItemClassification.filler,
    "name": "Destructive Link"
  },
   322: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.useful,
    "name": "Discharge"
  },
   323: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.useful,
    "name": "Discipline"
  },
   324: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.useful,
    "name": "Elemental Weakness"
  },
   325: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.useful,
    "name": "Enfeeble"
  },
   326: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 10,
    "classification": ItemClassification.useful,
    "name": "Flame Dash"
  },
   327: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.useful,
    "name": "Flammability"
  },
   328: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.useful,
    "name": "Flesh Offering"
  },
   329: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 34,
    "classification": ItemClassification.useful,
    "name": "Frost Shield"
  },
   330: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.useful,
    "name": "Frost Wall"
  },
   331: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.useful,
    "name": "Frostbite"
  },
   332: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.useful,
    "name": "Frostblink"
  },
   333: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 16,
    "classification": ItemClassification.useful,
    "name": "Herald of Thunder"
  },
   334: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 28,
    "classification": ItemClassification.useful,
    "name": "Hexblast"
  },
   335: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 10,
    "classification": ItemClassification.useful,
    "name": "Lightning Warp"
  },
   336: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.useful,
    "name": "Malevolence"
  },
   337: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.useful,
    "name": "Purity of Elements"
  },
   338: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.useful,
    "name": "Purity of Lightning"
  },
   339: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 34,
    "classification": ItemClassification.useful,
    "name": "Sigil of Power"
  },
   340: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 10,
    "classification": ItemClassification.useful,
    "name": "Siphoning Trap"
  },
   341: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 34,
    "classification": ItemClassification.filler,
    "name": "Soul Link"
  },
   342: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 12,
    "classification": ItemClassification.useful,
    "name": "Spirit Offering"
  },
   343: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.useful,
    "name": "Summon Holy Relic"
  },
   344: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 16,
    "classification": ItemClassification.useful,
    "name": "Tempest Shield"
  },
   345: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.useful,
    "name": "Wrath"
  },
   346: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.useful,
    "name": "Zealotry"
  },
   347: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 8,
    "classification": ItemClassification.useful,
    "name": "Detonate Mines"
  },
   348: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 10,
    "classification": ItemClassification.useful,
    "name": "Portal"
  },
   349: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 16,
    "classification": ItemClassification.useful,
    "name": "Ancestral Cry"
  },
   350: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.useful,
    "name": "Anger"
  },
   351: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.useful,
    "name": "Battlemage's Cry"
  },
   352: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 34,
    "classification": ItemClassification.useful,
    "name": "Berserk"
  },
   353: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.useful,
    "name": "Blood and Sand"
  },
   354: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 16,
    "classification": ItemClassification.useful,
    "name": "Corrupting Fever"
  },
   355: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.useful,
    "name": "Decoy Totem"
  },
   356: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 16,
    "classification": ItemClassification.useful,
    "name": "Defiance Banner"
  },
   357: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.useful,
    "name": "Determination"
  },
   358: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.useful,
    "name": "Devouring Totem"
  },
   359: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.useful,
    "name": "Dread Banner"
  },
   360: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 10,
    "classification": ItemClassification.useful,
    "name": "Enduring Cry"
  },
   361: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 34,
    "classification": ItemClassification.filler,
    "name": "Flame Link"
  },
   362: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 16,
    "classification": ItemClassification.useful,
    "name": "Flesh and Stone"
  },
   363: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.useful,
    "name": "General's Cry"
  },
   364: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 16,
    "classification": ItemClassification.useful,
    "name": "Herald of Ash"
  },
   365: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 16,
    "classification": ItemClassification.useful,
    "name": "Herald of Purity"
  },
   366: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 34,
    "classification": ItemClassification.useful,
    "name": "Immortal Call"
  },
   367: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 10,
    "classification": ItemClassification.useful,
    "name": "Intimidating Cry"
  },
   368: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 10,
    "classification": ItemClassification.useful,
    "name": "Leap Slam"
  },
   369: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.useful,
    "name": "Molten Shell"
  },
   370: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.useful,
    "name": "Petrified Blood"
  },
   371: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.useful,
    "name": "Pride"
  },
   372: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 34,
    "classification": ItemClassification.filler,
    "name": "Protective Link"
  },
   373: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.useful,
    "name": "Punishment"
  },
   374: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.useful,
    "name": "Purity of Fire"
  },
   375: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.useful,
    "name": "Rallying Cry"
  },
   376: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.useful,
    "name": "Reckoning"
  },
   377: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.useful,
    "name": "Rejuvenation Totem"
  },
   378: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 16,
    "classification": ItemClassification.useful,
    "name": "Seismic Cry"
  },
   379: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 10,
    "classification": ItemClassification.useful,
    "name": "Shield Charge"
  },
   380: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.useful,
    "name": "Steelskin"
  },
   381: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 10,
    "classification": ItemClassification.useful,
    "name": "Vitality"
  },
   382: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 24,
    "classification": ItemClassification.useful,
    "name": "Vulnerability"
  },
   383: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.useful,
    "name": "War Banner"
  },
   384: {
    "category": [
      "UtilSkillGem"
    ],
    "reqLevel": 16,
    "classification": ItemClassification.useful,
    "name": "Warlord's Mark"
  },
   385: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.useful,
    "name": "Chance to Bleed Support"
  },
#   386: {
#    "category": [
#      "SupportGem"
#    ],
#    "reqLevel": 1,
#    "classification": ItemClassification.useful,
#    "name": "Empower Support"
#  },
   387: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.useful,
    "name": "Ruthless Support"
  },
   388: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.useful,
    "name": "Ancestral Call Support"
  },
   389: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 8,
    "classification": ItemClassification.useful,
    "name": "Added Fire Damage Support"
  },
   390: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 8,
    "classification": ItemClassification.useful,
    "name": "Ballista Totem Support"
  },
   391: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 8,
    "classification": ItemClassification.useful,
    "name": "Earthbreaker Support"
  },
   392: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 8,
    "classification": ItemClassification.useful,
    "name": "Flamewood Support"
  },
   393: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 8,
    "classification": ItemClassification.useful,
    "name": "Knockback Support"
  },
   394: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 8,
    "classification": ItemClassification.useful,
    "name": "Life Gain on Hit Support"
  },
   395: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 8,
    "classification": ItemClassification.useful,
    "name": "Lifetap Support"
  },
   396: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 8,
    "classification": ItemClassification.useful,
    "name": "Maim Support"
  },
   397: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 8,
    "classification": ItemClassification.useful,
    "name": "Melee Splash Support"
  },
   398: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 8,
    "classification": ItemClassification.useful,
    "name": "Spell Totem Support"
  },
   399: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 8,
    "classification": ItemClassification.useful,
    "name": "Stun Support"
  },
   400: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.useful,
    "name": "Bloodlust Support"
  },
   401: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.useful,
    "name": "Cold to Fire Support"
  },
   402: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.useful,
    "name": "Cruelty Support"
  },
   403: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.useful,
    "name": "Damage on Full Life Support"
  },
   404: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.useful,
    "name": "Elemental Damage with Attacks Support"
  },
   405: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.filler,
    "name": "Endurance Charge on Melee Stun Support"
  },
   406: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.useful,
    "name": "Iron Grip Support"
  },
   407: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.useful,
    "name": "Iron Will Support"
  },
   408: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.useful,
    "name": "Melee Physical Damage Support"
  },
   409: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.useful,
    "name": "Rage Support"
  },
   410: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.useful,
    "name": "Sacred Wisps Support"
  },
   411: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.useful,
    "name": "Shockwave Support"
  },
   412: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.useful,
    "name": "Volatility Support"
  },
   413: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Arrogance Support"
  },
   414: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Bloodthirst Support"
  },
   415: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Burning Damage Support"
  },
   416: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Controlled Blaze Support"
  },
   417: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Corrupting Cry Support"
  },
   418: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Divine Blessing Support"
  },
   419: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Fire Penetration Support"
  },
   420: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Fortify Support"
  },
   421: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.filler,
    "name": "Generosity Support"
  },
   422: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Guardian's Blessing Support"
  },
   423: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Increased Duration Support"
  },
   424: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Inspiration Support"
  },
   425: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Less Duration Support"
  },
   426: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Life Leech Support"
  },
   427: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Pulverise Support"
  },
   428: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Urgent Orders Support"
  },
   429: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Behead Support"
  },
   430: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Brutality Support"
  },
   431: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.filler,
    "name": "Cast on Melee Kill Support"
  },
   432: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Cast when Damage Taken Support"
  },
   433: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Eternal Blessing Support"
  },
   434: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Fist of War Support"
  },
   435: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Multiple Totems Support"
  },
   436: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Multistrike Support"
  },
   437: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Trauma Support"
  },
   438: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.useful,
    "name": "Chance to Poison Support"
  },
#   439: {
#    "category": [
#      "SupportGem"
#    ],
#    "reqLevel": 1,
#    "classification": ItemClassification.useful,
#    "name": "Enhance Support"
#  },
   440: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.useful,
    "name": "Momentum Support"
  },
   441: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.useful,
    "name": "Mirage Archer Support"
  },
   442: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.useful,
    "name": "Pierce Support"
  },
   443: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.useful,
    "name": "Swift Assembly Support"
  },
   444: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.filler,
    "name": "Volley Support"
  },
   445: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 8,
    "classification": ItemClassification.useful,
    "name": "Added Cold Damage Support"
  },
   446: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 8,
    "classification": ItemClassification.useful,
    "name": "Additional Accuracy Support"
  },
   447: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 8,
    "classification": ItemClassification.useful,
    "name": "Arrow Nova Support"
  },
   448: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 8,
    "classification": ItemClassification.useful,
    "name": "Blind Support"
  },
   449: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 8,
    "classification": ItemClassification.filler,
    "name": "Chance to Flee Support"
  },
   450: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 8,
    "classification": ItemClassification.useful,
    "name": "Faster Attacks Support"
  },
   451: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 8,
    "classification": ItemClassification.filler,
    "name": "Lesser Multiple Projectiles Support"
  },
   452: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 8,
    "classification": ItemClassification.useful,
    "name": "Locus Mine Support"
  },
   453: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 8,
    "classification": ItemClassification.useful,
    "name": "Manaforged Arrows Support"
  },
   454: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 8,
    "classification": ItemClassification.useful,
    "name": "Multiple Traps Support"
  },
   455: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 8,
    "classification": ItemClassification.useful,
    "name": "Trap Support"
  },
   456: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 8,
    "classification": ItemClassification.useful,
    "name": "Void Manipulation Support"
  },
   457: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.useful,
    "name": "Block Chance Reduction Support"
  },
   458: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.useful,
    "name": "Close Combat Support"
  },
   459: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.useful,
    "name": "Culling Strike Support"
  },
   460: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.useful,
    "name": "Deadly Ailments Support"
  },
   461: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.useful,
    "name": "Nightblade Support"
  },
   462: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.useful,
    "name": "Point Blank Support"
  },
   463: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.useful,
    "name": "Sadism Support"
  },
   464: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.useful,
    "name": "Trap and Mine Damage Support"
  },
   465: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.useful,
    "name": "Vicious Projectiles Support"
  },
   466: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Advanced Traps Support"
  },
   467: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Charged Traps Support"
  },
   468: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Cold Penetration Support"
  },
   469: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Critical Strike Affliction Support"
  },
   470: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Faster Projectiles Support"
  },
   471: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Focused Ballista Support"
  },
   472: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Fork Support"
  },
   473: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Hypothermia Support"
  },
   474: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Ice Bite Support"
  },
   475: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Impale Support"
  },
   476: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Mana Leech Support"
  },
   477: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Second Wind Support"
  },
   478: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Slower Projectiles Support"
  },
   479: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Swift Affliction Support"
  },
   480: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Barrage Support"
  },
   481: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Cast On Critical Strike Support"
  },
   482: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Cast on Death Support"
  },
   483: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Chain Support"
  },
   484: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Cluster Traps Support"
  },
   485: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Greater Multiple Projectiles Support"
  },
   486: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Greater Volley Support"
  },
   487: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Mark On Hit Support"
  },
   488: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Returning Projectiles Support"
  },
   489: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Vile Toxins Support"
  },
   490: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Withering Touch Support"
  },
   491: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Added Chaos Damage Support"
  },
   492: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 8,
    "classification": ItemClassification.useful,
    "name": "Added Lightning Damage Support"
  },
   493: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.useful,
    "name": "Arcane Surge Support"
  },
   494: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Archmage Support"
  },
   495: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Blasphemy Support"
  },
   496: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 8,
    "classification": ItemClassification.useful,
    "name": "Blastchain Mine Support"
  },
   497: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Bonechill Support"
  },
   498: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Cast when Stunned Support"
  },
   499: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Cast while Channelling Support"
  },
   500: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Charged Mines Support"
  },
   501: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 8,
    "classification": ItemClassification.useful,
    "name": "Combustion Support"
  },
   502: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.useful,
    "name": "Concentrated Effect Support"
  },
   503: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.useful,
    "name": "Controlled Destruction Support"
  },
   504: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Cursed Ground Support"
  },
   505: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Decay Support"
  },
   506: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 8,
    "classification": ItemClassification.useful,
    "name": "Devour Support"
  },
   507: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 8,
    "classification": ItemClassification.useful,
    "name": "Efficacy Support"
  },
   508: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Elemental Army Support"
  },
   509: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.useful,
    "name": "Elemental Focus Support"
  },
   510: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Elemental Penetration Support"
  },
   511: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.useful,
    "name": "Elemental Proliferation Support"
  },
   512: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Energy Leech Support"
  },
#   513: {
#    "category": [
#      "SupportGem"
#    ],
#    "reqLevel": 1,
#    "classification": ItemClassification.useful,
#    "name": "Enlighten Support"
#  },
   514: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.useful,
    "name": "Faster Casting Support"
  },
   515: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Feeding Frenzy Support"
  },
   516: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.useful,
    "name": "Fresh Meat Support"
  },
   517: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Frigid Bond Support"
  },
   518: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Hex Bloom Support"
  },
   519: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Hextouch Support"
  },
   520: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "High-Impact Mine Support"
  },
   521: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Ignite Proliferation Support"
  },
   522: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Immolate Support"
  },
   523: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Impending Doom Support"
  },
   524: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Increased Area of Effect Support"
  },
   525: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.useful,
    "name": "Increased Critical Damage Support"
  },
   526: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 8,
    "classification": ItemClassification.useful,
    "name": "Increased Critical Strikes Support"
  },
   527: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 8,
    "classification": ItemClassification.useful,
    "name": "Infernal Legion Support"
  },
   528: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.useful,
    "name": "Infused Channelling Support"
  },
   529: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Innervate Support"
  },
   530: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Intensify Support"
  },
   531: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Item Rarity Support"
  },
   532: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Lightning Penetration Support"
  },
   533: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Meat Shield Support"
  },
   534: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Minefield Support"
  },
   535: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 8,
    "classification": ItemClassification.useful,
    "name": "Minion Damage Support"
  },
   536: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.useful,
    "name": "Minion Life Support"
  },
   537: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.useful,
    "name": "Minion Speed Support"
  },
   538: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.useful,
    "name": "Overcharge Support"
  },
   539: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.useful,
    "name": "Physical to Lightning Support"
  },
   540: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Pinpoint Support"
  },
   541: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.useful,
    "name": "Power Charge On Critical Support"
  },
   542: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.useful,
    "name": "Predator Support"
  },
   543: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 1,
    "classification": ItemClassification.useful,
    "name": "Prismatic Burst Support"
  },
   544: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Sacrifice Support"
  },
   545: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.useful,
    "name": "Spell Cascade Support"
  },
   546: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Spell Echo Support"
  },
   547: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Spellblade Support"
  },
   548: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 4,
    "classification": ItemClassification.useful,
    "name": "Summon Phantasm Support"
  },
   549: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 31,
    "classification": ItemClassification.useful,
    "name": "Swiftbrand Support"
  },
   550: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 18,
    "classification": ItemClassification.useful,
    "name": "Trinity Support"
  },
   551: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 8,
    "classification": ItemClassification.useful,
    "name": "Unbound Ailments Support"
  },
   552: {
    "category": [
      "SupportGem"
    ],
    "reqLevel": 38,
    "classification": ItemClassification.useful,
    "name": "Unleash Support"
  }
}