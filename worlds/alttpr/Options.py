from dataclasses import dataclass
from enum import Enum

from Options import PerGameCommonOptions, Range, TextChoice, Toggle


class WorldMode(TextChoice):
    """Open: Start from Link's House or Sanctuary, without needing to save Zelda in Hyrule Castle
    Standard: Start at Link's House and save Zelda in Hyrule Castle before accessing the rest of the world
    Inverted: The Light World and Dark World have been flipped.
        - Link starts at their house (swapped with the Bomb Shop) or Dark Sanctuary
        - All Dark World portals now take you to the Light World
        - Link is a bunny in the Light World unless you have the Moon Pearl
        - Agahnim's Tower and Ganon's Tower have swapped places. Agahnim's Tower now requires crystals to enter
        - Ganon is hiding in a new hole on top of Hyrule Castle
        - The Magic Mirror takes you from the Light World to the Dark World
        - The Flute must be activated in Kakariko Village, but will then take you to locations across the Dark World
        - Light World terrain has been modified so that mirror-locked locations can be reached without the mirror
        - The top of Turtle Rock can be accessed by jumping from its tail"""
    display_name = "World Mode"
    option_open = "open"
    option_standard = "standard"
    option_inverted = "inverted"
    # option_retro = "retro"
    default = "open"


class Goal(TextChoice):
    """Sets the goal for this seed.

    crystals: Collect the required number of crystals and kill Ganon
    triforcehunt: Collect the required number of pieces of the Triforce, then talk to Murahdahla outside Hyrule Castle"""
    display_name = "Goal"
    option_crystals = "crystals"
    option_ganon = "ganon"
    # option_dungeons = "dungeons"
    # option_pedestal = "pedestal"
    option_triforcehunt = "triforcehunt"
    # option_ganonhunt = "ganonhunt"
    # option_trinity = "trinity"
    # option_completionist = "completionist"
    default = "crystals"


class OpenPyramid(TextChoice):
    """ Whether the Pyramid hole leading to Ganon should be open at the start. Choosing "auto" will open or close it based on your goal setting."""
    display_name = "Open Pyramid"
    option_auto = "auto"
    option_open = "yes"
    option_closed = "no"
    default = "auto"


class CrystalsNeededForGanon(Range):
    """How many crystals are needed before Ganon can be killed"""
    display_name = "Crystals Needed for Ganon"
    range_start = 0
    range_end = 7
    default = 7


class TriforceHuntGoal(Range):
    """How many Triforce Pieces are required to beat the game when the goal is set to Triforce Hunt or Ganon Hunt"""
    display_name = "Triforce Hunt Goal"
    range_start = 1
    range_end = 50  # TODO: What should the max number of triforce pieces be?
    default = 20


class TriforceHuntTotal(Range):
    """How many Triforce Pieces are in the item pool when the goal is set to Triforce Hunt or Ganon Hunt"""
    display_name = "Triforce Hunt Total"
    range_start = 1
    range_end = 50
    default = 30


class MapShuffle(Toggle):
    """Maps can now appear outside of their dungeon. The map screen will not show if a dungeon gives a pendant or crystal until its map has been found."""
    display_name = "Map Shuffle"


class CompassShuffle(Toggle):
    """Compasses can now appear outside of their dungeon."""
    display_name = "Compass Shuffle"


class SmallKeyShuffle(Toggle):
    """Small keys can now appear outside of their dungeon."""
    display_name = "Small Key Shuffle"


class BigKeyShuffle(Toggle):
    """Big keys can now appear outside of their dungeon."""
    display_name = "Big Key Shuffle"


class EntranceShuffle(TextChoice):
    """Randomize where each building, cave, and dungeon entrance leads to."""
    display_name = "Entrance Shuffle"
    option_vanilla = "vanilla"
    option_crossed = "crossed"
    default = "vanilla"
    # TODO: Entrance shuffles other than vanilla and crossed


class Zelgawoods(Toggle):
    """If entrance shuffle is enabled, add Skull Woods entrances and dropdowns to the entrance shuffle. The main Skull Woods entrance/big chest
    dropdown and the second Skull Woods entrance/the dropdown in the back are both added to the dropdown pool. The other two dropdowns in the
    front are vanilla, and at least one of the entrances in the back of the Skull Woods area must be a connector."""
    # TODO: If I have a good link to the image description a picture is better than text descriptions
    display_name = "Zelgawoods"


class EnemyShuffle(TextChoice):
    """All enemies except bosses are randomized. Logical enemy shuffle might require defeating enemies that
    require specific items (Eyegore, Freezors, etc.) to progress in a dungeon."""
    display_name = "Enemy Shuffle"
    option_vanilla = "none"
    option_shuffled = "random"
    option_logical = "logical"
    default = "none"


class BossShuffle(TextChoice):
    """Bosses are randomized. This includes the Armos/Lanmolas/Moldorm rematches in Ganon's Tower, but not Ganon or either Aganhim fight. Some bosses cannot appear in some locations.

    * Vanilla: Bosses are in their original locations.
    * Simple: Bosses are shuffled randomly. Armos Knights, Lanmolas, and Moldorm will be fought twice.
    * Full: Bosses are shuffled randomly, and three random bosses will be fought twice.
    * Chaos: Bosses are shuffled randomly, and any boss can be fought any number of times."""
    display_name = "Boss Shuffle"
    option_vanilla = "none"
    option_simple = "simple"
    option_full = "full"
    option_chaos = "random"
    default = "none"


class Pseudoboots(Toggle):
    """Psuedoboots give Link the ability to dash like Pegasus Boots, but they cannot bonk rocks, open King's Tomb, knock items off torches/the Library, or clear small gaps"""
    display_name = "Pseudoboots"


class MirrorScroll(Toggle):
    """Mirror Scroll is an inventory item that warps Link to the start of their current dungeon, and is replaced upon finding the Magic Mirror"""
    display_name = "Mirror Scroll"


@dataclass
class ALttPROptions(PerGameCommonOptions):
    world_mode: WorldMode
    goal: Goal
    open_pyramid: OpenPyramid
    crystals_needed_for_ganon: CrystalsNeededForGanon
    triforce_hunt_goal: TriforceHuntGoal
    triforce_hunt_total: TriforceHuntTotal
    map_shuffle: MapShuffle
    compass_shuffle: CompassShuffle
    small_key_shuffle: SmallKeyShuffle
    big_key_shuffle: BigKeyShuffle
    entrance_shuffle: EntranceShuffle
    zelgawoods: Zelgawoods
    enemy_shuffle: EnemyShuffle
    boss_shuffle: BossShuffle
    pseudoboots: Pseudoboots
    mirror_scroll: MirrorScroll
