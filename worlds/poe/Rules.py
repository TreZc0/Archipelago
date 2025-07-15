from worlds.poe.Options import PathOfExileOptions
from .Locations import PathOfExileLocation, base_item_types
from . import Items
from BaseClasses import CollectionState, Region


MAX_GEAR_UPGRADES   = 50
MAX_FLASK_SLOTS     = 10
MAX_GEM_SLOTS       = 21
MAX_SKILL_GEMS      = 20 # you will get more, but this is the max required for "logic"
_debug = True
_very_debug = False
def can_reach(act: int, world , state: CollectionState) -> bool:
    opt : PathOfExileOptions = world.options

    reachable = True
    if act == 1:
        return True

#    if act != 10:
#        print("_______________________________________ YOU ARE IN ACT " + str(act) + " _______________________________________")


    ascedancy_amount = opt.ascendancies_available_per_class.value if act == 3 else 0
    gear_amount = min(opt.gear_upgrades_per_act.value * (act - 1), MAX_GEAR_UPGRADES)
    flask_amount = 0 if not opt.flask_slot_upgrades else min(opt.flask_slots_per_act.value * (act - 1), MAX_FLASK_SLOTS)
    gem_slot_amount = 0 if not opt.support_gem_slot_upgrades else min(opt.support_gem_slots_per_act.value * (act - 1), MAX_GEM_SLOTS)
    skill_gem_amount = min(opt.skill_gems_per_act.value * (act - 1), MAX_SKILL_GEMS)

    ascedancy_count = state.count_from_list([item['name'] for item in Items.get_ascendancy_class_items(opt.starting_character.current_option_name)], world.player)
    gear_count = state.count_from_list([item['name'] for item in Items.get_gear_items()], world.player)
    flask_count = state.count_from_list([item['name'] for item in Items.get_flask_items()], world.player)
    gem_slot_count = state.count_from_list([item['name'] for item in Items.get_max_links_items()], world.player)
    skill_gem_count = state.count_from_list([item['name'] for item in Items.get_main_skill_gem_items()], world.player)

    reachable = ascedancy_count >= ascedancy_amount and \
           gear_count >= gear_amount and \
           flask_count >= flask_amount and \
           gem_slot_count >= gem_slot_amount and \
           skill_gem_count >= skill_gem_amount
           
    if not reachable:
        if _debug:
            print (f"[DEBUG] Act {act} not reachable with gear: {gear_count}/{gear_amount}, flask: {flask_count}/{flask_amount}, gem slots: {gem_slot_count}/{gem_slot_amount}, skill gems: {skill_gem_count}/{skill_gem_amount}, ascendancies: {ascedancy_count}/{ascedancy_amount} for {opt.starting_character.current_option_name}")
        if _very_debug:
            print(f"[DEBUG] expecting Act {act} - Gear: {gear_amount}, Flask: {flask_amount}, Gem Slots: {gem_slot_amount}, Skill Gems: {skill_gem_amount}, Ascendancies: {ascedancy_amount}")
            print(f"[DEBUG] we have   Act {act} - Gear: {gear_count}, Flask: {flask_count}, Gem Slots: {gem_slot_count}, Skill Gems: {skill_gem_count}, Ascendancies: {ascedancy_count}")
            #add up all the prog items


            total_items = state.count_from_list([item["name"] for item in Items.get_gear_items()], world.player) + \
                          state.count_from_list([item["name"] for item in Items.get_flask_items()], world.player) + \
                          state.count_from_list([item["name"] for item in Items.get_max_links_items()], world.player) + \
                          state.count_from_list([item["name"] for item in Items.get_main_skill_gem_items()], world.player) + \
                          state.count_from_list([item["name"] for item in Items.get_ascendancy_class_items(opt.starting_character.current_option_name)], world.player)
            print(f"[DEBUG] total items {total_items}, ")
            print(f"[DEBUG] expecting   {gear_amount + flask_amount + gem_slot_amount + skill_gem_amount} items")
            print(f"\n\n")

    if _debug:
#        print(f"[DEBUG] Act {act} reachable: {reachable}")
        pass
    
    
    return reachable



