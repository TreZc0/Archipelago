from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from BaseClasses import Entrance, Location, Region

from .ALttPDoorRandomizer.BaseClasses import PotItem, PotFlags
from .ALttPDoorRandomizer.source.dungeon import EnemyList
from .ALttPDoorRandomizer import PotShuffle
from .ALttPDoorRandomizer import Regions as DoorRandomizerRegions
from .ALttPDoorRandomizer.source.rom import DataTables
from .StateAdapter import adapt_door_rando_rule

if TYPE_CHECKING:
    from .World import ALttPRWorld


location_name_to_id = {}
lookup_id_to_name = {}
lookup_name_to_id = {}
logger = logging.getLogger("alttpr")


class ALttPRLocation(Location):
    game = "The Legend of Zelda: A Link to the Past"


def create_and_connect_regions(world: ALttPRWorld) -> None:
    # First define every region, then loop through a second time to connect them.
    # Otherwise we're trying to connect to regions that don't exist yet.
    ap_regions = {}
    event_locations = get_event_locations(world)

    for region in world.door_rando_world.regions:
        ap_region = Region(region.name, world.player, world.multiworld)
        for location in region.locations:
            if "Shop - " in location.name or "Upgrade - " in location.name:
                # TODO: Shopsanity
                continue
            elif " Item " in location.name:
                # TODO: Retro
                continue
            else:
                # The dungeon prize locations aren't in lookup_name_to_id (not sure how they're removed?),
                # so they won't have an ID, which is how an event location is defined.
                id = lookup_name_to_id.get(location.name, None)
                if not id and \
                   " - Prize" not in location.name and \
                   "Key Drop" not in location.name and \
                   "Pot Key" not in location.name and \
                   location.name not in event_locations:
                    logger.error(f"Found unknown location {location.name} in region {region.name}.")
                    raise Exception()

                ap_location = ALttPRLocation(
                    world.player, location.name, id, ap_region
                )
                ap_location.access_rule = adapt_door_rando_rule(location.access_rule, world.door_rando_world, world.player)
                ap_region.locations.append(ap_location)

        ap_regions[region.name] = ap_region

    # Now make all the connections
    for region in world.door_rando_world.regions:
        ap_region = ap_regions[region.name]
        for exit in region.exits:
            if exit.connected_region is None:
                continue
            ap_entrance = Entrance(world.player, exit.name, parent=ap_region)
            ap_entrance.access_rule = adapt_door_rando_rule(exit.access_rule, world.door_rando_world, world.player)
            ap_region.exits.append(ap_entrance)
            ap_entrance.connect(ap_regions[exit.connected_region.name])

    world.multiworld.regions += list(ap_regions.values())


def get_event_locations(world: ALttPRWorld):
    # TODO: I feel like most of these aren't needed until door randomizer is added, and some of them still seem unnecessary (e.g. Skull Star Tile).
    # It's fine if it doesn't affect anything for players, but if it shows up in the player log or Poptracker than that could be an annoyance.
    event_locations = {
        "Ganon": "Triforce",
        "Agahnim 1": "Beat Agahnim 1",
        "Agahnim 2": "Beat Agahnim 2",
        "Frog": "Get Frog",
        "Missing Smith": "Return Smith",
        "Dark Blacksmith Ruins": "Pick Up Purple Chest",
        "Floodgate": "Open Floodgate",
        "Trench 1 Switch": "Trench 1 Filled",
        "Trench 2 Switch": "Trench 2 Filled",
        "Swamp Drain": "Drained Swamp",
        "Attic Cracked Floor": "Shining Light",
        "Suspicious Maiden": "Maiden Rescued",
        "Revealing Light": "Maiden Unmasked",
        "Ice Block Drop": "Convenient Block",
        "Skull Star Tile": "Hidden Pits",
        # Some events are only created in certain modes
        # "Zelda Pickup": "Zelda Herself",
        # "Zelda Drop Off": "Zelda Delivered",
        # "Murahdahla": "Triforce",
    }

    goal = world.options.goal.value
    if goal == "triforcehunt":
        event_locations["Murahdahla"] = "Triforce"
        event_locations["Ganon"] = "Nothing"
    if world.options.world_mode.value == "standard":
        event_locations["Zelda Pickup"] = "Zelda Herself"
        event_locations["Zelda Drop Off"] = "Zelda Delivered"

    return event_locations



# Add info on all locations to lookup_id_to_name and lookup_name_to_id.
# This is used by the client to send items we pick up.
def init_lookups():
    global lookup_id_to_name
    global lookup_name_to_id

    lookup_id_to_name = {x: y for x, y in DoorRandomizerRegions.lookup_id_to_name.items()}
    lookup_name_to_id = {x: y for x, y in DoorRandomizerRegions.lookup_name_to_id.items()}
    for super_tile, pot_list in PotShuffle.vanilla_pots.items():
        for pot_index, pot in enumerate(pot_list):
            if pot.item != PotItem.Hole:
                if pot.item == PotItem.Key:
                    loc_name = next(loc for loc, datum in PotShuffle.key_drop_data.items()
                                    if datum[1] == super_tile)
                else:
                    # TODO: Pottery lottery
                    # descriptor = 'Large Block' if pot.flags & PotFlags.Block else f'Pot #{pot_index+1}'
                    # loc_name = f'{pot.room} {descriptor}'
                    continue
                location_id = DoorRandomizerRegions.pot_address(pot_index, super_tile)
                lookup_name_to_id[loc_name] = location_id
                lookup_id_to_name[location_id] = loc_name
    uw_table = DataTables.get_uw_enemy_table()
    key_drop_data = {(v[1][1], v[1][2]): k for k, v in PotShuffle.key_drop_data.items() if v[0] == 'Drop'}
    for super_tile, enemy_list in uw_table.room_map.items():
        for index, sprite in enumerate(enemy_list):
            if (super_tile, index) in key_drop_data:
                loc_name = key_drop_data[(super_tile, index)]
                location_id = PotShuffle.key_drop_data[loc_name][1][0]
            else:
                # TODO: Enemizer
                # loc_name = f'{sprite.region} Enemy #{index+1}'
                # location_id = EnemyList.drop_address(index, super_tile)
                continue
            lookup_name_to_id[loc_name] = location_id
            lookup_id_to_name[location_id] = loc_name

init_lookups()