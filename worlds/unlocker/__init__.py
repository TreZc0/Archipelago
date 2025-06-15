from BaseClasses import Region, MultiWorld, Item, Location, ItemClassification
from worlds.AutoWorld import World, WebWorld
from Utils import visualize_regions
from .options import UnlockerOptions
import os
import yaml
import logging

# ----- SETUP CLIENT ----- #
from worlds.LauncherComponents import components, Component, launch_subprocess, Type, icon_paths

logger = logging.getLogger("Unlocker")

def launch_client():
    from . import client
    launch_subprocess(client.launch, name="unlockerClient", )

components.append(Component("Unlocker Client",
                            func=launch_client,
                            component_type=Type.CLIENT,
                            icon="unlocker"))

icon_paths["unlocker"] = f"ap:{__name__}/icons/unlocker.png"

# ----- ITEMS ----- #

class UnlockerItem(Item):
    game = "Unlocker"
    def __init__(self, name: str, classification: ItemClassification, id: int, player: int):
        super().__init__(name, classification, id, player)

# player specific item table
def generate_player_item_table(item_names, location_name_to_id):
    # Create a dictionary to ensure unique items
    player_items = {}
    for name in item_names:
        if name not in player_items:
            player_items[name] = {
                "name": name,
                "id": location_name_to_id.get(name),
#                "classification": ItemClassification.progression   # we need to serialize this, because we put it in the slot data
            }
    return player_items

# ----- LOCATIONS ----- #

# player specific location table
def generate_player_location_table(player_items, location_name_to_id, item_name_to_unlocker_location):
    player_locations = {}
    for name in player_items:
        location_name = item_name_to_unlocker_location[name]
        player_locations[location_name] = {
            "id": location_name_to_id.get(location_name),
            "loc_id": location_name_to_id.get(location_name),
            "name": location_name,
            "game": "Unlocker",
        }
    return player_locations

class UnlockerLocation(Location):
    game = "Unlocker"
    OnlyOtherGamesCanFill = True

    def __init__(self, player: int, name: str, address: int, parent=None, only_other_games_can_fill: bool = False):
        super().__init__(player, name, address, parent)
        self.OnlyOtherGamesCanFill = only_other_games_can_fill

    def can_fill(self, state, item, check_access=True) -> bool:
        # we can always allow items from other players to fill locations
        if item.player != self.player:
            return super().can_fill(state, item, check_access)

        if self.OnlyOtherGamesCanFill:
          return item.game != self.game
        else:
            # we do this so that there are no circular dependencies in the game.
            return item.code < self.address

# ----- WORLD CLASS ----- #

class Unlocker(World):
    game = "Unlocker"
    options_dataclass = UnlockerOptions

    def get_all_unlocker_items(players_dir="Players"):
        unique_items = {}
        # Ensure the players directory exists
        if not os.path.exists(players_dir):
            players_dir = "../" + players_dir  # Adjust path if needed
        if not os.path.exists(players_dir):
            players_dir = "../" + players_dir  # twice if we are running from the client in unlocker.
        yaml_files = os.listdir(players_dir)
        for filename in os.listdir(players_dir):
            if filename.endswith(".yaml"):
                with open(os.path.join(players_dir, filename), "r", encoding="utf-8") as f:
                    try:
                        data = yaml.safe_load(f)
                        if data.get("game", "").lower() == "unlocker":
                            items = data.get("Unlocker", {}).get("item_list", [])
                            # Handle both list and string (comma-separated) formats
                            if isinstance(items, str):
                                items = [item.strip() for item in items.split(",")]
                            for item in items:
                                if item not in unique_items:
                                    unique_items[item] = len(unique_items) + 1
                    except Exception as e:
                        logger.error(f"Error reading {filename}: {e}")
                        continue
        return unique_items

    def generate_all_unlocker_locations_from_items(item_list, item_name_to_unlocked_location=None):
        locations = {}
        for i, name in enumerate(item_list):
            key = f"Unlock #{item_list[name]} - {name} "
            locations[key] = item_list[name]
            item_name_to_unlocked_location[name] = key
        return locations

    item_name_to_unlocker_location = {}

    # needed by parent, TODO make this static
    item_name_to_id = get_all_unlocker_items()
    location_name_to_id = generate_all_unlocker_locations_from_items(item_name_to_id, item_name_to_unlocker_location)


    player_location_table = {}
    player_item_table = {}
    origin_region_name = "Menu"


    def generate_early(self) -> None:
        items = self.options.item_list.value
        self.player_item_table = generate_player_item_table(items, self.item_name_to_id)
        self.player_location_table = generate_player_location_table(items, self.location_name_to_id,
                                                                    self.item_name_to_unlocker_location)

    # Every region in Unlocker is unlocked by an item, the item and the location are tightly coupled.
    def create_regions(self):
        menu = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu)
        region = Region("Unlocker Region", self.player, self.multiworld)
        menu.connect(region)
        self.multiworld.regions.append(region)
        logger.info(f"Creating Unlocker locations for player {self.player}")

        for loc_name, loc_obj in self.player_location_table.items():
            location = UnlockerLocation(self.player, loc_name, loc_obj["id"], region, self.options.only_allow_other_games_items.value == 1)
            def access_func(state, loc=loc_obj["id"]):
                return state.has(self.item_id_to_name[loc], self.player)
            location.access_rule = access_func
            region.locations.append(location)

    def create_items(self):
        items = self.options.item_list.value
        logger.info(f"Creating Unlocker items: {items}")
        for i, (name, data) in enumerate(self.player_item_table.items()):
            new_item = UnlockerItem(name, ItemClassification.progression, data["id"], self.player) # TODO classification
            self.multiworld.itempool.append(new_item)

    def set_rules(self):
        # completion condition - player wins when they collect all items
        def completion_rule(state):
            for item in self.player_item_table.keys():
                if not state.has(item, self.player):
                    return False
            return True

        self.multiworld.completion_condition[self.player] = completion_rule

    def fill_slot_data(self):
        location_table = self.player_location_table
        # make a table of item id to location name
        item_id_to_location_name = {data["id"]: name for name, data in self.player_location_table.items()}
        return {
            "item_name_to_unlocker_location": self.item_name_to_unlocker_location,
            "player_location_table": self.player_location_table,
            "player_item_table": self.player_item_table,
            "item_id_to_location_name": item_id_to_location_name,
        }

    def generate_output(self, output_directory: str):
        visualize_regions(self.multiworld.get_region("Menu", self.player), f"Player{self.player}.puml",
                          show_entrance_names=True,
                          regions_to_highlight=self.multiworld.get_all_state(self.player).reachable_regions[
                              self.player])