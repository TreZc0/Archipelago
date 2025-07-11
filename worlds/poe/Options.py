from dataclasses import dataclass, fields, Field
from typing import FrozenSet, Union, Set

from Options import Choice, Toggle, DefaultOnToggle, ItemSet, OptionSet, Range, PerGameCommonOptions
from worlds.AutoWorld import World



class GearUpgrades(Choice):
    """
    Specifies if gear should be restricted to a certain rarity, unlockable through items found in the multiworld.
    """
    display_name = "Gear Unlocks"
    NoRestrictionOnAnyGear = 0
    NoRestrictionOnUniqueGear = 1
    UnlockableRestrictionOnAllGear = 2
    default = 2

class FlaskSlotUpgrades(Toggle):
    """
    Specifies if the number of flask slots should be restricted, unlockable through items found in the multiworld.
    """
    display_name = "Flask Slot Upgrades"
    default = True

class SupportGemSlotUpgrades(Toggle):
    """
    Specifies if the number support gem slots should be restricted, unlockable through items found in the multiworld.
    """
    display_name = "Support Gem Slot Upgrades"
    default = True

class GucciHoboMode(Toggle):
    """
    Specifies if the world should be in Gucci Hobo Mode, this restricts use of any non-unique equipment to only 1 slot.
    (this will probobly be very difficult to play with)
    """
    display_name = "Gucci Hobo Mode"
    default = False


class GearUpgradesPerAct(Range):
    """
    Specifies a minimum number of rarity of gear upgrades available per act. (there are 38 total)
    This will be ignored if the "Gear Upgrades" option is turned off.
    """
    display_name = "Gear Upgrades Per Act"
    range_start = 0
    range_end = 38
    default = 5


class FlaskSlotsPerAct(Range):
    """
    Specifies a minimum number of available flask slots per act. (there are 5 total)
    This will be ignored if the "Flask Slots" option is turned off.
    """
    display_name = "Flask Slots Per Act"
    range_start = 0
    range_end = 5
    default = 1

class SupportGemSlotsPerAct(Range):
    """
    Specifies a minimum number of available support gem slots per act. (there are 19 total)
    This will be ignored if the "Support Gem Slot Upgrades" option is turned off.
    """
    display_name = "Support Gem Slots Per Act"
    range_start = 0
    range_end = 19
    default = 2

class AscendanciesAvailablePerClass(Range):
    """
    Specifies the maximum number of available ascendancies per class.
    """
    display_name = "Ascendancies Available Per Class"
    range_start = 0
    range_end = 3
    default = 1

class AllowUnlockOfOtherCharacters(Toggle):
    """
    Allows unlocking of other characters.
    """
    display_name = "Allow Unlock of Other Characters"
    default = True

class StartingCharacter(Choice):
    """
    The starting character for the world. This will determine the class and ascendancy available.
     """
    display_name = "Starting Character"
    Random      = 0
    Marauder    = 1
    Ranger      = 2
    Witch       = 3
    Duelist     = 4
    Templar     = 5
    Shadow      = 6
    Scion       = 7
    default = 0

class EnableTTS(Choice):
    """
    Settings for the Text-to-Speech (TTS) feature.
    """
    display_name = "Text-to-Speech"
    Disabled     = 0
    Enabled_Saying_AP_Item = 1
    Enabled_Saying_Base_Item = 2
    default = 1

class TTSSpeed(Range):
    """
    Speed of the Text-to-Speech (TTS) feature.
    """
    display_name = "TTS Speed"
    range_start = 50
    range_end = 500
    default = 200
