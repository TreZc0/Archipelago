
from worlds.poe.Options import PathOfExileOptions
from .Locations import PathOfExileLocation, base_item_types
from . import Items
from BaseClasses import CollectionState, Region

def can_reach(act: int, opt: PathOfExileOptions , state: CollectionState) -> bool:

    can_reach = True
    if act == 1:
        return True

    gear_logic = lambda: opt.gear_upgrades_per_act.value * act <= state.count_from_list(Items.get_gear_items())
    flask_logic = lambda: opt.flask_slots_per_act.value * act <= state.count_from_list(Items.get_flask_items())
    gem_slot_logic = lambda: opt.support_gem_slots_per_act.value * act <= state.count_from_list(Items.get_support_gem_items())
    
    if can_reach and opt.gear_upgrades.value != opt.gear_upgrades.option_all_gear_unlocked:
        can_reach = gear_logic()
    if can_reach and opt.flask_slot_upgrades.value != opt.flask_slot_upgrades.option_all_flask_slots_unlocked:
        can_reach = flask_logic()
    if can_reach and opt.support_gem_slot_upgrades.value != opt.support_gem_slot_upgrades.option_all_support_gem_slots_unlocked:
        can_reach = gem_slot_logic()


    

    opt.flask_slots_per_act.value * act <= state.has_any_count


