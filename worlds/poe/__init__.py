import os
from worlds.LauncherComponents import components, Component, launch_subprocess, Type, icon_paths
from BaseClasses import Region, MultiWorld, Item, Location, LocationProgressType, ItemClassification
from worlds.AutoWorld import World, WebWorld
from Utils import visualize_regions
import yaml
import logging

from .Options import PathOfExileOptions
import Items
import Locations
import Regions


# ----- Configure the POE client ----- #
logger = logging.getLogger("poe")

def launch_client():
    from . import Client
    launch_subprocess(Client.launch, name="poeClient", )

components.append(Component("Path of Exile Client",
                            func=launch_client,
                            component_type=Type.CLIENT,
                            icon="poe"))

icon_paths["poe"] = f"ap:{__name__}/icons/poeicon.png"

# ----- PathOfExile Web World ----- #

class PathOfExileWebWorld(WebWorld):
    """
    Web interface for the Path of Exile world.
    This class can be extended to include specific web functionalities.
    """
    theme = "stone"
    bug_report_page = "https://github.com/stubobis1/Archipelago/issues" # if anyone else wants to maintain this, please do so

# ----- PathOfExile World ----- #


class PathOfExileWorld(World):
    """
    Represents the Path of Exile world in Archipelago.
    This class can be extended to include specific world properties and methods.
    """
    _debug = True
    game = "Path of Exile"
    web_world_class = PathOfExileWebWorld
    options_dataclass = PathOfExileOptions

    #generate the location and item tables from Locations.py and Items.py
    location_name_to_id = { loc.name: loc.id for loc in Locations.base_item_types }
    item_name_to_id = { item.name: item.id for item in Items.item_table }

    def fill_slot_data(self):
        options: PathOfExileOptions = self.options
        # make a table of item id to location name
        client_options = {
            "gucciHobo" : options.gucci_hobo_mode.value,
            "ttsSpeed" : options.tts_speed.value,
            "ttsVolume" : options.tts_volume.value,

        }
        return {
            client_options: client_options,
        }

    def generate_early(self):
        options: PathOfExileOptions = self.options
        if options.starting_character.value == options.starting_character.option_random:
            options.starting_character.value = self.random.choice(
                [options.starting_character.option_marauder,
                 options.starting_character.option_ranger,
                 options.starting_character.option_witch,
                 options.starting_character.option_duelist,
                 options.starting_character.option_templar,
                 options.starting_character.option_shadow,
                 options.starting_character.option_scion])
        
        if options.gear_unlocks.value == False:
            gear_upgrades = Items.get_gear_items()
            for item in gear_upgrades:
                item_id = self.item_name_to_id[item.name]
                item_obj = Item(item.name, item_id, self.player, classification=ItemClassification.progression)
                self.multiworld.push_precollected(item_obj)

        if options.flask_slot_upgrades.value == False:
            flask_slots = Items.get_flask_items()
            for item in flask_slots:
                item_id = self.item_name_to_id[item.name]
                item_obj = Item(item.name, item_id, self.player, classification=ItemClassification.progression)
                self.multiworld.push_precollected(item_obj)
                    
        if options.support_gem_slot_upgrades.value == False:
            support_gem_slots = Items.get_support_gem_items()
            for item in support_gem_slots:
                item_id = self.item_name_to_id[item.name]
                item_obj = Item(item.name, item_id, self.player, classification=ItemClassification.progression)
                self.multiworld.push_precollected(item_obj)
                
                
        if options.starting_character.value == options.starting_character.option_scion:
            item_id = self.item_name_to_id["Scion"]
            item_obj = Item("Scion", item_id, self.player, classification=ItemClassification.progression)
            self.multiworld.push_precollected(item_obj)

        if options.starting_character.value == options.starting_character.option_marauder:
            item_id = self.item_name_to_id["Marauder"]
            item_obj = Item("Marauder", item_id, self.player, classification=ItemClassification.progression)
            self.multiworld.push_precollected(item_obj)

        if options.starting_character.value == options.starting_character.option_duelist:
            item_id = self.item_name_to_id["Duelist"]
            item_obj = Item("Duelist", item_id, self.player, classification=ItemClassification.progression)
            self.multiworld.push_precollected(item_obj)
            
        if options.starting_character.value == options.starting_character.option_ranger:
            item_id = self.item_name_to_id["Ranger"]
            item_obj = Item("Ranger", item_id, self.player, classification=ItemClassification.progression)
            self.multiworld.push_precollected(item_obj)

        if options.starting_character.value == options.starting_character.option_shadow:
            item_id = self.item_name_to_id["Shadow"]
            item_obj = Item("Shadow", item_id, self.player, classification=ItemClassification.progression)
            self.multiworld.push_precollected(item_obj)
            
        if options.starting_character.value == options.starting_character.option_witch:
            item_id = self.item_name_to_id["Witch"]
            item_obj = Item("Witch", item_id, self.player, classification=ItemClassification.progression)
            self.multiworld.push_precollected(item_obj)

        if options.starting_character.value == options.starting_character.option_templar:
            item_id = self.item_name_to_id["Templar"]
            item_obj = Item("Templar", item_id, self.player, classification=ItemClassification.progression)
            self.multiworld.push_precollected(item_obj)


        self.origin_region_name = "menu"

    
    def generate_output(self, output_directory: str):
        if self._debug:
            logger.debug(f"Generating output for {self.game} in {output_directory}")
            visualize_regions(self.multiworld.get_region(self.origin_region_name, self.player), f"Player{self.player}.puml",
                            show_entrance_names=True,
                            regions_to_highlight=self.multiworld.get_all_state(self.player).reachable_regions[
                                self.player])