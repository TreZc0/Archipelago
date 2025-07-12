from ast import Set
import os
from typing import Dict
from worlds.LauncherComponents import components, Component, launch_subprocess, Type, icon_paths
from BaseClasses import Region, MultiWorld, Item, Location, LocationProgressType, ItemClassification
from worlds.AutoWorld import World, WebWorld
from Utils import visualize_regions
import yaml
import logging

from .Options import PathOfExileOptions
from . import Items
from . import Locations
from . import Regions as poeRegions


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
    origin_region_name = "Menu"

    items_to_place = {}
    locations_to_place = {}
    
    #generate the location and item tables from Locations.py and Items.py
    location_name_to_id = { loc.name: loc.id for loc in Locations.base_item_types }
    item_name_to_id = { item.name: item.id for item in Items.item_table }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.items_to_place = Items.item_table.copy()
        self.locations_to_place = Locations.base_item_types.copy()

    def remove_and_create_item_by_dict(self, item: Items.ItemDict) -> Item:
        item_id = self.item_name_to_id[item.name]
        item_to_place = self.items_to_place.pop(item_id)  # Remove from items to place
        item_obj = Item(item_to_place.name, item_id, self.player, classification=ItemClassification.progression)
        return item_obj

    def remove_and_create_item_by_name(self, item_name: str) -> Item:
        item_id = self.item_name_to_id[item_name]
        item_to_place = self.items_to_place.pop(item_id)  # Remove from items to place
        item_obj = Item(item_to_place.name, item_id, self.player, classification=ItemClassification.progression)
        return item_obj
    
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
            gear_upgrades = Items.get_gear_items(table=self.items_to_place)
            for item in gear_upgrades:
                item_obj = self.remove_and_create_item_by_dict(item)
                self.multiworld.push_precollected(item_obj)

        if options.flask_slot_upgrades.value == False:
            flask_slots = Items.get_flask_items(table=self.items_to_place)
            for item in flask_slots:
                item_obj = self.remove_and_create_item_by_dict(item)
                self.multiworld.push_precollected(item_obj)
                    
        if options.support_gem_slot_upgrades.value == False:
            support_gem_slots = Items.get_max_links_items(table=self.items_to_place)
            for item in support_gem_slots:
                item_obj = self.remove_and_create_item_by_dict(item)
                self.multiworld.push_precollected(item_obj)
                
                
        if options.starting_character.value == options.starting_character.option_scion:
            item_obj = self.remove_and_create_item_by_name("Scion")
            self.multiworld.push_precollected(item_obj)

        if options.starting_character.value == options.starting_character.option_marauder:
            item_obj = self.remove_and_create_item_by_name("Marauder")
            self.multiworld.push_precollected(item_obj)

        if options.starting_character.value == options.starting_character.option_duelist:
            item_obj = self.remove_and_create_item_by_name("Duelist")
            self.multiworld.push_precollected(item_obj)
            
        if options.starting_character.value == options.starting_character.option_ranger:
            item_obj = self.remove_and_create_item_by_name("Ranger")
            self.multiworld.push_precollected(item_obj)

        if options.starting_character.value == options.starting_character.option_shadow:
            item_obj = self.remove_and_create_item_by_name("Shadow")
            self.multiworld.push_precollected(item_obj)
            
        if options.starting_character.value == options.starting_character.option_witch:
            item_obj = self.remove_and_create_item_by_name("Witch")
            self.multiworld.push_precollected(item_obj)

        if options.starting_character.value == options.starting_character.option_templar:
            item_obj = self.remove_and_create_item_by_name("Templar")
            self.multiworld.push_precollected(item_obj)

        


    def create_regions(self):
        """Create the regions for the Path of Exile world.
        This method initializes the regions based on the acts defined in Regions.py.
        """
        options: PathOfExileOptions = self.options

        temp_items_to_place = {}
        # add ascendancy items.
        for item in range(0, options.ascendancies_available_per_class.value):
            for char_class in ["Marauder", "Ranger", "Witch", "Duelist", "Templar", "Shadow", "Scion"]:
                item: Items.ItemDict = self.random.choice(Items.get_ascendancy_class_items(char_class + " Class", table=self.items_to_place))
                temp_items_to_place[item.id] = item

        # remove all the other ascendancy items

        for item in Items.get_ascendancy_items(table=self.items_to_place):
            item_id = self.item_name_to_id[item.name]
            self.items_to_place.pop(item_id, None)
            
        # add the temp items to place back to the items to place
        for item_id, item_obj in temp_items_to_place.items():
            self.items_to_place[item_id] = item_obj

        if options.allow_unlock_of_other_characters.value == False : 
            for item in Items.get_character_class_items(table=self.items_to_place):
                for ascendancy in Items.get_ascendancy_class_items(item.name + " Class", table=self.items_to_place):
                    item_id = self.item_name_to_id[ascendancy.name]
                    self.items_to_place.pop(item_id, None)
                item_id = self.item_name_to_id[item.name]
                self.items_to_place.pop(item_id, None)

        # get the length of items_to_place
        items_to_place_length = len(self.items_to_place)
        # and only use the first `items_to_place_length` items of the Locations.base_item_types
        locations_to_place = Locations.base_item_types[:items_to_place_length]

        poeRegions.create_and_populate_regions(self, self.multiworld, self.player, locations_to_place, poeRegions.acts)

        
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
        
        
    def generate_output(self, output_directory: str):
        if self._debug:
            logger.debug(f"Generating output for {self.game} in {output_directory}")
            visualize_regions(self.multiworld.get_region(self.origin_region_name, self.player), f"Player{self.player}.puml",
                            show_entrance_names=True,
                            regions_to_highlight=self.multiworld.get_all_state(self.player).reachable_regions[
                                self.player])



