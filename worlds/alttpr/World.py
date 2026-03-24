import base64
from collections.abc import Mapping
import logging
import os
import threading
import typing

# Imports of base Archipelago modules must be absolute.
from BaseClasses import ItemClassification
import settings
from worlds.AutoWorld import World
from worlds.Files import APProcedurePatch

# Imports of your world's files must be relative.
from .ALttPDoorRandomizer.BaseClasses import World as DoorRandoWorld  # Avoid naming conflict with AP's World class
from .ALttPDoorRandomizer.source.enemizer.DamageTables import DamageTable
from .ALttPDoorRandomizer.source.rom.DataTables import init_data_tables
from .ALttPDoorRandomizer.Doors import create_doors
from .ALttPDoorRandomizer.DoorShuffle import link_doors, link_doors_prep
from .ALttPDoorRandomizer.Dungeons import create_dungeons
from .ALttPDoorRandomizer.source.overworld.EntranceShuffle2 import link_entrances_new
from .ALttPDoorRandomizer.Fill import dungeon_tracking, fill_dungeons_restrictive, promote_dungeon_items
from .ALttPDoorRandomizer.source.item.FillUtil import create_item_pool_config, massage_item_pool
from .ALttPDoorRandomizer.ItemList import difficulties, fill_prizes, generate_itempool
from .ALttPDoorRandomizer.Items import ItemFactory
from .ALttPDoorRandomizer.OverworldShuffle import create_dynamic_exits, link_overworld
from .ALttPDoorRandomizer.Regions import adjust_locations, create_regions, create_dungeon_regions, create_shops, lookup_name_to_id
from .ALttPDoorRandomizer.Rom import apply_rom_settings, patch_rom
from .ALttPDoorRandomizer.RoomData import create_rooms
from .ALttPDoorRandomizer.Rules import set_rules
from .Client import ALttPRSNIClient
from . import Items, Regions, Rules
from . import Options as alttpr_options  # rename due to a name conflict with World.options
from .Rom import ALttPRRom, JAP10HASH


logger = logging.getLogger("alttpr")

class ALttPRSettings(settings.Group):
    class ALttPRRomFile(settings.SNESRomPath):
        """File name of the Japanese 1.0 ALttP ROM file"""
        description = "A Link to the Past Japanese 1.0 ROM File"
        copy_to = "Zelda no Densetsu - Kamigami no Triforce (Japan).sfc"
        md5s = [JAP10HASH]

    rom_file: ALttPRRomFile = ALttPRRomFile(ALttPRRomFile.copy_to)


