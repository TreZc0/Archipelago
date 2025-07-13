from typing import Dict, TypedDict
from BaseClasses import Location


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
base_item_types: Dict[int, LocationDict] = {
  0:{
    "baseItem": "Plate Vest",
    "dropLevel": 1,
    "act": 1
  },
  1:{
    "baseItem": "Iron Greaves",
    "dropLevel": 1,
    "act": 1
  },
  2:{
    "baseItem": "Crude Bow",
    "dropLevel": 1,
    "act": 1
  },
  3:{
    "baseItem": "Glass Shank",
    "dropLevel": 1,
    "act": 1
  },
  4:{
    "baseItem": "Iron Gauntlets",
    "dropLevel": 1,
    "act": 1
  },
  5:{
    "baseItem": "Iron Hat",
    "dropLevel": 1,
    "act": 1
  },
  6:{
    "baseItem": "Small Life Flask",
    "dropLevel": 1,
    "act": 1
  },
  7:{
    "baseItem": "Small Mana Flask",
    "dropLevel": 1,
    "act": 1
  },
  8:{
    "baseItem": "Driftwood Club",
    "dropLevel": 1,
    "act": 1
  },
  9:{
    "baseItem": "Rusted Sword",
    "dropLevel": 1,
    "act": 1
  },
  10:{
    "baseItem": "Driftwood Sceptre",
    "dropLevel": 1,
    "act": 1
  },
  11:{
    "baseItem": "Splintered Tower Shield",
    "dropLevel": 1,
    "act": 1
  },
  12:{
    "baseItem": "Driftwood Wand",
    "dropLevel": 1,
    "act": 1
  },
  13:{
    "baseItem": "Chain Belt",
    "dropLevel": 2,
    "act": 1
  },
  14:{
    "baseItem": "Rustic Sash",
    "dropLevel": 2,
    "act": 1
  },
  15:{
    "baseItem": "Shabby Jerkin",
    "dropLevel": 2,
    "act": 1
  },
  16:{
    "baseItem": "Rusted Hatchet",
    "dropLevel": 2,
    "act": 1
  },
  17:{
    "baseItem": "Iron Ring",
    "dropLevel": 2,
    "act": 1
  },
  18:{
    "baseItem": "Goathide Buckler",
    "dropLevel": 2,
    "act": 1
  },
  19:{
    "baseItem": "Paua Amulet",
    "dropLevel": 3,
    "act": 1
  },
  20:{
    "baseItem": "Coral Amulet",
    "dropLevel": 3,
    "act": 1
  },
  21:{
    "baseItem": "Simple Robe",
    "dropLevel": 3,
    "act": 1
  },
  22:{
    "baseItem": "Wool Shoes",
    "dropLevel": 3,
    "act": 1
  },
  23:{
    "baseItem": "Rawhide Boots",
    "dropLevel": 3,
    "act": 1
  },
  24:{
    "baseItem": "Nailed Fist",
    "dropLevel": 3,
    "act": 1
  },
  25:{
    "baseItem": "Wool Gloves",
    "dropLevel": 3,
    "act": 1
  },
  26:{
    "baseItem": "Rawhide Gloves",
    "dropLevel": 3,
    "act": 1
  },
  27:{
    "baseItem": "Vine Circlet",
    "dropLevel": 3,
    "act": 1
  },
  28:{
    "baseItem": "Leather Cap",
    "dropLevel": 3,
    "act": 1
  },
  29:{
    "baseItem": "Medium Life Flask",
    "dropLevel": 3,
    "act": 1
  },
  30:{
    "baseItem": "Medium Mana Flask",
    "dropLevel": 3,
    "act": 1
  },
  31:{
    "baseItem": "Twig Spirit Shield",
    "dropLevel": 3,
    "act": 1
  },
  32:{
    "baseItem": "Rusted Spike",
    "dropLevel": 3,
    "act": 1
  },
  33:{
    "baseItem": "Driftwood Maul",
    "dropLevel": 3,
    "act": 1
  },
  34:{
    "baseItem": "Corroded Blade",
    "dropLevel": 3,
    "act": 1
  },
  35:{
    "baseItem": "Scale Vest",
    "dropLevel": 4,
    "act": 1
  },
  36:{
    "baseItem": "Chainmail Vest",
    "dropLevel": 4,
    "act": 1
  },
  37:{
    "baseItem": "Padded Vest",
    "dropLevel": 4,
    "act": 1
  },
  38:{
    "baseItem": "Fishscale Gauntlets",
    "dropLevel": 4,
    "act": 1
  },
  39:{
    "baseItem": "Scare Mask",
    "dropLevel": 4,
    "act": 1
  },
  40:{
    "baseItem": "Battered Helm",
    "dropLevel": 4,
    "act": 1
  },
  41:{
    "baseItem": "Serrated Arrow Quiver",
    "dropLevel": 4,
    "act": 1
  },
  42:{
    "baseItem": "Coral Ring",
    "dropLevel": 4,
    "act": 1
  },
  43:{
    "baseItem": "Gnarled Branch",
    "dropLevel": 4,
    "act": 1
  },
  44:{
    "baseItem": "Stone Axe",
    "dropLevel": 4,
    "act": 1
  },
  47:{
    "baseItem": "Chain Boots",
    "dropLevel": 5,
    "act": 1
  },
  48:{
    "baseItem": "Short Bow",
    "dropLevel": 5,
    "act": 1
  },
  49:{
    "baseItem": "Skinning Knife",
    "dropLevel": 5,
    "act": 1
  },
  50:{
    "baseItem": "Wrapped Mitts",
    "dropLevel": 5,
    "act": 1
  },
  51:{
    "baseItem": "Rusted Coif",
    "dropLevel": 5,
    "act": 1
  },
  52:{
    "baseItem": "Tribal Club",
    "dropLevel": 5,
    "act": 1
  },
  53:{
    "baseItem": "Copper Sword",
    "dropLevel": 5,
    "act": 1
  },
  54:{
    "baseItem": "Paua Ring",
    "dropLevel": 5,
    "act": 1
  },
  55:{
    "baseItem": "Darkwood Sceptre",
    "dropLevel": 5,
    "act": 1
  },
  56:{
    "baseItem": "Rotted Round Shield",
    "dropLevel": 5,
    "act": 1
  },
  57:{
    "baseItem": "Spiked Bundle",
    "dropLevel": 5,
    "act": 1
  },
  58:{
    "baseItem": "Corroded Tower Shield",
    "dropLevel": 5,
    "act": 1
  },
  59:{
    "baseItem": "Chestplate",
    "dropLevel": 6,
    "act": 1
  },
  60:{
    "baseItem": "Wrapped Boots",
    "dropLevel": 6,
    "act": 1
  },
  61:{
    "baseItem": "Leatherscale Boots",
    "dropLevel": 6,
    "act": 1
  },
  62:{
    "baseItem": "Large Life Flask",
    "dropLevel": 6,
    "act": 1
  },
  63:{
    "baseItem": "Large Mana Flask",
    "dropLevel": 6,
    "act": 1
  },
  64:{
    "baseItem": "Jade Hatchet",
    "dropLevel": 6,
    "act": 1
  },
  65:{
    "baseItem": "Goat's Horn",
    "dropLevel": 6,
    "act": 1
  },
  66:{
    "baseItem": "Jade Amulet",
    "dropLevel": 7,
    "act": 1
  },
  67:{
    "baseItem": "Lapis Amulet",
    "dropLevel": 7,
    "act": 1
  },
  68:{
    "baseItem": "Amber Amulet",
    "dropLevel": 7,
    "act": 1
  },
  69:{
    "baseItem": "Sharktooth Claw",
    "dropLevel": 7,
    "act": 1
  },
  70:{
    "baseItem": "Chain Gloves",
    "dropLevel": 7,
    "act": 1
  },
  71:{
    "baseItem": "Cone Helmet",
    "dropLevel": 7,
    "act": 1
  },
  72:{
    "baseItem": "Plank Kite Shield",
    "dropLevel": 7,
    "act": 1
  },
  73:{
    "baseItem": "Whalebone Rapier",
    "dropLevel": 7,
    "act": 1
  },
  74:{
    "baseItem": "Chainmail Tunic",
    "dropLevel": 8,
    "act": 1
  },
  75:{
    "baseItem": "Light Brigandine",
    "dropLevel": 8,
    "act": 1
  },
  76:{
    "baseItem": "Iron Circlet",
    "dropLevel": 8,
    "act": 1
  },
  77:{
    "baseItem": "Sapphire Ring",
    "dropLevel": 8,
    "act": 1
  },
  78:{
    "baseItem": "Pine Buckler",
    "dropLevel": 8,
    "act": 1
  },
  79:{
    "baseItem": "Tribal Maul",
    "dropLevel": 8,
    "act": 1
  },
  80:{
    "baseItem": "Longsword",
    "dropLevel": 8,
    "act": 1
  },
  81:{
    "baseItem": "Oiled Vest",
    "dropLevel": 9,
    "act": 1
  },
  82:{
    "baseItem": "Strapped Leather",
    "dropLevel": 9,
    "act": 1
  },
  83:{
    "baseItem": "Steel Greaves",
    "dropLevel": 9,
    "act": 1
  },
  84:{
    "baseItem": "Velvet Slippers",
    "dropLevel": 9,
    "act": 1
  },
  85:{
    "baseItem": "Long Bow",
    "dropLevel": 9,
    "act": 1
  },
  86:{
    "baseItem": "Goathide Gloves",
    "dropLevel": 9,
    "act": 1
  },
  87:{
    "baseItem": "Fire Arrow Quiver",
    "dropLevel": 9,
    "act": 1
  },
  88:{
    "baseItem": "Yew Spirit Shield",
    "dropLevel": 9,
    "act": 1
  },
  89:{
    "baseItem": "Primitive Staff",
    "dropLevel": 9,
    "act": 1
  },
  90:{
    "baseItem": "Jade Chopper",
    "dropLevel": 9,
    "act": 1
  },
  91:{
    "baseItem": "Heavy Belt",
    "dropLevel": 10,
    "act": 1
  },
  92:{
    "baseItem": "Leather Belt",
    "dropLevel": 10,
    "act": 1
  },
  93:{
    "baseItem": "Tricorne",
    "dropLevel": 10,
    "act": 1
  },
  94:{
    "baseItem": "Plague Mask",
    "dropLevel": 10,
    "act": 1
  },
  95:{
    "baseItem": "Small Hybrid Flask",
    "dropLevel": 10,
    "act": 1
  },
  96:{
    "baseItem": "Spiked Club",
    "dropLevel": 10,
    "act": 1
  },
  97:{
    "baseItem": "Sabre",
    "dropLevel": 10,
    "act": 1
  },
  98:{
    "baseItem": "Carving Knife",
    "dropLevel": 10,
    "act": 1
  },
  99:{
    "baseItem": "Bronze Sceptre",
    "dropLevel": 10,
    "act": 1
  },
  100:{
    "baseItem": "Silken Vest",
    "dropLevel": 11,
    "act": 1
  },
  101:{
    "baseItem": "Plated Gauntlets",
    "dropLevel": 11,
    "act": 1
  },
  102:{
    "baseItem": "Boarding Axe",
    "dropLevel": 11,
    "act": 1
  },
  103:{
    "baseItem": "Rawhide Tower Shield",
    "dropLevel": 11,
    "act": 1
  },
  104:{
    "baseItem": "Goathide Boots",
    "dropLevel": 12,
    "act": 1
  },
  105:{
    "baseItem": "Awl",
    "dropLevel": 12,
    "act": 1
  },
  106:{
    "baseItem": "Velvet Gloves",
    "dropLevel": 12,
    "act": 1
  },
  107:{
    "baseItem": "Soldier Helmet",
    "dropLevel": 12,
    "act": 1
  },
  108:{
    "baseItem": "Greater Life Flask",
    "dropLevel": 12,
    "act": 1
  },
  109:{
    "baseItem": "Greater Mana Flask",
    "dropLevel": 12,
    "act": 1
  },
  110:{
    "baseItem": "Topaz Ring",
    "dropLevel": 12,
    "act": 1
  },
  111:{
    "baseItem": "Driftwood Spiked Shield",
    "dropLevel": 12,
    "act": 1
  },
  112:{
    "baseItem": "Fir Round Shield",
    "dropLevel": 12,
    "act": 1
  },
  113:{
    "baseItem": "Battered Foil",
    "dropLevel": 12,
    "act": 1
  },
  114:{
    "baseItem": "Mallet",
    "dropLevel": 12,
    "act": 1
  },
  115:{
    "baseItem": "Bastard Sword",
    "dropLevel": 12,
    "act": 1
  },
  116:{
    "baseItem": "Carved Wand",
    "dropLevel": 12,
    "act": 1
  },
  117:{
    "baseItem": "Ringmail Boots",
    "dropLevel": 13,
    "act": 2
  },
  118:{
    "baseItem": "Sallet",
    "dropLevel": 13,
    "act": 2
  },
  119:{
    "baseItem": "Linden Kite Shield",
    "dropLevel": 13,
    "act": 2
  },
  120:{
    "baseItem": "Woodsplitter",
    "dropLevel": 13,
    "act": 2
  },
  121:{
    "baseItem": "Iron Staff",
    "dropLevel": 13,
    "act": 2
  },
  122:{
    "baseItem": "Composite Bow",
    "dropLevel": 14,
    "act": 2
  },
  123:{
    "baseItem": "Sharktooth Arrow Quiver",
    "dropLevel": 14,
    "act": 2
  },
  124:{
    "baseItem": "Gold Amulet",
    "dropLevel": 15,
    "act": 2
  },
  125:{
    "baseItem": "Stiletto",
    "dropLevel": 15,
    "act": 2
  },
  126:{
    "baseItem": "Ironscale Gauntlets",
    "dropLevel": 15,
    "act": 2
  },
  127:{
    "baseItem": "Stone Hammer",
    "dropLevel": 15,
    "act": 2
  },
  128:{
    "baseItem": "Broad Sword",
    "dropLevel": 15,
    "act": 2
  },
  129:{
    "baseItem": "Quartz Sceptre",
    "dropLevel": 15,
    "act": 2
  },
  130:{
    "baseItem": "Bone Spirit Shield",
    "dropLevel": 15,
    "act": 2
  },
  131:{
    "baseItem": "Strapped Boots",
    "dropLevel": 16,
    "act": 2
  },
  132:{
    "baseItem": "Strapped Mitts",
    "dropLevel": 16,
    "act": 2
  },
  133:{
    "baseItem": "Cleaver",
    "dropLevel": 16,
    "act": 2
  },
  134:{
    "baseItem": "Ruby Ring",
    "dropLevel": 16,
    "act": 2
  },
  135:{
    "baseItem": "Painted Buckler",
    "dropLevel": 16,
    "act": 2
  },
  136:{
    "baseItem": "Ringmail Coat",
    "dropLevel": 17,
    "act": 2
  },
  137:{
    "baseItem": "Buckskin Tunic",
    "dropLevel": 17,
    "act": 2
  },
  138:{
    "baseItem": "Scale Doublet",
    "dropLevel": 17,
    "act": 2
  },
  139:{
    "baseItem": "Copper Plate",
    "dropLevel": 17,
    "act": 2
  },
  140:{
    "baseItem": "Cat's Paw",
    "dropLevel": 17,
    "act": 2
  },
  141:{
    "baseItem": "Iron Mask",
    "dropLevel": 17,
    "act": 2
  },
  142:{
    "baseItem": "Torture Cage",
    "dropLevel": 17,
    "act": 2
  },
  143:{
    "baseItem": "Cedar Tower Shield",
    "dropLevel": 17,
    "act": 2
  },
  144:{
    "baseItem": "Basket Rapier",
    "dropLevel": 17,
    "act": 2
  },
  145:{
    "baseItem": "Sledgehammer",
    "dropLevel": 17,
    "act": 2
  },
  146:{
    "baseItem": "Two-Handed Sword",
    "dropLevel": 17,
    "act": 2
  },
  147:{
    "baseItem": "Scholar's Robe",
    "dropLevel": 18,
    "act": 2
  },
  148:{
    "baseItem": "Padded Jacket",
    "dropLevel": 18,
    "act": 2
  },
  149:{
    "baseItem": "Ironscale Boots",
    "dropLevel": 18,
    "act": 2
  },
  150:{
    "baseItem": "Recurve Bow",
    "dropLevel": 18,
    "act": 2
  },
  151:{
    "baseItem": "Barbute Helmet",
    "dropLevel": 18,
    "act": 2
  },
  152:{
    "baseItem": "Grand Life Flask",
    "dropLevel": 18,
    "act": 2
  },
  153:{
    "baseItem": "Grand Mana Flask",
    "dropLevel": 18,
    "act": 2
  },
  154:{
    "baseItem": "Long Staff",
    "dropLevel": 18,
    "act": 2
  },
  155:{
    "baseItem": "Poleaxe",
    "dropLevel": 18,
    "act": 2
  },
  156:{
    "baseItem": "Quartz Wand",
    "dropLevel": 18,
    "act": 2
  },
  157:{
    "baseItem": "Ringmail Gloves",
    "dropLevel": 19,
    "act": 2
  },
  158:{
    "baseItem": "Turquoise Amulet",
    "dropLevel": 20,
    "act": 2
  },
  159:{
    "baseItem": "Citrine Amulet",
    "dropLevel": 20,
    "act": 2
  },
  160:{
    "baseItem": "Agate Amulet",
    "dropLevel": 20,
    "act": 2
  },
  161:{
    "baseItem": "Studded Belt",
    "dropLevel": 20,
    "act": 2
  },
  162:{
    "baseItem": "Cloth Belt",
    "dropLevel": 20,
    "act": 2
  },
  163:{
    "baseItem": "Leather Hood",
    "dropLevel": 20,
    "act": 2
  },
  164:{
    "baseItem": "Medium Hybrid Flask",
    "dropLevel": 20,
    "act": 2
  },
  165:{
    "baseItem": "War Hammer",
    "dropLevel": 20,
    "act": 2
  },
  166:{
    "baseItem": "War Sword",
    "dropLevel": 20,
    "act": 2
  },
  167:{
    "baseItem": "Feathered Arrow Quiver",
    "dropLevel": 20,
    "act": 2
  },
  168:{
    "baseItem": "Gold Ring",
    "dropLevel": 20,
    "act": 2
  },
  169:{
    "baseItem": "Two-Stone Ring",
    "dropLevel": 20,
    "act": 2
  },
  172:{
    "baseItem": "Boot Knife",
    "dropLevel": 20,
    "act": 2
  },
  173:{
    "baseItem": "Iron Sceptre",
    "dropLevel": 20,
    "act": 2
  },
  174:{
    "baseItem": "Studded Round Shield",
    "dropLevel": 20,
    "act": 2
  },
  175:{
    "baseItem": "Alloyed Spiked Shield",
    "dropLevel": 20,
    "act": 2
  },
  176:{
    "baseItem": "Reinforced Kite Shield",
    "dropLevel": 20,
    "act": 2
  },
  177:{
    "baseItem": "Calling Wand",
    "dropLevel": 20,
    "act": 2
  },
  178:{
    "baseItem": "Infantry Brigandine",
    "dropLevel": 21,
    "act": 2
  },
  179:{
    "baseItem": "War Plate",
    "dropLevel": 21,
    "act": 2
  },
  180:{
    "baseItem": "Chainmail Doublet",
    "dropLevel": 21,
    "act": 2
  },
  181:{
    "baseItem": "Deerskin Gloves",
    "dropLevel": 21,
    "act": 2
  },
  182:{
    "baseItem": "Broad Axe",
    "dropLevel": 21,
    "act": 2
  },
  183:{
    "baseItem": "Oiled Coat",
    "dropLevel": 22,
    "act": 2
  },
  184:{
    "baseItem": "Silk Slippers",
    "dropLevel": 22,
    "act": 2
  },
  185:{
    "baseItem": "Deerskin Boots",
    "dropLevel": 22,
    "act": 2
  },
  186:{
    "baseItem": "Blinder",
    "dropLevel": 22,
    "act": 2
  },
  187:{
    "baseItem": "Great Helmet",
    "dropLevel": 22,
    "act": 2
  },
  188:{
    "baseItem": "Jagged Foil",
    "dropLevel": 22,
    "act": 2
  },
  189:{
    "baseItem": "Jagged Maul",
    "dropLevel": 22,
    "act": 2
  },
  190:{
    "baseItem": "Etched Greatsword",
    "dropLevel": 22,
    "act": 2
  },
  191:{
    "baseItem": "Plated Greaves",
    "dropLevel": 23,
    "act": 3
  },
  192:{
    "baseItem": "Bone Bow",
    "dropLevel": 23,
    "act": 3
  },
  193:{
    "baseItem": "Bronze Gauntlets",
    "dropLevel": 23,
    "act": 3
  },
  194:{
    "baseItem": "Visored Sallet",
    "dropLevel": 23,
    "act": 3
  },
  195:{
    "baseItem": "Hammered Buckler",
    "dropLevel": 23,
    "act": 3
  },
  196:{
    "baseItem": "Tarnished Spirit Shield",
    "dropLevel": 23,
    "act": 3
  },
  197:{
    "baseItem": "Double Axe",
    "dropLevel": 23,
    "act": 3
  },
  198:{
    "baseItem": "Coiled Staff",
    "dropLevel": 23,
    "act": 3
  },
  199:{
    "baseItem": "Giant Life Flask",
    "dropLevel": 24,
    "act": 3
  },
  200:{
    "baseItem": "Giant Mana Flask",
    "dropLevel": 24,
    "act": 3
  },
  201:{
    "baseItem": "Bladed Mace",
    "dropLevel": 24,
    "act": 3
  },
  202:{
    "baseItem": "Ancient Sword",
    "dropLevel": 24,
    "act": 3
  },
  203:{
    "baseItem": "Copper Kris",
    "dropLevel": 24,
    "act": 3
  },
  204:{
    "baseItem": "Ochre Sceptre",
    "dropLevel": 24,
    "act": 3
  },
  205:{
    "baseItem": "Copper Tower Shield",
    "dropLevel": 24,
    "act": 3
  },
  206:{
    "baseItem": "Spiraled Wand",
    "dropLevel": 24,
    "act": 3
  },
  207:{
    "baseItem": "Onyx Amulet",
    "dropLevel": 25,
    "act": 3
  },
  208:{
    "baseItem": "Silken Garb",
    "dropLevel": 25,
    "act": 3
  },
  209:{
    "baseItem": "Wild Leather",
    "dropLevel": 25,
    "act": 3
  },
  210:{
    "baseItem": "Silk Gloves",
    "dropLevel": 25,
    "act": 3
  },
  211:{
    "baseItem": "Arming Axe",
    "dropLevel": 25,
    "act": 3
  },
  212:{
    "baseItem": "Penetrating Arrow Quiver",
    "dropLevel": 25,
    "act": 3
  },
  213:{
    "baseItem": "Diamond Ring",
    "dropLevel": 25,
    "act": 3
  },
  214:{
    "baseItem": "Moonstone Ring",
    "dropLevel": 25,
    "act": 3
  },
  215:{
    "baseItem": "Timeworn Claw",
    "dropLevel": 26,
    "act": 3
  },
  216:{
    "baseItem": "Tribal Circlet",
    "dropLevel": 26,
    "act": 3
  },
  217:{
    "baseItem": "Close Helmet",
    "dropLevel": 26,
    "act": 3
  },
  218:{
    "baseItem": "Antique Rapier",
    "dropLevel": 26,
    "act": 3
  },
  219:{
    "baseItem": "Clasped Boots",
    "dropLevel": 27,
    "act": 3
  },
  220:{
    "baseItem": "Bronzescale Gauntlets",
    "dropLevel": 27,
    "act": 3
  },
  221:{
    "baseItem": "Scarlet Round Shield",
    "dropLevel": 27,
    "act": 3
  },
  222:{
    "baseItem": "Burnished Spiked Shield",
    "dropLevel": 27,
    "act": 3
  },
  223:{
    "baseItem": "Layered Kite Shield",
    "dropLevel": 27,
    "act": 3
  },
  224:{
    "baseItem": "Brass Maul",
    "dropLevel": 27,
    "act": 3
  },
  225:{
    "baseItem": "Ornate Sword",
    "dropLevel": 27,
    "act": 3
  },
  226:{
    "baseItem": "Full Leather",
    "dropLevel": 28,
    "act": 3
  },
  227:{
    "baseItem": "Full Plate",
    "dropLevel": 28,
    "act": 3
  },
  228:{
    "baseItem": "Full Ringmail",
    "dropLevel": 28,
    "act": 3
  },
  229:{
    "baseItem": "Full Scale Armour",
    "dropLevel": 28,
    "act": 3
  },
  230:{
    "baseItem": "Scarlet Raiment",
    "dropLevel": 28,
    "act": 3
  },
  231:{
    "baseItem": "Mage's Vestment",
    "dropLevel": 28,
    "act": 3
  },
  232:{
    "baseItem": "Mesh Boots",
    "dropLevel": 28,
    "act": 3
  },
  233:{
    "baseItem": "Royal Bow",
    "dropLevel": 28,
    "act": 3
  },
  234:{
    "baseItem": "Festival Mask",
    "dropLevel": 28,
    "act": 3
  },
  235:{
    "baseItem": "Ceremonial Mace",
    "dropLevel": 28,
    "act": 3
  },
  236:{
    "baseItem": "Elegant Sword",
    "dropLevel": 28,
    "act": 3
  },
  237:{
    "baseItem": "Skean",
    "dropLevel": 28,
    "act": 3
  },
  238:{
    "baseItem": "Ritual Sceptre",
    "dropLevel": 28,
    "act": 3
  },
  239:{
    "baseItem": "Jingling Spirit Shield",
    "dropLevel": 28,
    "act": 3
  },
  240:{
    "baseItem": "Royal Staff",
    "dropLevel": 28,
    "act": 3
  },
  241:{
    "baseItem": "Gilded Axe",
    "dropLevel": 28,
    "act": 3
  },
  242:{
    "baseItem": "Decorative Axe",
    "dropLevel": 29,
    "act": 3
  },
  243:{
    "baseItem": "War Buckler",
    "dropLevel": 29,
    "act": 3
  },
  244:{
    "baseItem": "Bronzescale Boots",
    "dropLevel": 30,
    "act": 3
  },
  245:{
    "baseItem": "Sparkling Claw",
    "dropLevel": 30,
    "act": 3
  },
  246:{
    "baseItem": "Flaying Knife",
    "dropLevel": 30,
    "act": 3
  },
  247:{
    "baseItem": "Wolf Pelt",
    "dropLevel": 30,
    "act": 3
  },
  248:{
    "baseItem": "Large Hybrid Flask",
    "dropLevel": 30,
    "act": 3
  },
  249:{
    "baseItem": "Colossal Life Flask",
    "dropLevel": 30,
    "act": 3
  },
  250:{
    "baseItem": "Colossal Mana Flask",
    "dropLevel": 30,
    "act": 3
  },
  251:{
    "baseItem": "Bone Ring",
    "dropLevel": 30,
    "act": 3
  },
  252:{
    "baseItem": "Reinforced Tower Shield",
    "dropLevel": 30,
    "act": 3
  },
  253:{
    "baseItem": "Elegant Foil",
    "dropLevel": 30,
    "act": 3
  },
  254:{
    "baseItem": "Sage Wand",
    "dropLevel": 30,
    "act": 3
  },
  255:{
    "baseItem": "Clasped Mitts",
    "dropLevel": 31,
    "act": 3
  },
  256:{
    "baseItem": "Crusader Helmet",
    "dropLevel": 31,
    "act": 3
  },
  257:{
    "baseItem": "Blunt Arrow Quiver",
    "dropLevel": 31,
    "act": 3
  },
  258:{
    "baseItem": "Full Chainmail",
    "dropLevel": 32,
    "act": 3
  },
  259:{
    "baseItem": "Silk Robe",
    "dropLevel": 32,
    "act": 3
  },
  260:{
    "baseItem": "Arena Plate",
    "dropLevel": 32,
    "act": 3
  },
  261:{
    "baseItem": "Waxed Garb",
    "dropLevel": 32,
    "act": 3
  },
  262:{
    "baseItem": "Sun Leather",
    "dropLevel": 32,
    "act": 3
  },
  263:{
    "baseItem": "Soldier's Brigandine",
    "dropLevel": 32,
    "act": 3
  },
  264:{
    "baseItem": "Scholar Boots",
    "dropLevel": 32,
    "act": 3
  },
  265:{
    "baseItem": "Death Bow",
    "dropLevel": 32,
    "act": 3
  },
  266:{
    "baseItem": "Mesh Gloves",
    "dropLevel": 32,
    "act": 3
  },
  267:{
    "baseItem": "Dream Mace",
    "dropLevel": 32,
    "act": 3
  },
  268:{
    "baseItem": "Dusk Blade",
    "dropLevel": 32,
    "act": 3
  },
  269:{
    "baseItem": "Imp Dagger",
    "dropLevel": 32,
    "act": 3
  },
  270:{
    "baseItem": "Shadow Sceptre",
    "dropLevel": 32,
    "act": 3
  },
  271:{
    "baseItem": "Fright Maul",
    "dropLevel": 32,
    "act": 3
  },
  272:{
    "baseItem": "Spectral Sword",
    "dropLevel": 32,
    "act": 3
  },
  273:{
    "baseItem": "Reinforced Greaves",
    "dropLevel": 33,
    "act": 4
  },
  274:{
    "baseItem": "Nubuck Gloves",
    "dropLevel": 33,
    "act": 4
  },
  275:{
    "baseItem": "Gilded Sallet",
    "dropLevel": 33,
    "act": 4
  },
  276:{
    "baseItem": "Spectral Axe",
    "dropLevel": 33,
    "act": 4
  },
  277:{
    "baseItem": "Splendid Round Shield",
    "dropLevel": 33,
    "act": 4
  },
  278:{
    "baseItem": "Ornate Spiked Shield",
    "dropLevel": 33,
    "act": 4
  },
  279:{
    "baseItem": "Brass Spirit Shield",
    "dropLevel": 33,
    "act": 4
  },
  280:{
    "baseItem": "Shadow Axe",
    "dropLevel": 33,
    "act": 4
  },
  281:{
    "baseItem": "Vile Staff",
    "dropLevel": 33,
    "act": 4
  },
  282:{
    "baseItem": "Shackled Boots",
    "dropLevel": 34,
    "act": 4
  },
  283:{
    "baseItem": "Nubuck Boots",
    "dropLevel": 34,
    "act": 4
  },
  284:{
    "baseItem": "Fright Claw",
    "dropLevel": 34,
    "act": 4
  },
  285:{
    "baseItem": "Bone Circlet",
    "dropLevel": 34,
    "act": 4
  },
  286:{
    "baseItem": "Wyrm Mace",
    "dropLevel": 34,
    "act": 4
  },
  287:{
    "baseItem": "Hook Sword",
    "dropLevel": 34,
    "act": 4
  },
  288:{
    "baseItem": "Ceremonial Kite Shield",
    "dropLevel": 34,
    "act": 4
  },
  289:{
    "baseItem": "Gilded Buckler",
    "dropLevel": 34,
    "act": 4
  },
  290:{
    "baseItem": "Thorn Rapier",
    "dropLevel": 34,
    "act": 4
  },
  291:{
    "baseItem": "Morning Star",
    "dropLevel": 34,
    "act": 4
  },
  292:{
    "baseItem": "Pagan Wand",
    "dropLevel": 34,
    "act": 4
  },
  293:{
    "baseItem": "Thief's Garb",
    "dropLevel": 35,
    "act": 4
  },
  294:{
    "baseItem": "Cabalist Regalia",
    "dropLevel": 35,
    "act": 4
  },
  295:{
    "baseItem": "Bone Armour",
    "dropLevel": 35,
    "act": 4
  },
  296:{
    "baseItem": "Holy Chainmail",
    "dropLevel": 35,
    "act": 4
  },
  297:{
    "baseItem": "Lordly Plate",
    "dropLevel": 35,
    "act": 4
  },
  298:{
    "baseItem": "Field Lamellar",
    "dropLevel": 35,
    "act": 4
  },
  299:{
    "baseItem": "Grove Bow",
    "dropLevel": 35,
    "act": 4
  },
  300:{
    "baseItem": "Steel Gauntlets",
    "dropLevel": 35,
    "act": 4
  },
  301:{
    "baseItem": "Golden Mask",
    "dropLevel": 35,
    "act": 4
  },
  302:{
    "baseItem": "Gladiator Helmet",
    "dropLevel": 35,
    "act": 4
  },
  303:{
    "baseItem": "Etched Hatchet",
    "dropLevel": 35,
    "act": 4
  },
  304:{
    "baseItem": "Petrified Club",
    "dropLevel": 35,
    "act": 4
  },
  305:{
    "baseItem": "Variscite Blade",
    "dropLevel": 35,
    "act": 4
  },
  306:{
    "baseItem": "Grinning Fetish",
    "dropLevel": 35,
    "act": 4
  },
  307:{
    "baseItem": "Painted Tower Shield",
    "dropLevel": 35,
    "act": 4
  },
  308:{
    "baseItem": "Curved Blade",
    "dropLevel": 35,
    "act": 4
  },
  309:{
    "baseItem": "Faun's Horn",
    "dropLevel": 35,
    "act": 4
  },
  310:{
    "baseItem": "Riveted Boots",
    "dropLevel": 36,
    "act": 4
  },
  311:{
    "baseItem": "Steelscale Boots",
    "dropLevel": 36,
    "act": 4
  },
  312:{
    "baseItem": "Reflex Bow",
    "dropLevel": 36,
    "act": 4
  },
  313:{
    "baseItem": "Double Claw",
    "dropLevel": 36,
    "act": 4
  },
  314:{
    "baseItem": "Prong Dagger",
    "dropLevel": 36,
    "act": 4
  },
  315:{
    "baseItem": "Embroidered Gloves",
    "dropLevel": 36,
    "act": 4
  },
  316:{
    "baseItem": "Steelscale Gauntlets",
    "dropLevel": 36,
    "act": 4
  },
  317:{
    "baseItem": "Trapper Mitts",
    "dropLevel": 36,
    "act": 4
  },
  318:{
    "baseItem": "Secutor Helm",
    "dropLevel": 36,
    "act": 4
  },
  319:{
    "baseItem": "Sacred Life Flask",
    "dropLevel": 36,
    "act": 4
  },
  320:{
    "baseItem": "Sacred Mana Flask",
    "dropLevel": 36,
    "act": 4
  },
  321:{
    "baseItem": "Jasper Axe",
    "dropLevel": 36,
    "act": 4
  },
  322:{
    "baseItem": "Two-Point Arrow Quiver",
    "dropLevel": 36,
    "act": 4
  },
  323:{
    "baseItem": "Horned Sceptre",
    "dropLevel": 36,
    "act": 4
  },
  324:{
    "baseItem": "Crescent Staff",
    "dropLevel": 36,
    "act": 4
  },
  325:{
    "baseItem": "Smallsword",
    "dropLevel": 36,
    "act": 4
  },
  326:{
    "baseItem": "Dagger Axe",
    "dropLevel": 36,
    "act": 4
  },
  327:{
    "baseItem": "Totemic Maul",
    "dropLevel": 36,
    "act": 4
  },
  328:{
    "baseItem": "Butcher Sword",
    "dropLevel": 36,
    "act": 4
  },
  329:{
    "baseItem": "Eelskin Tunic",
    "dropLevel": 37,
    "act": 4
  },
  330:{
    "baseItem": "Sage's Robe",
    "dropLevel": 37,
    "act": 4
  },
  331:{
    "baseItem": "Bronze Plate",
    "dropLevel": 37,
    "act": 4
  },
  332:{
    "baseItem": "Antique Greaves",
    "dropLevel": 37,
    "act": 4
  },
  333:{
    "baseItem": "Thresher Claw",
    "dropLevel": 37,
    "act": 4
  },
  334:{
    "baseItem": "Riveted Gloves",
    "dropLevel": 37,
    "act": 4
  },
  335:{
    "baseItem": "Aventail Helmet",
    "dropLevel": 37,
    "act": 4
  },
  336:{
    "baseItem": "Walnut Spirit Shield",
    "dropLevel": 37,
    "act": 4
  },
  337:{
    "baseItem": "Woodful Staff",
    "dropLevel": 37,
    "act": 4
  },
  338:{
    "baseItem": "Wyrmbone Rapier",
    "dropLevel": 37,
    "act": 4
  },
  339:{
    "baseItem": "Jasper Chopper",
    "dropLevel": 37,
    "act": 4
  },
  340:{
    "baseItem": "Wyrmscale Doublet",
    "dropLevel": 38,
    "act": 4
  },
  341:{
    "baseItem": "Satin Slippers",
    "dropLevel": 38,
    "act": 4
  },
  342:{
    "baseItem": "Decurve Bow",
    "dropLevel": 38,
    "act": 4
  },
  343:{
    "baseItem": "Eelskin Gloves",
    "dropLevel": 38,
    "act": 4
  },
  344:{
    "baseItem": "Raven Mask",
    "dropLevel": 38,
    "act": 4
  },
  345:{
    "baseItem": "Barbed Club",
    "dropLevel": 38,
    "act": 4
  },
  346:{
    "baseItem": "Cutlass",
    "dropLevel": 38,
    "act": 4
  },
  347:{
    "baseItem": "Amethyst Ring",
    "dropLevel": 38,
    "act": 4
  },
  348:{
    "baseItem": "Butcher Knife",
    "dropLevel": 38,
    "act": 4
  },
  349:{
    "baseItem": "Sekhem",
    "dropLevel": 38,
    "act": 4
  },
  350:{
    "baseItem": "Oak Buckler",
    "dropLevel": 38,
    "act": 4
  },
  351:{
    "baseItem": "Latticed Ringmail",
    "dropLevel": 39,
    "act": 4
  },
  352:{
    "baseItem": "Eelskin Boots",
    "dropLevel": 39,
    "act": 4
  },
  353:{
    "baseItem": "Antique Gauntlets",
    "dropLevel": 39,
    "act": 4
  },
  354:{
    "baseItem": "Lunaris Circlet",
    "dropLevel": 39,
    "act": 4
  },
  355:{
    "baseItem": "Tomahawk",
    "dropLevel": 39,
    "act": 4
  },
  356:{
    "baseItem": "Buckskin Tower Shield",
    "dropLevel": 39,
    "act": 4
  },
  357:{
    "baseItem": "Maple Round Shield",
    "dropLevel": 39,
    "act": 4
  },
  358:{
    "baseItem": "Redwood Spiked Shield",
    "dropLevel": 39,
    "act": 4
  },
  359:{
    "baseItem": "Quilted Jacket",
    "dropLevel": 40,
    "act": 5
  },
  360:{
    "baseItem": "Zealot Boots",
    "dropLevel": 40,
    "act": 5
  },
  361:{
    "baseItem": "Gouger",
    "dropLevel": 40,
    "act": 5
  },
  362:{
    "baseItem": "Reaver Helmet",
    "dropLevel": 40,
    "act": 5
  },
  363:{
    "baseItem": "Colossal Hybrid Flask",
    "dropLevel": 40,
    "act": 5
  },
  364:{
    "baseItem": "Spike-Point Arrow Quiver",
    "dropLevel": 40,
    "act": 5
  },
  365:{
    "baseItem": "Etched Kite Shield",
    "dropLevel": 40,
    "act": 5
  },
  366:{
    "baseItem": "Burnished Foil",
    "dropLevel": 40,
    "act": 5
  },
  367:{
    "baseItem": "Great Mallet",
    "dropLevel": 40,
    "act": 5
  },
  368:{
    "baseItem": "Footman Sword",
    "dropLevel": 40,
    "act": 5
  },
  369:{
    "baseItem": "Engraved Wand",
    "dropLevel": 40,
    "act": 5
  },
  370:{
    "baseItem": "Silken Wrap",
    "dropLevel": 41,
    "act": 5
  },
  371:{
    "baseItem": "Frontier Leather",
    "dropLevel": 41,
    "act": 5
  },
  372:{
    "baseItem": "Battle Plate",
    "dropLevel": 41,
    "act": 5
  },
  373:{
    "baseItem": "Trapper Boots",
    "dropLevel": 41,
    "act": 5
  },
  374:{
    "baseItem": "Compound Bow",
    "dropLevel": 41,
    "act": 5
  },
  375:{
    "baseItem": "Poignard",
    "dropLevel": 41,
    "act": 5
  },
  376:{
    "baseItem": "Satin Gloves",
    "dropLevel": 41,
    "act": 5
  },
  377:{
    "baseItem": "Hunter Hood",
    "dropLevel": 41,
    "act": 5
  },
  378:{
    "baseItem": "Rock Breaker",
    "dropLevel": 41,
    "act": 5
  },
  379:{
    "baseItem": "Baselard",
    "dropLevel": 41,
    "act": 5
  },
  380:{
    "baseItem": "Crystal Sceptre",
    "dropLevel": 41,
    "act": 5
  },
  381:{
    "baseItem": "Ivory Spirit Shield",
    "dropLevel": 41,
    "act": 5
  },
  382:{
    "baseItem": "Timber Axe",
    "dropLevel": 41,
    "act": 5
  },
  383:{
    "baseItem": "Military Staff",
    "dropLevel": 41,
    "act": 5
  },
  384:{
    "baseItem": "Hussar Brigandine",
    "dropLevel": 42,
    "act": 5
  },
  385:{
    "baseItem": "Serpentscale Boots",
    "dropLevel": 42,
    "act": 5
  },
  386:{
    "baseItem": "Hallowed Life Flask",
    "dropLevel": 42,
    "act": 5
  },
  387:{
    "baseItem": "Hallowed Mana Flask",
    "dropLevel": 42,
    "act": 5
  },
  388:{
    "baseItem": "Wrist Chopper",
    "dropLevel": 42,
    "act": 5
  },
  389:{
    "baseItem": "Enameled Buckler",
    "dropLevel": 42,
    "act": 5
  },
  390:{
    "baseItem": "Crusader Chainmail",
    "dropLevel": 43,
    "act": 5
  },
  391:{
    "baseItem": "Tiger's Paw",
    "dropLevel": 43,
    "act": 5
  },
  392:{
    "baseItem": "Zealot Gloves",
    "dropLevel": 43,
    "act": 5
  },
  393:{
    "baseItem": "Serpentscale Gauntlets",
    "dropLevel": 43,
    "act": 5
  },
  394:{
    "baseItem": "Fencer Helm",
    "dropLevel": 43,
    "act": 5
  },
  395:{
    "baseItem": "Mahogany Tower Shield",
    "dropLevel": 43,
    "act": 5
  },
  396:{
    "baseItem": "Estoc",
    "dropLevel": 43,
    "act": 5
  },
  397:{
    "baseItem": "Sleek Coat",
    "dropLevel": 44,
    "act": 5
  },
  398:{
    "baseItem": "Sharkskin Boots",
    "dropLevel": 44,
    "act": 5
  },
  399:{
    "baseItem": "Samite Slippers",
    "dropLevel": 44,
    "act": 5
  },
  400:{
    "baseItem": "Sniper Bow",
    "dropLevel": 44,
    "act": 5
  },
  401:{
    "baseItem": "Zealot Helmet",
    "dropLevel": 44,
    "act": 5
  },
  402:{
    "baseItem": "Battle Hammer",
    "dropLevel": 44,
    "act": 5
  },
  403:{
    "baseItem": "Battle Sword",
    "dropLevel": 44,
    "act": 5
  },
  404:{
    "baseItem": "Boot Blade",
    "dropLevel": 44,
    "act": 5
  },
  405:{
    "baseItem": "Lead Sceptre",
    "dropLevel": 44,
    "act": 5
  },
  406:{
    "baseItem": "Steelhead",
    "dropLevel": 44,
    "act": 5
  },
  407:{
    "baseItem": "Highland Blade",
    "dropLevel": 44,
    "act": 5
  },
  408:{
    "baseItem": "Sun Plate",
    "dropLevel": 45,
    "act": 6
  },
  409:{
    "baseItem": "Glorious Leather",
    "dropLevel": 45,
    "act": 6
  },
  410:{
    "baseItem": "Conjurer's Vestment",
    "dropLevel": 45,
    "act": 6
  },
  411:{
    "baseItem": "Sharkskin Gloves",
    "dropLevel": 45,
    "act": 6
  },
  412:{
    "baseItem": "Ambush Mitts",
    "dropLevel": 45,
    "act": 6
  },
  413:{
    "baseItem": "Callous Mask",
    "dropLevel": 45,
    "act": 6
  },
  414:{
    "baseItem": "War Axe",
    "dropLevel": 45,
    "act": 6
  },
  415:{
    "baseItem": "Blazing Arrow Quiver",
    "dropLevel": 45,
    "act": 6
  },
  416:{
    "baseItem": "Unset Ring",
    "dropLevel": 45,
    "act": 6
  },
  417:{
    "baseItem": "Ancient Spirit Shield",
    "dropLevel": 45,
    "act": 6
  },
  418:{
    "baseItem": "Spiked Round Shield",
    "dropLevel": 45,
    "act": 6
  },
  419:{
    "baseItem": "Compound Spiked Shield",
    "dropLevel": 45,
    "act": 6
  },
  420:{
    "baseItem": "Quarterstaff",
    "dropLevel": 45,
    "act": 6
  },
  421:{
    "baseItem": "Headsman Axe",
    "dropLevel": 45,
    "act": 6
  },
  422:{
    "baseItem": "Crystal Wand",
    "dropLevel": 45,
    "act": 6
  },
  423:{
    "baseItem": "Full Wyrmscale",
    "dropLevel": 46,
    "act": 6
  },
  424:{
    "baseItem": "Ancient Greaves",
    "dropLevel": 46,
    "act": 6
  },
  425:{
    "baseItem": "Gut Ripper",
    "dropLevel": 46,
    "act": 6
  },
  426:{
    "baseItem": "Corrugated Buckler",
    "dropLevel": 46,
    "act": 6
  },
  427:{
    "baseItem": "Steel Kite Shield",
    "dropLevel": 46,
    "act": 6
  },
  428:{
    "baseItem": "Serrated Foil",
    "dropLevel": 46,
    "act": 6
  },
  429:{
    "baseItem": "Ornate Ringmail",
    "dropLevel": 47,
    "act": 6
  },
  430:{
    "baseItem": "Ambush Boots",
    "dropLevel": 47,
    "act": 6
  },
  431:{
    "baseItem": "Ivory Bow",
    "dropLevel": 47,
    "act": 6
  },
  432:{
    "baseItem": "Samite Gloves",
    "dropLevel": 47,
    "act": 6
  },
  433:{
    "baseItem": "Ancient Gauntlets",
    "dropLevel": 47,
    "act": 6
  },
  434:{
    "baseItem": "Noble Tricorne",
    "dropLevel": 47,
    "act": 6
  },
  435:{
    "baseItem": "Flanged Mace",
    "dropLevel": 47,
    "act": 6
  },
  436:{
    "baseItem": "Elder Sword",
    "dropLevel": 47,
    "act": 6
  },
  437:{
    "baseItem": "Golden Kris",
    "dropLevel": 47,
    "act": 6
  },
  438:{
    "baseItem": "Blood Sceptre",
    "dropLevel": 47,
    "act": 6
  },
  439:{
    "baseItem": "Bronze Tower Shield",
    "dropLevel": 47,
    "act": 6
  },
  440:{
    "baseItem": "Crimson Raiment",
    "dropLevel": 48,
    "act": 6
  },
  441:{
    "baseItem": "Steel Circlet",
    "dropLevel": 48,
    "act": 6
  },
  442:{
    "baseItem": "Siege Helmet",
    "dropLevel": 48,
    "act": 6
  },
  443:{
    "baseItem": "Chest Splitter",
    "dropLevel": 48,
    "act": 6
  },
  444:{
    "baseItem": "Spiny Maul",
    "dropLevel": 48,
    "act": 6
  },
  445:{
    "baseItem": "Engraved Greatsword",
    "dropLevel": 48,
    "act": 6
  },
  446:{
    "baseItem": "Spidersilk Robe",
    "dropLevel": 49,
    "act": 6
  },
  447:{
    "baseItem": "Coronal Leather",
    "dropLevel": 49,
    "act": 6
  },
  448:{
    "baseItem": "Colosseum Plate",
    "dropLevel": 49,
    "act": 6
  },
  449:{
    "baseItem": "Soldier Boots",
    "dropLevel": 49,
    "act": 6
  },
  450:{
    "baseItem": "Prehistoric Claw",
    "dropLevel": 49,
    "act": 6
  },
  451:{
    "baseItem": "Wyrmscale Gauntlets",
    "dropLevel": 49,
    "act": 6
  },
  452:{
    "baseItem": "Broadhead Arrow Quiver",
    "dropLevel": 49,
    "act": 6
  },
  453:{
    "baseItem": "Chiming Spirit Shield",
    "dropLevel": 49,
    "act": 6
  },
  454:{
    "baseItem": "Crimson Round Shield",
    "dropLevel": 49,
    "act": 6
  },
  455:{
    "baseItem": "Polished Spiked Shield",
    "dropLevel": 49,
    "act": 6
  },
  456:{
    "baseItem": "Primeval Rapier",
    "dropLevel": 49,
    "act": 6
  },
  457:{
    "baseItem": "Labrys",
    "dropLevel": 49,
    "act": 6
  },
  458:{
    "baseItem": "Coiled Wand",
    "dropLevel": 49,
    "act": 6
  },
  459:{
    "baseItem": "Serpentine Staff",
    "dropLevel": 49,
    "act": 6
  },
  460:{
    "baseItem": "Commander's Brigandine",
    "dropLevel": 50,
    "act": 7
  },
  461:{
    "baseItem": "Highborn Bow",
    "dropLevel": 50,
    "act": 7
  },
  462:{
    "baseItem": "Carnal Mitts",
    "dropLevel": 50,
    "act": 7
  },
  463:{
    "baseItem": "Sacred Hybrid Flask",
    "dropLevel": 50,
    "act": 7
  },
  464:{
    "baseItem": "Sanctified Life Flask",
    "dropLevel": 50,
    "act": 7
  },
  465:{
    "baseItem": "Sanctified Mana Flask",
    "dropLevel": 50,
    "act": 7
  },
  466:{
    "baseItem": "Ornate Mace",
    "dropLevel": 50,
    "act": 7
  },
  467:{
    "baseItem": "Graceful Sword",
    "dropLevel": 50,
    "act": 7
  },
  468:{
    "baseItem": "Royal Skean",
    "dropLevel": 50,
    "act": 7
  },
  469:{
    "baseItem": "Royal Sceptre",
    "dropLevel": 50,
    "act": 7
  },
  470:{
    "baseItem": "Laminated Kite Shield",
    "dropLevel": 50,
    "act": 7
  },
  471:{
    "baseItem": "Battle Buckler",
    "dropLevel": 50,
    "act": 7
  },
  472:{
    "baseItem": "Convening Wand",
    "dropLevel": 50,
    "act": 7
  },
  473:{
    "baseItem": "Chain Hauberk",
    "dropLevel": 51,
    "act": 7
  },
  474:{
    "baseItem": "Wyrmscale Boots",
    "dropLevel": 51,
    "act": 7
  },
  475:{
    "baseItem": "Trisula",
    "dropLevel": 51,
    "act": 7
  },
  476:{
    "baseItem": "Soldier Gloves",
    "dropLevel": 51,
    "act": 7
  },
  477:{
    "baseItem": "Lacquered Helmet",
    "dropLevel": 51,
    "act": 7
  },
  478:{
    "baseItem": "Ceremonial Axe",
    "dropLevel": 51,
    "act": 7
  },
  479:{
    "baseItem": "Girded Tower Shield",
    "dropLevel": 51,
    "act": 7
  },
  480:{
    "baseItem": "Plated Maul",
    "dropLevel": 51,
    "act": 7
  },
  481:{
    "baseItem": "Tiger Sword",
    "dropLevel": 51,
    "act": 7
  },
  482:{
    "baseItem": "Lacquered Garb",
    "dropLevel": 52,
    "act": 7
  },
  483:{
    "baseItem": "Noble Claw",
    "dropLevel": 52,
    "act": 7
  },
  484:{
    "baseItem": "Regicide Mask",
    "dropLevel": 52,
    "act": 7
  },
  485:{
    "baseItem": "Highborn Staff",
    "dropLevel": 52,
    "act": 7
  },
  486:{
    "baseItem": "Fancy Foil",
    "dropLevel": 52,
    "act": 7
  },
  487:{
    "baseItem": "Noble Axe",
    "dropLevel": 52,
    "act": 7
  },
  488:{
    "baseItem": "Destroyer Regalia",
    "dropLevel": 53,
    "act": 7
  },
  489:{
    "baseItem": "Majestic Plate",
    "dropLevel": 53,
    "act": 7
  },
  490:{
    "baseItem": "Cutthroat's Garb",
    "dropLevel": 53,
    "act": 7
  },
  491:{
    "baseItem": "Conjurer Boots",
    "dropLevel": 53,
    "act": 7
  },
  492:{
    "baseItem": "Decimation Bow",
    "dropLevel": 53,
    "act": 7
  },
  493:{
    "baseItem": "Goliath Gauntlets",
    "dropLevel": 53,
    "act": 7
  },
  494:{
    "baseItem": "Great Crown",
    "dropLevel": 53,
    "act": 7
  },
  495:{
    "baseItem": "Phantom Mace",
    "dropLevel": 53,
    "act": 7
  },
  496:{
    "baseItem": "Twilight Blade",
    "dropLevel": 53,
    "act": 7
  },
  497:{
    "baseItem": "Fiend Dagger",
    "dropLevel": 53,
    "act": 7
  },
  498:{
    "baseItem": "Abyssal Sceptre",
    "dropLevel": 53,
    "act": 7
  },
  499:{
    "baseItem": "Thorium Spirit Shield",
    "dropLevel": 53,
    "act": 7
  },
  500:{
    "baseItem": "Omen Wand",
    "dropLevel": 53,
    "act": 7
  },
  501:{
    "baseItem": "Battle Lamellar",
    "dropLevel": 54,
    "act": 8
  },
  502:{
    "baseItem": "Goliath Greaves",
    "dropLevel": 54,
    "act": 8
  },
  503:{
    "baseItem": "Shagreen Gloves",
    "dropLevel": 54,
    "act": 8
  },
  504:{
    "baseItem": "Necromancer Circlet",
    "dropLevel": 54,
    "act": 8
  },
  505:{
    "baseItem": "Wraith Axe",
    "dropLevel": 54,
    "act": 8
  },
  506:{
    "baseItem": "Golden Buckler",
    "dropLevel": 54,
    "act": 8
  },
  507:{
    "baseItem": "Baroque Round Shield",
    "dropLevel": 54,
    "act": 8
  },
  508:{
    "baseItem": "Sovereign Spiked Shield",
    "dropLevel": 54,
    "act": 8
  },
  509:{
    "baseItem": "Dread Maul",
    "dropLevel": 54,
    "act": 8
  },
  510:{
    "baseItem": "Wraith Sword",
    "dropLevel": 54,
    "act": 8
  },
  511:{
    "baseItem": "Devout Chainmail",
    "dropLevel": 55,
    "act": 8
  },
  512:{
    "baseItem": "Shagreen Boots",
    "dropLevel": 55,
    "act": 8
  },
  513:{
    "baseItem": "Carnal Boots",
    "dropLevel": 55,
    "act": 8
  },
  514:{
    "baseItem": "Eagle Claw",
    "dropLevel": 55,
    "act": 8
  },
  515:{
    "baseItem": "Conjurer Gloves",
    "dropLevel": 55,
    "act": 8
  },
  516:{
    "baseItem": "Samnite Helmet",
    "dropLevel": 55,
    "act": 8
  },
  517:{
    "baseItem": "Ursine Pelt",
    "dropLevel": 55,
    "act": 8
  },
  518:{
    "baseItem": "Dragon Mace",
    "dropLevel": 55,
    "act": 8
  },
  519:{
    "baseItem": "Grappler",
    "dropLevel": 55,
    "act": 8
  },
  520:{
    "baseItem": "Vile Arrow Quiver",
    "dropLevel": 55,
    "act": 8
  },
  521:{
    "baseItem": "Stag Sceptre",
    "dropLevel": 55,
    "act": 8
  },
  522:{
    "baseItem": "Angelic Kite Shield",
    "dropLevel": 55,
    "act": 8
  },
  523:{
    "baseItem": "Crested Tower Shield",
    "dropLevel": 55,
    "act": 8
  },
  524:{
    "baseItem": "Apex Rapier",
    "dropLevel": 55,
    "act": 8
  },
  525:{
    "baseItem": "Abyssal Axe",
    "dropLevel": 55,
    "act": 8
  },
  526:{
    "baseItem": "Heathen Wand",
    "dropLevel": 55,
    "act": 8
  },
  527:{
    "baseItem": "Foul Staff",
    "dropLevel": 55,
    "act": 8
  },
  528:{
    "baseItem": "Savant's Robe",
    "dropLevel": 56,
    "act": 8
  },
  529:{
    "baseItem": "Golden Plate",
    "dropLevel": 56,
    "act": 8
  },
  530:{
    "baseItem": "Sharkskin Tunic",
    "dropLevel": 56,
    "act": 8
  },
  531:{
    "baseItem": "Crypt Armour",
    "dropLevel": 56,
    "act": 8
  },
  532:{
    "baseItem": "Thicket Bow",
    "dropLevel": 56,
    "act": 8
  },
  533:{
    "baseItem": "Gutting Knife",
    "dropLevel": 56,
    "act": 8
  },
  534:{
    "baseItem": "Engraved Hatchet",
    "dropLevel": 56,
    "act": 8
  },
  535:{
    "baseItem": "Ancestral Club",
    "dropLevel": 56,
    "act": 8
  },
  536:{
    "baseItem": "Gemstone Sword",
    "dropLevel": 56,
    "act": 8
  },
  537:{
    "baseItem": "Karui Sceptre",
    "dropLevel": 56,
    "act": 8
  },
  538:{
    "baseItem": "Lacewood Spirit Shield",
    "dropLevel": 56,
    "act": 8
  },
  539:{
    "baseItem": "Solar Maul",
    "dropLevel": 56,
    "act": 8
  },
  540:{
    "baseItem": "Lithe Blade",
    "dropLevel": 56,
    "act": 8
  },
  541:{
    "baseItem": "Demon's Horn",
    "dropLevel": 56,
    "act": 8
  },
  542:{
    "baseItem": "Dragonscale Doublet",
    "dropLevel": 57,
    "act": 8
  },
  543:{
    "baseItem": "Steelwood Bow",
    "dropLevel": 57,
    "act": 8
  },
  544:{
    "baseItem": "Twin Claw",
    "dropLevel": 57,
    "act": 8
  },
  545:{
    "baseItem": "Legion Gloves",
    "dropLevel": 57,
    "act": 8
  },
  546:{
    "baseItem": "Harlequin Mask",
    "dropLevel": 57,
    "act": 8
  },
  547:{
    "baseItem": "Karui Axe",
    "dropLevel": 57,
    "act": 8
  },
  548:{
    "baseItem": "Ironwood Buckler",
    "dropLevel": 57,
    "act": 8
  },
  549:{
    "baseItem": "Moon Staff",
    "dropLevel": 57,
    "act": 8
  },
  550:{
    "baseItem": "Courtesan Sword",
    "dropLevel": 57,
    "act": 8
  },
  551:{
    "baseItem": "Karui Maul",
    "dropLevel": 57,
    "act": 8
  },
  552:{
    "baseItem": "Headman's Sword",
    "dropLevel": 57,
    "act": 8
  },
  553:{
    "baseItem": "Loricated Ringmail",
    "dropLevel": 58,
    "act": 8
  },
  554:{
    "baseItem": "Legion Boots",
    "dropLevel": 58,
    "act": 8
  },
  555:{
    "baseItem": "Citadel Bow",
    "dropLevel": 58,
    "act": 8
  },
  556:{
    "baseItem": "Great White Claw",
    "dropLevel": 58,
    "act": 8
  },
  557:{
    "baseItem": "Assassin's Mitts",
    "dropLevel": 58,
    "act": 8
  },
  558:{
    "baseItem": "Fluted Bascinet",
    "dropLevel": 58,
    "act": 8
  },
  559:{
    "baseItem": "Magistrate Crown",
    "dropLevel": 58,
    "act": 8
  },
  560:{
    "baseItem": "Tenderizer",
    "dropLevel": 58,
    "act": 8
  },
  561:{
    "baseItem": "Corsair Sword",
    "dropLevel": 58,
    "act": 8
  },
  562:{
    "baseItem": "Slaughter Knife",
    "dropLevel": 58,
    "act": 8
  },
  563:{
    "baseItem": "Tyrant's Sekhem",
    "dropLevel": 58,
    "act": 8
  },
  564:{
    "baseItem": "Shagreen Tower Shield",
    "dropLevel": 58,
    "act": 8
  },
  565:{
    "baseItem": "Teak Round Shield",
    "dropLevel": 58,
    "act": 8
  },
  566:{
    "baseItem": "Alder Spiked Shield",
    "dropLevel": 58,
    "act": 8
  },
  567:{
    "baseItem": "Primordial Staff",
    "dropLevel": 58,
    "act": 8
  },
  568:{
    "baseItem": "Dragonbone Rapier",
    "dropLevel": 58,
    "act": 8
  },
  569:{
    "baseItem": "Karui Chopper",
    "dropLevel": 58,
    "act": 8
  },
  570:{
    "baseItem": "Necromancer Silks",
    "dropLevel": 59,
    "act": 8
  },
  571:{
    "baseItem": "Crusader Plate",
    "dropLevel": 59,
    "act": 8
  },
  572:{
    "baseItem": "Destiny Leather",
    "dropLevel": 59,
    "act": 8
  },
  573:{
    "baseItem": "Sentinel Jacket",
    "dropLevel": 59,
    "act": 8
  },
  574:{
    "baseItem": "Hydrascale Boots",
    "dropLevel": 59,
    "act": 8
  },
  575:{
    "baseItem": "Hydrascale Gauntlets",
    "dropLevel": 59,
    "act": 8
  },
  576:{
    "baseItem": "Solaris Circlet",
    "dropLevel": 59,
    "act": 8
  },
  577:{
    "baseItem": "Siege Axe",
    "dropLevel": 59,
    "act": 8
  },
  578:{
    "baseItem": "Fossilised Spirit Shield",
    "dropLevel": 59,
    "act": 8
  },
  579:{
    "baseItem": "Branded Kite Shield",
    "dropLevel": 59,
    "act": 8
  },
  580:{
    "baseItem": "Talon Axe",
    "dropLevel": 59,
    "act": 8
  },
  581:{
    "baseItem": "Colossus Mallet",
    "dropLevel": 59,
    "act": 8
  },
  582:{
    "baseItem": "Reaver Sword",
    "dropLevel": 59,
    "act": 8
  },
  583:{
    "baseItem": "Imbued Wand",
    "dropLevel": 59,
    "act": 8
  },
  584:{
    "baseItem": "Desert Brigandine",
    "dropLevel": 60,
    "act": 9
  },
  585:{
    "baseItem": "Ranger Bow",
    "dropLevel": 60,
    "act": 9
  },
  586:{
    "baseItem": "Throat Stabber",
    "dropLevel": 60,
    "act": 9
  },
  587:{
    "baseItem": "Ambusher",
    "dropLevel": 60,
    "act": 9
  },
  588:{
    "baseItem": "Arcanist Gloves",
    "dropLevel": 60,
    "act": 9
  },
  589:{
    "baseItem": "Silken Hood",
    "dropLevel": 60,
    "act": 9
  },
  590:{
    "baseItem": "Ezomyte Burgonet",
    "dropLevel": 60,
    "act": 9
  },
  591:{
    "baseItem": "Hallowed Hybrid Flask",
    "dropLevel": 60,
    "act": 9
  },
  592:{
    "baseItem": "Divine Life Flask",
    "dropLevel": 60,
    "act": 9
  },
  593:{
    "baseItem": "Divine Mana Flask",
    "dropLevel": 60,
    "act": 9
  },
  594:{
    "baseItem": "Gavel",
    "dropLevel": 60,
    "act": 9
  },
  595:{
    "baseItem": "Gladius",
    "dropLevel": 60,
    "act": 9
  },
  596:{
    "baseItem": "Opal Sceptre",
    "dropLevel": 60,
    "act": 9
  },
  597:{
    "baseItem": "Lacquered Buckler",
    "dropLevel": 60,
    "act": 9
  },
  598:{
    "baseItem": "Tempered Foil",
    "dropLevel": 60,
    "act": 9
  },
  599:{
    "baseItem": "Sundering Axe",
    "dropLevel": 60,
    "act": 9
  },
  600:{
    "baseItem": "Ezomyte Staff",
    "dropLevel": 60,
    "act": 9
  },
  601:{
    "baseItem": "Conquest Chainmail",
    "dropLevel": 61,
    "act": 9
  },
  602:{
    "baseItem": "Arcanist Slippers",
    "dropLevel": 61,
    "act": 9
  },
  603:{
    "baseItem": "Reaver Axe",
    "dropLevel": 61,
    "act": 9
  },
  604:{
    "baseItem": "Heavy Arrow Quiver",
    "dropLevel": 61,
    "act": 9
  },
  605:{
    "baseItem": "Ebony Tower Shield",
    "dropLevel": 61,
    "act": 9
  },
  606:{
    "baseItem": "Piledriver",
    "dropLevel": 61,
    "act": 9
  },
  607:{
    "baseItem": "Ezomyte Blade",
    "dropLevel": 61,
    "act": 9
  },
  608:{
    "baseItem": "Astral Plate",
    "dropLevel": 62,
    "act": 9
  },
  609:{
    "baseItem": "Exquisite Leather",
    "dropLevel": 62,
    "act": 9
  },
  610:{
    "baseItem": "Varnished Coat",
    "dropLevel": 62,
    "act": 9
  },
  611:{
    "baseItem": "Occultist's Vestment",
    "dropLevel": 62,
    "act": 9
  },
  612:{
    "baseItem": "Vaal Greaves",
    "dropLevel": 62,
    "act": 9
  },
  613:{
    "baseItem": "Stealth Boots",
    "dropLevel": 62,
    "act": 9
  },
  614:{
    "baseItem": "Assassin Bow",
    "dropLevel": 62,
    "act": 9
  },
  615:{
    "baseItem": "Hellion's Paw",
    "dropLevel": 62,
    "act": 9
  },
  616:{
    "baseItem": "Stealth Gloves",
    "dropLevel": 62,
    "act": 9
  },
  617:{
    "baseItem": "Vaal Mask",
    "dropLevel": 62,
    "act": 9
  },
  618:{
    "baseItem": "Legion Hammer",
    "dropLevel": 62,
    "act": 9
  },
  619:{
    "baseItem": "Legion Sword",
    "dropLevel": 62,
    "act": 9
  },
  620:{
    "baseItem": "Ezomyte Dagger",
    "dropLevel": 62,
    "act": 9
  },
  621:{
    "baseItem": "Platinum Sceptre",
    "dropLevel": 62,
    "act": 9
  },
  622:{
    "baseItem": "Spiny Round Shield",
    "dropLevel": 62,
    "act": 9
  },
  623:{
    "baseItem": "Vaal Spirit Shield",
    "dropLevel": 62,
    "act": 9
  },
  624:{
    "baseItem": "Ezomyte Spiked Shield",
    "dropLevel": 62,
    "act": 9
  },
  625:{
    "baseItem": "Champion Kite Shield",
    "dropLevel": 62,
    "act": 9
  },
  626:{
    "baseItem": "Lathi",
    "dropLevel": 62,
    "act": 9
  },
  627:{
    "baseItem": "Pecoraro",
    "dropLevel": 62,
    "act": 9
  },
  628:{
    "baseItem": "Ezomyte Axe",
    "dropLevel": 62,
    "act": 9
  },
  629:{
    "baseItem": "Opal Wand",
    "dropLevel": 62,
    "act": 9
  },
  630:{
    "baseItem": "Full Dragonscale",
    "dropLevel": 63,
    "act": 9
  },
  631:{
    "baseItem": "Assassin's Boots",
    "dropLevel": 63,
    "act": 9
  },
  632:{
    "baseItem": "Vaal Gauntlets",
    "dropLevel": 63,
    "act": 9
  },
  633:{
    "baseItem": "Prophet Crown",
    "dropLevel": 63,
    "act": 9
  },
  634:{
    "baseItem": "Pig-Faced Bascinet",
    "dropLevel": 63,
    "act": 9
  },
  635:{
    "baseItem": "Butcher Axe",
    "dropLevel": 63,
    "act": 9
  },
  636:{
    "baseItem": "Vaal Buckler",
    "dropLevel": 63,
    "act": 9
  },
  637:{
    "baseItem": "Meatgrinder",
    "dropLevel": 63,
    "act": 9
  },
  638:{
    "baseItem": "Vaal Greatsword",
    "dropLevel": 63,
    "act": 9
  },
  639:{
    "baseItem": "Elegant Ringmail",
    "dropLevel": 64,
    "act": 10
  },
  640:{
    "baseItem": "Elegant Ringmail",
    "dropLevel": 64,
    "act": 10
  },
  641:{
    "baseItem": "Crusader Boots",
    "dropLevel": 64,
    "act": 10
  },
  642:{
    "baseItem": "Spine Bow",
    "dropLevel": 64,
    "act": 10
  },
  643:{
    "baseItem": "Eye Gouger",
    "dropLevel": 64,
    "act": 10
  },
  644:{
    "baseItem": "Sinner Tricorne",
    "dropLevel": 64,
    "act": 10
  },
  645:{
    "baseItem": "Pernach",
    "dropLevel": 64,
    "act": 10
  },
  646:{
    "baseItem": "Vaal Blade",
    "dropLevel": 64,
    "act": 10
  },
  647:{
    "baseItem": "Platinum Kris",
    "dropLevel": 64,
    "act": 10
  },
  648:{
    "baseItem": "Vaal Sceptre",
    "dropLevel": 64,
    "act": 10
  },
  649:{
    "baseItem": "Ezomyte Tower Shield",
    "dropLevel": 64,
    "act": 10
  },
  650:{
    "baseItem": "Spiraled Foil",
    "dropLevel": 64,
    "act": 10
  },
  651:{
    "baseItem": "Vaal Axe",
    "dropLevel": 64,
    "act": 10
  },
  652:{
    "baseItem": "Maelström Staff",
    "dropLevel": 64,
    "act": 10
  },
  653:{
    "baseItem": "Zodiac Leather",
    "dropLevel": 65,
    "act": 10
  },
  654:{
    "baseItem": "Widowsilk Robe",
    "dropLevel": 65,
    "act": 10
  },
  655:{
    "baseItem": "Gladiator Plate",
    "dropLevel": 65,
    "act": 10
  },
  656:{
    "baseItem": "Blood Raiment",
    "dropLevel": 65,
    "act": 10
  },
  657:{
    "baseItem": "Dragonscale Boots",
    "dropLevel": 65,
    "act": 10
  },
  658:{
    "baseItem": "Mind Cage",
    "dropLevel": 65,
    "act": 10
  },
  659:{
    "baseItem": "Royal Burgonet",
    "dropLevel": 65,
    "act": 10
  },
  660:{
    "baseItem": "Eternal Life Flask",
    "dropLevel": 65,
    "act": 10
  },
  661:{
    "baseItem": "Eternal Mana Flask",
    "dropLevel": 65,
    "act": 10
  },
  662:{
    "baseItem": "Vaal Hatchet",
    "dropLevel": 65,
    "act": 10
  },
  663:{
    "baseItem": "Harmonic Spirit Shield",
    "dropLevel": 65,
    "act": 10
  },
  664:{
    "baseItem": "Mosaic Kite Shield",
    "dropLevel": 65,
    "act": 10
  },
  665:{
    "baseItem": "Imperial Maul",
    "dropLevel": 65,
    "act": 10
  },
  666:{
    "baseItem": "Lion Sword",
    "dropLevel": 65,
    "act": 10
  },
  667:{
    "baseItem": "Tornado Wand",
    "dropLevel": 65,
    "act": 10
  },
  668:{
    "baseItem": "General's Brigandine",
    "dropLevel": 66,
    "act": 10
  },
  669:{
    "baseItem": "Imperial Bow",
    "dropLevel": 66,
    "act": 10
  },
  670:{
    "baseItem": "Vaal Claw",
    "dropLevel": 66,
    "act": 10
  },
  671:{
    "baseItem": "Crusader Gloves",
    "dropLevel": 66,
    "act": 10
  },
  672:{
    "baseItem": "Auric Mace",
    "dropLevel": 66,
    "act": 10
  },
  673:{
    "baseItem": "Eternal Sword",
    "dropLevel": 66,
    "act": 10
  },
  674:{
    "baseItem": "Primal Arrow Quiver",
    "dropLevel": 66,
    "act": 10
  },
  675:{
    "baseItem": "Imperial Skean",
    "dropLevel": 66,
    "act": 10
  },
  676:{
    "baseItem": "Carnal Sceptre",
    "dropLevel": 66,
    "act": 10
  },
  677:{
    "baseItem": "Mirrored Spiked Shield",
    "dropLevel": 66,
    "act": 10
  },
  678:{
    "baseItem": "Crusader Buckler",
    "dropLevel": 66,
    "act": 10
  },
  679:{
    "baseItem": "Cardinal Round Shield",
    "dropLevel": 66,
    "act": 10
  },
  680:{
    "baseItem": "Imperial Staff",
    "dropLevel": 66,
    "act": 10
  },
  681:{
    "baseItem": "Vaal Rapier",
    "dropLevel": 66,
    "act": 10
  },
  682:{
    "baseItem": "Despot Axe",
    "dropLevel": 66,
    "act": 10
  },
  683:{
    "baseItem": "Saint's Hauberk",
    "dropLevel": 67,
    "act": "11"
  },
  684:{
    "baseItem": "Sorcerer Boots",
    "dropLevel": 67,
    "act": "11"
  },
  685:{
    "baseItem": "Dragonscale Gauntlets",
    "dropLevel": 67,
    "act": "11"
  },
  686:{
    "baseItem": "Murder Mitts",
    "dropLevel": 67,
    "act": "11"
  },
  687:{
    "baseItem": "Nightmare Bascinet",
    "dropLevel": 67,
    "act": "11"
  },
  688:{
    "baseItem": "Deicide Mask",
    "dropLevel": 67,
    "act": "11"
  },
  689:{
    "baseItem": "Royal Axe",
    "dropLevel": 67,
    "act": "11"
  },
  690:{
    "baseItem": "Colossal Tower Shield",
    "dropLevel": 67,
    "act": "11"
  },
  691:{
    "baseItem": "Terror Maul",
    "dropLevel": 67,
    "act": "11"
  },
  692:{
    "baseItem": "Infernal Sword",
    "dropLevel": 67,
    "act": "11"
  },
  693:{
    "baseItem": "Vaal Regalia",
    "dropLevel": 68,
    "act": "11"
  },
  694:{
    "baseItem": "Assassin's Garb",
    "dropLevel": 68,
    "act": "11"
  },
  695:{
    "baseItem": "Sadist Garb",
    "dropLevel": 68,
    "act": "11"
  },
  696:{
    "baseItem": "Glorious Plate",
    "dropLevel": 68,
    "act": "11"
  },
  697:{
    "baseItem": "Titan Greaves",
    "dropLevel": 68,
    "act": "11"
  },
  698:{
    "baseItem": "Harbinger Bow",
    "dropLevel": 68,
    "act": "11"
  },
  699:{
    "baseItem": "Imperial Claw",
    "dropLevel": 68,
    "act": "11"
  },
  700:{
    "baseItem": "Praetor Crown",
    "dropLevel": 68,
    "act": "11"
  },
  701:{
    "baseItem": "Nightmare Mace",
    "dropLevel": 68,
    "act": "11"
  },
  702:{
    "baseItem": "Midnight Blade",
    "dropLevel": 68,
    "act": "11"
  },
  703:{
    "baseItem": "Demon Dagger",
    "dropLevel": 68,
    "act": "11"
  },
  704:{
    "baseItem": "Void Sceptre",
    "dropLevel": 68,
    "act": "11"
  },
  705:{
    "baseItem": "Titanium Spirit Shield",
    "dropLevel": 68,
    "act": "11"
  },
  706:{
    "baseItem": "Archon Kite Shield",
    "dropLevel": 68,
    "act": "11"
  },
  707:{
    "baseItem": "Jewelled Foil",
    "dropLevel": 68,
    "act": "11"
  },
  708:{
    "baseItem": "Void Axe",
    "dropLevel": 68,
    "act": "11"
  },
  709:{
    "baseItem": "Prophecy Wand",
    "dropLevel": 68,
    "act": "11"
  },
  710:{
    "baseItem": "Judgement Staff",
    "dropLevel": 68,
    "act": "11"
  },
  711:{
    "baseItem": "Triumphant Lamellar",
    "dropLevel": 69,
    "act": "11"
  },
  712:{
    "baseItem": "Slink Boots",
    "dropLevel": 69,
    "act": "11"
  },
  713:{
    "baseItem": "Murder Boots",
    "dropLevel": 69,
    "act": "11"
  },
  714:{
    "baseItem": "Sorcerer Gloves",
    "dropLevel": 69,
    "act": "11"
  },
  715:{
    "baseItem": "Titan Gauntlets",
    "dropLevel": 69,
    "act": "11"
  },
  716:{
    "baseItem": "Hubris Circlet",
    "dropLevel": 69,
    "act": "11"
  },
  717:{
    "baseItem": "Eternal Burgonet",
    "dropLevel": 69,
    "act": "11"
  },
  718:{
    "baseItem": "Infernal Axe",
    "dropLevel": 69,
    "act": "11"
  },
  719:{
    "baseItem": "Imperial Buckler",
    "dropLevel": 69,
    "act": "11"
  },
  720:{
    "baseItem": "Coronal Maul",
    "dropLevel": 69,
    "act": "11"
  },
  721:{
    "baseItem": "Saintly Chainmail",
    "dropLevel": 70,
    "act": "11"
  },
  722:{
    "baseItem": "Two-Toned Boots",
    "dropLevel": 70,
    "act": "11"
  },
  723:{
    "baseItem": "Two-Toned Boots",
    "dropLevel": 70,
    "act": "11"
  },
  724:{
    "baseItem": "Two-Toned Boots",
    "dropLevel": 70,
    "act": "11"
  },
  725:{
    "baseItem": "Fugitive Boots",
    "dropLevel": 70,
    "act": "11"
  },
  726:{
    "baseItem": "Terror Claw",
    "dropLevel": 70,
    "act": "11"
  },
  727:{
    "baseItem": "Sai",
    "dropLevel": 70,
    "act": "11"
  },
  728:{
    "baseItem": "Apothecary's Gloves",
    "dropLevel": 70,
    "act": "11"
  },
  729:{
    "baseItem": "Spiked Gloves",
    "dropLevel": 70,
    "act": "11"
  },
  730:{
    "baseItem": "Slink Gloves",
    "dropLevel": 70,
    "act": "11"
  },
  731:{
    "baseItem": "Gripped Gloves",
    "dropLevel": 70,
    "act": "11"
  },
  732:{
    "baseItem": "Fingerless Silk Gloves",
    "dropLevel": 70,
    "act": "11"
  },
  733:{
    "baseItem": "Lion Pelt",
    "dropLevel": 70,
    "act": "11"
  },
  734:{
    "baseItem": "Behemoth Mace",
    "dropLevel": 70,
    "act": "11"
  },
  735:{
    "baseItem": "Tiger Hook",
    "dropLevel": 70,
    "act": "11"
  },
  736:{
    "baseItem": "Sambar Sceptre",
    "dropLevel": 70,
    "act": "11"
  },
  737:{
    "baseItem": "Elegant Round Shield",
    "dropLevel": 70,
    "act": "11"
  },
  738:{
    "baseItem": "Pinnacle Tower Shield",
    "dropLevel": 70,
    "act": "11"
  },
  739:{
    "baseItem": "Supreme Spiked Shield",
    "dropLevel": 70,
    "act": "11"
  },
  740:{
    "baseItem": "Eclipse Staff",
    "dropLevel": 70,
    "act": "11"
  },
  741:{
    "baseItem": "Harpy Rapier",
    "dropLevel": 70,
    "act": "11"
  },
  742:{
    "baseItem": "Fleshripper",
    "dropLevel": 70,
    "act": "11"
  },
  743:{
    "baseItem": "Fleshripper",
    "dropLevel": 70,
    "act": "11"
  },
  744:{
    "baseItem": "Exquisite Blade",
    "dropLevel": 70,
    "act": "11"
  },
  745:{
    "baseItem": "Profane Wand",
    "dropLevel": 70,
    "act": "11"
  },
  746:{
    "baseItem": "Carnal Armour",
    "dropLevel": 71,
    "act": "11"
  },
  747:{
    "baseItem": "Maraketh Bow",
    "dropLevel": 71,
    "act": "11"
  },
  748:{
    "baseItem": "Runic Hatchet",
    "dropLevel": 71,
    "act": "11"
  },
  749:{
    "baseItem": "Gemini Claw",
    "dropLevel": 72,
    "act": "11"
  },
  750:{
    "baseItem": "Dragoon Sword",
    "dropLevel": 72,
    "act": "11"
  },
  751:{
    "baseItem": "Convoking Wand",
    "dropLevel": 72,
    "act": "11"
  },
  752:{
    "baseItem": "Crystal Belt",
    "dropLevel": 73,
    "act": "11"
  },
  753:{
    "baseItem": "Vanguard Belt",
    "dropLevel": 73,
    "act": "11"
  },
  754:{
    "baseItem": "Full Wyvernscale",
    "dropLevel": 73,
    "act": "11"
  },
  755:{
    "baseItem": "Titan Plate",
    "dropLevel": 73,
    "act": "11"
  },
  756:{
    "baseItem": "Grand Ringmail",
    "dropLevel": 73,
    "act": "11"
  },
  757:{
    "baseItem": "Arcane Vestment",
    "dropLevel": 73,
    "act": "11"
  },
  758:{
    "baseItem": "Supreme Leather",
    "dropLevel": 73,
    "act": "11"
  },
  759:{
    "baseItem": "Sanguine Raiment",
    "dropLevel": 73,
    "act": "11"
  },
  760:{
    "baseItem": "Jester Mask",
    "dropLevel": 73,
    "act": "11"
  },
  761:{
    "baseItem": "General's Helmet",
    "dropLevel": 73,
    "act": "11"
  },
  762:{
    "baseItem": "Bone Helmet",
    "dropLevel": 73,
    "act": "11"
  },
  763:{
    "baseItem": "Faithful Helmet",
    "dropLevel": 73,
    "act": "11"
  },
  764:{
    "baseItem": "Moonlit Circlet",
    "dropLevel": 73,
    "act": "11"
  },
  765:{
    "baseItem": "Dire Pelt",
    "dropLevel": 73,
    "act": "11"
  },
  766:{
    "baseItem": "Knight Helm",
    "dropLevel": 73,
    "act": "11"
  },
  767:{
    "baseItem": "Marble Amulet",
    "dropLevel": 74,
    "act": "11"
  },
  768:{
    "baseItem": "Seaglass Amulet",
    "dropLevel": 74,
    "act": "11"
  },
  769:{
    "baseItem": "Artillery Quiver",
    "dropLevel": 74,
    "act": "11"
  },
  770:{
    "baseItem": "Blue Pearl Amulet",
    "dropLevel": 77,
    "act": "11"
  },
  771:{
    "baseItem": "Paladin's Hauberk",
    "dropLevel": 78,
    "act": "11"
  },
  772:{
    "baseItem": "Marshall's Brigandine",
    "dropLevel": 78,
    "act": "11"
  },
  773:{
    "baseItem": "Torturer Garb",
    "dropLevel": 78,
    "act": "11"
  },
  774:{
    "baseItem": "Nightweave Robe",
    "dropLevel": 78,
    "act": "11"
  },
  775:{
    "baseItem": "Astral Leather",
    "dropLevel": 78,
    "act": "11"
  },
  776:{
    "baseItem": "Legion Plate",
    "dropLevel": 78,
    "act": "11"
  },
  777:{
    "baseItem": "Chimerascale Boots",
    "dropLevel": 78,
    "act": "11"
  },
  778:{
    "baseItem": "Martyr Boots",
    "dropLevel": 78,
    "act": "11"
  },
  779:{
    "baseItem": "Infiltrator Boots",
    "dropLevel": 78,
    "act": "11"
  },
  780:{
    "baseItem": "Sage Slippers",
    "dropLevel": 78,
    "act": "11"
  },
  781:{
    "baseItem": "Harpyskin Boots",
    "dropLevel": 78,
    "act": "11"
  },
  782:{
    "baseItem": "Precursor Greaves",
    "dropLevel": 78,
    "act": "11"
  },
  783:{
    "baseItem": "Chimerascale Gauntlets",
    "dropLevel": 78,
    "act": "11"
  },
  784:{
    "baseItem": "Martyr Gloves",
    "dropLevel": 78,
    "act": "11"
  },
  785:{
    "baseItem": "Sage Gloves",
    "dropLevel": 78,
    "act": "11"
  },
  786:{
    "baseItem": "Infiltrator Mitts",
    "dropLevel": 78,
    "act": "11"
  },
  787:{
    "baseItem": "Harpyskin Gloves",
    "dropLevel": 78,
    "act": "11"
  },
  788:{
    "baseItem": "Precursor Gauntlets",
    "dropLevel": 78,
    "act": "11"
  },
  789:{
    "baseItem": "Conqueror's Helmet",
    "dropLevel": 78,
    "act": "11"
  },
  790:{
    "baseItem": "Conquest Helmet",
    "dropLevel": 78,
    "act": "11"
  },
  791:{
    "baseItem": "Paladin Crown",
    "dropLevel": 78,
    "act": "11"
  },
  792:{
    "baseItem": "Sunfire Circlet",
    "dropLevel": 78,
    "act": "11"
  },
  793:{
    "baseItem": "Grizzly Pelt",
    "dropLevel": 78,
    "act": "11"
  },
  794:{
    "baseItem": "Ancient Mask",
    "dropLevel": 78,
    "act": "11"
  },
  795:{
    "baseItem": "Iolite Ring",
    "dropLevel": 78,
    "act": "11"
  },
  796:{
    "baseItem": "Opal Ring",
    "dropLevel": 78,
    "act": "11"
  },
  797:{
    "baseItem": "Steel Ring",
    "dropLevel": 78,
    "act": "11"
  },
  798:{
    "baseItem": "Cerulean Ring",
    "dropLevel": 80,
    "act": "11"
  },
  799:{
    "baseItem": "Vermillion Ring",
    "dropLevel": 80,
    "act": "11"
  },
  800:{
    "baseItem": "Conquest Lamellar",
    "dropLevel": 84,
    "act": "11"
  },
  801:{
    "baseItem": "Syndicate's Garb",
    "dropLevel": 84,
    "act": "11"
  },
  802:{
    "baseItem": "Twilight Regalia",
    "dropLevel": 84,
    "act": "11"
  },
  803:{
    "baseItem": "Royal Plate",
    "dropLevel": 84,
    "act": "11"
  },
  804:{
    "baseItem": "Necrotic Armour",
    "dropLevel": 84,
    "act": "11"
  },
  805:{
    "baseItem": "Sacred Chainmail",
    "dropLevel": 84,
    "act": "11"
  },
  806:{
    "baseItem": "Paladin Boots",
    "dropLevel": 84,
    "act": "11"
  },
  807:{
    "baseItem": "Wyvernscale Boots",
    "dropLevel": 84,
    "act": "11"
  },
  808:{
    "baseItem": "Phantom Boots",
    "dropLevel": 84,
    "act": "11"
  },
  809:{
    "baseItem": "Velour Boots",
    "dropLevel": 84,
    "act": "11"
  },
  810:{
    "baseItem": "Warlock Boots",
    "dropLevel": 84,
    "act": "11"
  },
  811:{
    "baseItem": "Leviathan Greaves",
    "dropLevel": 84,
    "act": "11"
  },
  812:{
    "baseItem": "Paladin Gloves",
    "dropLevel": 84,
    "act": "11"
  },
  813:{
    "baseItem": "Wyvernscale Gauntlets",
    "dropLevel": 84,
    "act": "11"
  },
  814:{
    "baseItem": "Phantom Mitts",
    "dropLevel": 84,
    "act": "11"
  },
  815:{
    "baseItem": "Velour Gloves",
    "dropLevel": 84,
    "act": "11"
  },
  816:{
    "baseItem": "Warlock Gloves",
    "dropLevel": 84,
    "act": "11"
  },
  817:{
    "baseItem": "Leviathan Gauntlets",
    "dropLevel": 84,
    "act": "11"
  },
  818:{
    "baseItem": "Divine Crown",
    "dropLevel": 84,
    "act": "11"
  },
  819:{
    "baseItem": "Torturer's Mask",
    "dropLevel": 84,
    "act": "11"
  },
  820:{
    "baseItem": "Giantslayer Helmet",
    "dropLevel": 84,
    "act": "11"
  },
  821:{
    "baseItem": "Majestic Pelt",
    "dropLevel": 84,
    "act": "11"
  },
  822:{
    "baseItem": "Haunted Bascinet",
    "dropLevel": 84,
    "act": "11"
  },
  823:{
    "baseItem": "Lich's Circlet",
    "dropLevel": 84,
    "act": "11"
  }
}