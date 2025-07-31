from ast import Set
import os
from typing import Dict
from worlds.LauncherComponents import components, Component, launch_subprocess, Type, icon_paths
from BaseClasses import Region, MultiWorld, Item, Location, LocationProgressType, ItemClassification
from worlds.AutoWorld import World, WebWorld
from Utils import visualize_regions
import yaml
import logging
import base64

from worlds.poe.data import ItemTable

from .Options import PathOfExileOptions
from . import Items
from . import Locations
from . import Regions as poeRegions
from . import Rules as poeRules

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
    items_procollected = {}
    locations_to_place = {}
    total_items_count = 0
    
    goal_act = 0
    #generate the location and item tables from Locations.py and Items.py
    # location_name_to_id = { loc.name: loc.id for loc in Locations.base_item_types }
    location_name_to_id = { loc["name"]: id for id, loc in Locations.full_locations.items() }
    item_name_to_id = { item["name"]: item["id"] for item in Items.item_table.values() }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.items_to_place = Items.item_table.copy()

    def remove_and_create_item_by_itemdict(self, item: Items.ItemDict) -> list[Items.PathOfExileItem]:
        item_id = item["id"]
        item_to_place = self.items_to_place.pop(item_id)  # Remove from items to place
        item_objs = []
        count = item.get("count", 1)
        for i in range(count):
            item_obj = Items.PathOfExileItem(item_to_place["name"], ItemClassification.progression, item_id, self.player)
            item_objs.append(item_obj)
        return item_objs

    def remove_and_create_item_by_name(self, item_name: str) -> Item:
        item_id = self.item_name_to_id[item_name]
        item_to_place = self.items_to_place.pop(item_id)  # Remove from items to place
        item_obj = Items.PathOfExileItem(item_to_place["name"], ItemClassification.progression, item_id, self.player)
        return item_obj

    def precollect(self, item_obj):
        self.items_procollected[item_obj.code] = item_obj
        self.multiworld.push_precollected(item_obj)
    
    def generate_early(self):
        options: PathOfExileOptions = self.options
        self.goal_act = self.get_goal_act(options)
        max_level = Locations.acts[self.goal_act]["maxMonsterLevel"]

        if options.gucci_hobo_mode.value != options.gucci_hobo_mode.option_disabled:
            uniques = [item for item in Items.item_table.values() if "Unique" in item["category"]]
            for unique in uniques:
                unique["classification"] = ItemClassification.progression

            if (options.gucci_hobo_mode.value == options.gucci_hobo_mode.option_allow_one_slot_of_normal_rarity
                    or options.gucci_hobo_mode.value == options.gucci_hobo_mode.option_no_non_unique_items):
                gear_upgrades = Items.get_gear_items(table=self.items_to_place)
                for item in gear_upgrades:
                    if "Magic" in item["category"] or "Rare" in item["category"]:
                        self.items_to_place.pop(item["id"])

            if (options.gucci_hobo_mode.value == options.gucci_hobo_mode.option_no_non_unique_items):
                for item in gear_upgrades:
                    if "Normal" in item["category"]:
                        self.items_to_place.pop(item["id"])

        # remove passive skill points from item pool
        # we are using the slot_data to tell the client to chill out when it comes to passive skill points
        if options.add_passive_skill_points_to_item_pool.value == False:
            item = Items.get_by_name("Progressive passive point")
            if item:
                self.items_to_place.pop(item["id"], None)
        else:
            item = Items.get_by_name("Progressive passive point")
            if item:
                item["count"] = poeRules.passives_required_for_act[self.goal_act + 1]
                
        items_to_remove = {}
        gem_categories = {"MainSkillGem", "SupportGem", "UtilSkillGem"}
        # remove gems that are too high level from item pool
        for item in self.items_to_place.values():
            if set(item["category"]).intersection(gem_categories) and item["reqLevel"] > max_level:
                items_to_remove[item["id"]] = item

        for item_id in items_to_remove:
            self.items_to_place.pop(item_id)

        if options.gear_upgrades != options.gear_upgrades.option_no_gear_unlocked:
            categories = set()
            if options.gear_upgrades in {options.gear_upgrades.option_all_gear_unlocked_at_start,
                                         options.gear_upgrades.option_all_normal_and_unique_gear_unlocked,
                                         options.gear_upgrades.option_all_normal_gear_unlocked}:
                categories.add("Normal")
            if options.gear_upgrades in {options.gear_upgrades.option_all_gear_unlocked_at_start,
                                         options.gear_upgrades.option_all_normal_and_unique_gear_unlocked,
                                         options.gear_upgrades.option_all_uniques_unlocked}:
                categories.add("Unique")
            if options.gear_upgrades == options.gear_upgrades.option_all_gear_unlocked_at_start:
                categories.add("Magic")
                categories.add("Rare")

            all_gear_items = Items.get_gear_items(table=self.items_to_place)
            gear_upgrades = [item for item in all_gear_items if set(item["category"]).intersection(categories)]
            for item in gear_upgrades:
                item_objs = self.remove_and_create_item_by_itemdict(item)
                for item_obj in item_objs:
                    self.precollect(item_obj)

        if options.add_flask_slots_to_item_pool.value == False:
            flask_slots = Items.get_flask_items(table=self.items_to_place)
            for item in flask_slots:
                item_objs = self.remove_and_create_item_by_itemdict(item)
                for item_obj in item_objs:
                    self.precollect(item_obj)

        if options.add_max_links_to_item_pool.value == False:
            support_gem_slots = Items.get_max_links_items(table=self.items_to_place)
            for item in support_gem_slots:
                item_obj = self.remove_and_create_item_by_itemdict(item)
                self.precollect(item_obj)
        
        def handle_starting_character(char):
            item_obj = self.remove_and_create_item_by_name(char)
            self.precollect(item_obj)
            
            if options.usable_starting_gear.value in \
            (options.usable_starting_gear.option_starting_weapon_flask_and_gems,
            options.usable_starting_gear.option_starting_weapon_and_gems,
            options.usable_starting_gear.option_starting_weapon):
                weapon_name = ItemTable.starting_items_table[char]["weapon"]
                if weapon_name in [item["name"] for item in self.items_to_place.values()]:
                    self.precollect(self.remove_and_create_item_by_name(weapon_name))
                
                count = self.multiworld.state.count("Progressive max links - Weapon", self.player)
                if count < 1:
                    wep = self.remove_and_create_item_by_name("Progressive max links - Weapon")
                    self.precollect(wep)

            if options.usable_starting_gear.value in \
            (options.usable_starting_gear.option_starting_weapon_flask_and_gems,
             options.usable_starting_gear.option_starting_weapon_and_gems):
                self.precollect(self.remove_and_create_item_by_name(ItemTable.starting_items_table[char]["gem"]))
                self.precollect(self.remove_and_create_item_by_name(ItemTable.starting_items_table[char]["support"]))
            
            STARTING_FLASK_SLOTS = 3    
            if options.usable_starting_gear.value in \
            (options.usable_starting_gear.option_starting_weapon_flask_and_gems,
            options.usable_starting_gear.option_starting_weapon_and_flask_slots):

                # Get all normal flask items from the main table
                normal_flasks = Items.get_by_has_every_category({"Flask", "Normal"})
                normal_flask_ids = {flask["id"] for flask in normal_flasks}

                # Count how many normal flasks are already collected
                collected_normal_flask_count = sum(
                    1 for item_obj in self.items_procollected.values()
                    if item_obj.code in normal_flask_ids
                )

                # add flasks
                flasks_needed = STARTING_FLASK_SLOTS - collected_normal_flask_count
                if flasks_needed > 0:
                    available_flasks = Items.get_by_has_every_category({"Flask", "Normal"}, table=self.items_to_place)
                    for i in range(min(flasks_needed, len(available_flasks))):
                        flask = self.remove_and_create_item_by_name(available_flasks[i]["name"])
                        self.precollect(flask)
            return char
            
        starting_character = ""
        if options.starting_character.value == options.starting_character.option_scion:
            starting_character = handle_starting_character("Scion")
        if options.starting_character.value == options.starting_character.option_marauder:
            starting_character = handle_starting_character("Marauder")
        if options.starting_character.value == options.starting_character.option_duelist:
            starting_character = handle_starting_character("Duelist")
        if options.starting_character.value == options.starting_character.option_ranger:
            starting_character = handle_starting_character("Ranger")
        if options.starting_character.value == options.starting_character.option_shadow:
            starting_character = handle_starting_character("Shadow")
        if options.starting_character.value == options.starting_character.option_witch:
            starting_character = handle_starting_character("Witch")
        if options.starting_character.value == options.starting_character.option_templar:
            starting_character = handle_starting_character("Templar")

        temp_items_to_place = {}
        # add ascendancy items.
        char_classes = ["Marauder", "Ranger", "Witch", "Duelist", "Templar", "Shadow", "Scion"] if options.allow_unlock_of_other_characters.value else [starting_character]
        for item in range(0, options.ascendancies_available_per_class.value):
            for char_class in char_classes:
                item: Items.ItemDict = self.random.choice(Items.get_ascendancy_class_items(char_class, table=self.items_to_place))
                temp_items_to_place[item["id"]] = item
        
        # remove all the other ascendancy items
        for item in Items.get_ascendancy_items(table=self.items_to_place):
            item_id = self.item_name_to_id[item["name"]]
            self.items_to_place.pop(item_id, None)

        # remove other character class items, if not allowed
        if not options.allow_unlock_of_other_characters.value:
            character_items = Items.get_character_class_items(self.items_to_place)
            for character_item in character_items:
                if character_item['name'] != starting_character:
                    self.items_to_place.pop(character_item['id'], None)
        
        # add the temp items to place back to the items to place
        for item_id, item_obj in temp_items_to_place.items():
            self.items_to_place[item_id] = item_obj

        self.total_items_count = sum(item.get("count", 1) for item in self.items_to_place.values())
        self.locations_to_place = poeRules.SelectLocationsToAdd(world=self, target_amount=self.total_items_count)

        if len(self.locations_to_place) <  self.total_items_count:
            logger.debug(f"[Debug]: Not enough locations to place all items! {len(self.locations_to_place)} < {self.total_items_count}\nCulling...")
            Items.cull_items_to_place(self, self.items_to_place, self.locations_to_place)



        logger.debug(f"[DEBUG]: total items to place: {len(self.items_to_place)} / {self.total_items_count} possible")
        logger.debug("Here 1")
        logger.debug(f"[DEBUG]: total locs in world.: {len(self.locations_to_place)} / {len(Locations.full_locations)} possible")
        logger.debug("Here 2")

    def get_goal_act(self, options) -> int:
        if options.goal.value == options.goal.option_complete_act_1: return 1
        elif options.goal.value == options.goal.option_complete_act_2: return 2
        elif options.goal.value == options.goal.option_complete_act_3: return 3
        elif options.goal.value == options.goal.option_complete_act_4: return 4
        elif options.goal.value == options.goal.option_kauri_fortress_act_6: return 5
        elif options.goal.value == options.goal.option_complete_act_6: return 6
        elif options.goal.value == options.goal.option_complete_act_7: return 7
        elif options.goal.value == options.goal.option_complete_act_8: return 8
        elif options.goal.value == options.goal.option_complete_act_9: return 9
        elif options.goal.value == options.goal.option_complete_the_campaign: return 10
        else: return 11

    def create_regions(self):
        """Create the regions for the Path of Exile world.
        This method initializes the regions based on the acts defined in Regions.py.
        """
        options: PathOfExileOptions = self.options
        acts_to_play = [act for act in poeRegions.acts if act["act"] <= self.goal_act]
        poeRegions.create_and_populate_regions(world = self,
                                               multiworld=self.multiworld,
                                               player= self.player,
                                               locations=self.locations_to_place,
                                               act_regions=acts_to_play)
        #poeRegions.create_and_populate_regions(self, self.multiworld, self.player, locations_to_place, poeRegions.acts)

        self.multiworld.completion_condition[self.player] = lambda state: (poeRules.completion_condition(self, state))

    def create_items(self):
        """Create the items for the Path of Exile world.
        This method initializes the items based on the items defined in Items.py.
        """
        options: PathOfExileOptions = self.options
        # iterate over a copy to be safe while modifying the dictionary
        for item in list(self.items_to_place.values()):
            list_of_items = self.remove_and_create_item_by_itemdict(item)
            for item in list_of_items:
                self.multiworld.itempool.append(item)

        logger.debug(f"[DEBUG]: items left to place:{len(self.items_to_place)} /{self.total_items_count}.\n Created {len(self.locations_to_place)} locations.")



    def fill_slot_data(self):
        options: PathOfExileOptions = self.options
        game_options = {
            "gucciHobo": options.gucci_hobo_mode.value,
            "passivePointsAsItems": options.add_passive_skill_points_to_item_pool.value,
            "LevelingUpAsLocations": options.add_leveling_up_to_location_pool.value,
            "goal": options.goal.value,
        }
        client_options = {
            "ttsSpeed" : options.tts_speed.value,
            "ttsEnabled": options.enable_tts.value,
        }
        return {
            "game_options": game_options,
            "client_options": client_options,
            "poe-uuid": base64.urlsafe_b64encode(self.random.randbytes(8)).strip(b'=').decode('utf-8'), # used for generation id
        }

        
    def generate_output(self, output_directory: str):
        if self._debug:
            logger.debug(f"Generating output for {self.game} in {output_directory}")
            visualize_regions(self.multiworld.get_region(self.origin_region_name, self.player), f"Player{self.player}.puml",
                            show_entrance_names=True,
                            regions_to_highlight=self.multiworld.get_all_state(self.player).reachable_regions[
                                self.player])



# TODO handle multiple locations with the same name -- two stone rings and stone axe (IIRC)
# TODO handle multiple items with the same name -- for flasks and such