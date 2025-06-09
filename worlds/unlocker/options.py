from dataclasses import dataclass
from Options import OptionList, PerGameCommonOptions

class ItemList(OptionList):
    """Comma-separated list of items to unlock in this game."""
    display_name = "Items to unlock"
    default = ["Item 1", "Item 2", "Item 3"]

@dataclass
class UnlockerOptions(PerGameCommonOptions):
    item_list: ItemList