from dataclasses import dataclass
from Options import OptionList, PerGameCommonOptions, Toggle, DefaultOnToggle


class ItemList(OptionList):
    """Comma-separated list of items to unlock in this game."""
    display_name = "Items to unlock"
    default = ["Item 1", "Item 2", "Item 3"]

class OnlyAllowOtherGamesItems(DefaultOnToggle):
    """If enabled, only items from other games will be used. if false, items from any unlocker game can also be used."""
    display_name = "Only allow items from other games"
    description = "If enabled, only items from other games will be used."


# maybe have a separate option for progression items vs non-progression items?
# maybe have an option for if unlocker will allow any unlocker items to be used in generation?

@dataclass
class UnlockerOptions(PerGameCommonOptions):
    item_list: ItemList
    only_allow_other_games_items: OnlyAllowOtherGamesItems