class ALttPRWorld(World):
    """
    The Legend of Zelda: A Link to the Past is a good game.
    TODO: Better description here.
    """

    # IMO Zelda games should start with "The Legend of Zelda", but no one else does it.
    # Be the change you want to see.
    door_rando_world = None
    game = "The Legend of Zelda: A Link to the Past"
    rom_name = None

    options_dataclass = alttpr_options.ALttPROptions
    options: alttpr_options.ALttPROptions

    settings: typing.ClassVar[ALttPRSettings]

    # Our world class must have a static location_name_to_id and item_name_to_id defined.
    item_name_to_id = Items.item_name_to_id
    location_name_to_id = Regions.lookup_name_to_id
    item_name_groups = {
        "Bottles": {"Bottle", "Bottle (Green Potion)", "Bottle (Red Potion)", "Bottle (Blue Potion)", "Bottle (Bee)", "Bottle (Good Bee)", "Bottle (Fairy)"}
    }

    # There is always one region that the generator starts from & assumes you can always go back to.
    origin_region_name = "Menu"

    # We need to modify the multiworld to recognize the ALttPR ROM hash, but only after that ROM has finished generating
    finished_generating: threading.Event

    def generate_early(self) -> None:
        # TODO: Error check all of the options
        start_inventory = self.options.start_inventory.value.keys()
        if "Triforce Piece" in start_inventory or "Green Clock" in start_inventory:
            # TODO: What's the proper way to throw generation errors?
            # TODO: Should do something like "If any item in start_inventory isn't a valid item"
            raise Exception("ALttPR: There is an invalid item in the start_inventory.")

        # Have the Door Randomizer generate a world with all the locations, entrances, items, etc.
        # Items should not be placed except for not-fully-randomized stuff like dungeon items without keysanity,
        # or dungeon prizes. Otherwise let AP place all the items later.
        #
        # The world can create a multiworld with many players each with different options, but we only need to
        # generate for one player, hence all the "1"s everywhere.
        self.door_rando_world = DoorRandoWorld(
            1, {1: self.options.entrance_shuffle.value}, {1: "vanilla"}, {1: "noglitches"}, {1: self.options.world_mode.value},
            {1: "random"}, {1: "normal"}, {1: None}, "none", "on", {1: self.options.goal.value},
            "balanced", {1: "locations"}, {1: True}, False, Items.default_items_dict,
            {1: False}, "none"
        )

        # There are sooo many fields that aren't set in the
        # door rando's world constructor :(
        self.door_rando_world.bigkeyshuffle = {1: True if self.options.big_key_shuffle.value else False}
        self.door_rando_world.boots_hint = {1: False}
        self.door_rando_world.bow_mode = {1: "progressive"}
        self.door_rando_world.compassshuffle = {1: True if self.options.compass_shuffle.value else False}
        self.door_rando_world.crystals_needed_for_ganon = {1: self.options.crystals_needed_for_ganon.value}
        self.door_rando_world.customizer = None
        self.door_rando_world.dropshuffle = {1: "none"}
        self.door_rando_world.dungeon_counters = {1: "default"}
        self.door_rando_world.intensity = {1: 0}  # No door shuffle
        self.door_rando_world.keyshuffle = {1: "none" if not self.options.small_key_shuffle.value else "wild"}
        self.door_rando_world.linked_drops = {1: "unset"}  # In entrance shuffle, whether dropdowns link with their matching exit is determined by the entrance setting
        self.door_rando_world.mapshuffle = {1: True if self.options.map_shuffle.value else False}
        self.door_rando_world.mirrorscroll = {1: self.options.mirror_scroll.value}
        self.door_rando_world.open_pyramid = {1: self.options.open_pyramid.value}
        self.door_rando_world.overworld_map = {1: "default"}
        self.door_rando_world.pottery = {1: "none"}
        self.door_rando_world.pseudoboots = {1: self.options.pseudoboots.value}
        self.door_rando_world.rom_seeds = {1: self.random.randint(0, 999999999)}
        self.door_rando_world.shufflelinks = {1: False}
        self.door_rando_world.shuffletavern = {1: False}
        self.door_rando_world.skullwoods = {1: "followlinked" if self.options.zelgawoods.value else "original"}  # How to handle Skull Woods in entrance shuffle.
        self.door_rando_world.treasure_hunt_count = {1: self.options.triforce_hunt_goal.value}
        self.door_rando_world.treasure_hunt_total = {1: self.options.triforce_hunt_total.value}

        self.door_rando_world.player_names = {}
        for player_id, player_name in self.multiworld.player_name.items():
            self.door_rando_world.player_names[player_id] = {1: player_name}

        self.door_rando_world.finish_init()
        self.finished_generating = threading.Event()
        self.door_rando_world.difficulty_requirements = {1: difficulties[self.door_rando_world.difficulty[1]]}

        for item_name, item_count in self.options.start_inventory.value.items():
            classification = ItemClassification.filler
            if item_name in Items.progressive_items:
                classification = ItemClassification.progression
            elif item_name in Items.useful_items:
                classification = ItemClassification.useful

            for i in range(0, item_count):
                door_rando_item = ItemFactory(item_name, 1)
                self.door_rando_world.push_precollected(door_rando_item)
                self.multiworld.push_precollected(Items.create_item(self, item_name, classification))

        create_regions(self.door_rando_world, 1)
        create_dungeon_regions(self.door_rando_world, 1)
        create_shops(self.door_rando_world, 1)
        create_doors(self.door_rando_world, 1)
        create_rooms(self.door_rando_world, 1)  # Not sure if this is needed or what it does?
        create_dungeons(self.door_rando_world, 1)
        self.door_rando_world.damage_table[1] = DamageTable()
        self.door_rando_world.data_tables[1] = init_data_tables(self.door_rando_world, 1)
        adjust_locations(self.door_rando_world, 1)
        link_overworld(self.door_rando_world, 1)
        create_dynamic_exits(self.door_rando_world, 1)
        link_entrances_new(self.door_rando_world, 1)
        link_doors_prep(self.door_rando_world, 1)
        create_item_pool_config(self.door_rando_world)
        link_doors(self.door_rando_world, 1)
        generate_itempool(self.door_rando_world, 1)
        set_rules(self.door_rando_world, 1)
        dungeon_tracking(self.door_rando_world)
        massage_item_pool(self.door_rando_world)
        fill_prizes(self.door_rando_world)
        shuffled_locations = self.door_rando_world.get_unfilled_locations()
        self.random.shuffle(shuffled_locations)  # Make sure we use AP's random() features so that it generates consistently. TODO: the random() calls inside DR don't do that.
        fill_dungeons_restrictive(self.door_rando_world, shuffled_locations)


    def create_regions(self) -> None:
        Regions.create_and_connect_regions(self)


    def set_rules(self) -> None:
        Rules.set_all_rules(self)


    def create_items(self) -> None:
        Items.create_all_items(self)


    def pre_fill(self) -> None:
        Items.place_pre_fill_items(self)


    # Our world class must also have a create_item function that can create any one of our items by name at any time.
    def create_item(self, name: str, classification: ItemClassification = ItemClassification.filler) -> Items.ALttPRItem:
        return Items.create_item(self, name, classification)


    # For features such as item links and panic-method start inventory, AP may ask your world to create extra filler.
    # The way it does this is by calling get_filler_item_name.
    # For this purpose, your world *must* have at least one infinitely repeatable item (usually filler).
    # You must override this function and return this infinitely repeatable item's name.
    # In our case, we defined a function called get_random_filler_item_name for this purpose in our items.py.
    def get_filler_item_name(self) -> str:
        return Items.get_random_filler_item_name(self)


    def generate_output(self, output_directory: str) -> None:
        for location in self.multiworld.get_filled_locations(self.player):
            if location.item.player == self.player:
                # TODO: Key drop
                if location.is_event or "Key Drop" in location.name or "Pot Key" in location.name:
                    continue
                dr_location = self.door_rando_world.get_location(location.name, 1)
                if dr_location.item is not None:
                    # This is a prefilled location, probably a dungeon item
                    continue

                dr_item_name = location.item.name if location.item.name not in Items.dr_ap_different_names else Items.dr_ap_different_names[location.item.name]
                dr_items = [item for item in self.door_rando_world.get_items() if item.name == dr_item_name and item.location is None]
                dr_item = dr_items[0] if dr_items else None
                if dr_item is None:
                    logger.error(f"Could not find item {location.item.name} in door rando itempool.")
                    raise Exception()
            else:
                # Using the green/blue/red clocks as placeholders for AP items.
                # TODO: Edit the base ROM to add AP items and matching sprites
                if location.item.classification & ItemClassification.progression:
                    dr_item = ItemFactory("Green Clock", 1)
                elif location.item.classification & ItemClassification.useful:
                    dr_item = ItemFactory("Blue Clock", 1)
                else:
                    dr_item = ItemFactory("Red Clock", 1)

            self.door_rando_world.push_item(self.door_rando_world.get_location(location.name, 1), dr_item, collect=False)

        rom = ALttPRRom(self.player, self.player_name)
        try:
            patch_rom(self.door_rando_world, rom, 1, 1, is_mystery=False)
        except RuntimeError as e:
            # TODO: We're in bad shape if this happens, because it still runs generate_output
            # But raising the exception freezes AP. Not sure what to do about errors in generate_output?
            logger.error(f"Unknown error occurred while patching the ALttPR ROM: {e}")

        self.apply_player_settings(rom)  # Change settings which don't affect logic, like quickswapping
        rom.write(os.path.join(output_directory, f"{self.multiworld.get_out_file_name_base(self.player)}.apalttpr"))
        self.rom_name = rom.name
        self.finished_generating.set()


    def apply_player_settings(self, rom):
        # TODO: Player settings like heart color, heart beep rate, and palette swap
        heart_beep_rate = "half"
        heart_color = "red"
        quickswap = True
        fast_menu = "normal"
        disable_music = False
        sprite = None
        ow_palettes = "default"
        uw_palettes = "default"
        reduce_flashing = True
        shuffle_sfx = False
        msu_resume = True

        apply_rom_settings(rom, heart_beep_rate, heart_color, quickswap,
                           fast_menu, disable_music, sprite,
                           ow_palettes, uw_palettes, reduce_flashing,
                           shuffle_sfx, msu_resume)


    def modify_multidata(self, multidata: dict):
        self.finished_generating.wait()
        if self.rom_name:
            # SNIClient connects to the AP server using an encoded ROM filename, instead of the player's name, for some reason.
            # This tells the AP server to associate the ROM filename with our player's name.
            new_name = base64.b64encode(bytes(self.rom_name)).decode()
            multidata["connect_names"][new_name] = multidata["connect_names"][self.multiworld.player_name[self.player]]
        else:
            logger.error("ROM name is not set, cannot make needed multiworld changes in modify_multidata()")