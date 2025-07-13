from worlds.poe.Options import PathOfExileOptions
from .Locations import PathOfExileLocation, base_item_types
from . import Items
from BaseClasses import CollectionState, Region

def can_reach(act: int, world , state: CollectionState) -> bool:
    
    return True
    opt : PathOfExileOptions = world.options

    reachable = True
    if act == 1:
        return True

    gear_logic = lambda: opt.gear_upgrades_per_act.value * act <= state.count_from_list(
        [item["name"] for item in Items.get_gear_items()], world.player
    )
    flask_logic = lambda: opt.flask_slots_per_act.value * act <= state.count_from_list(
        [item["name"] for item in Items.get_flask_items()], world.player
    )
    gem_slot_logic = lambda: opt.support_gem_slots_per_act.value * act <= state.count_from_list(
        [item["name"] for item in Items.get_max_links_items()], world.player
    )

    if reachable and opt.gear_upgrades != opt.gear_upgrades.option_all_gear_unlocked:
        reachable = gear_logic()
    if reachable and opt.flask_slot_upgrades:
        reachable = flask_logic()
    if reachable and opt.support_gem_slot_upgrades:
        reachable = gem_slot_logic()
    
    return reachable


