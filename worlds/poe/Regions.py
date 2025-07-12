from BaseClasses import Region, region, MultiWorld
from worlds.poe import PathOfExileWorld
from .Locations import PathOfExileLocation, base_item_types
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
    {"act": "maps", "maxMonsterLevel": 86}
]

def create_regions(world: PathOfExileWorld, multiworld: MultiWorld, player: int, name: str, locations=base_item_types, act_regions=acts) -> list[Region]:
    last_area_level = 0
    menu = Region("menu", player, MultiWorld)
    multiworld.regions.append(menu)
    regions = []
    last_region = menu
    for act in act_regions:
        region_name = f"Act {act['act']}"
        
        region = Region(region_name, player, multiworld)

        locations_for_regions = [loc for loc in locations if loc["dropLevel"] > last_area_level and loc["dropLevel"] <= act["maxMonsterLevel"]]
        for location in locations_for_regions:
            location_name = f"{location["baseItem"]} - {act['act']}"
            locationObj = PathOfExileLocation(player, location_name, parent=region)
            region.locations.append(locationObj)
        last_area_level = act["maxMonsterLevel"]
        entrance_logic = lambda state: can_reach(act["act"], world.options, state)
        last_region.connect(region, rule=entrance_logic)
        region.connect(last_region, rule=entrance_logic)
        last_region = region

        
    return regions

class PathOfExileRegion(Region):
    def can_reach(self, state):
        return super().can_reach(state) and can_reach(self.act, self, state)
    