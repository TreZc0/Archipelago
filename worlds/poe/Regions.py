from typing import Dict
from BaseClasses import Region, MultiWorld
from .Locations import LocationDict, PathOfExileLocation, base_item_types
from .Rules import can_reach

acts = [
    {"act": 1, "maxMonsterLevel": 13},
    {"act": 2, "maxMonsterLevel": 23},
    {"act": 3, "maxMonsterLevel": 33},
    {"act": 4, "maxMonsterLevel": 40},
    {"act": 5, "maxMonsterLevel": 45},
    {"act": 6, "maxMonsterLevel": 50},
    {"act": 7, "maxMonsterLevel": 54},
    {"act": 8, "maxMonsterLevel": 60},
    {"act": 9, "maxMonsterLevel": 64},
    {"act": 10, "maxMonsterLevel": 67},
#    {"act": 11, "maxMonsterLevel": 86}
]

def create_and_populate_regions(world, multiworld: MultiWorld, player: int, locations: list[LocationDict] = base_item_types, act_regions=acts) -> list[Region]:
    locations: list[LocationDict] = locations.copy()
    menu = Region("Menu", player, multiworld)
    multiworld.regions.append(menu)
    regions = []
    last_region = menu
    for act in act_regions:
        region_name = f"Act {act['act']}"
        
        region = Region(region_name, player, multiworld)
        entrance_logic = lambda state, act=act["act"]: can_reach(act, world, state)
        last_region.connect(region, rule=entrance_logic)
        region.connect(last_region, rule=entrance_logic)
        multiworld.regions.append(region)
        last_region = region

        for i, loc in enumerate(locations):
            if loc != "used" and loc["dropLevel"] <= act["maxMonsterLevel"]:
                location_name = f"{loc['baseItem']} - Act {act['act']}"
                locationObj = PathOfExileLocation(player, location_name, parent=region, address=loc["id"])
                region.locations.append(locationObj)
                locations[i] = "used"  # Mark the location as used to avoid duplicates
            # act=act["act"] -- this is used to pass the act number to the can_reach function, otherwise it would be the last act number.

    return regions

class PathOfExileRegion(Region):
    def can_reach(self, state):
        return super().can_reach(state) and can_reach(self.act, self, state)
