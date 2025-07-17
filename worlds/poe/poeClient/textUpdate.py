
from worlds.poe import Items
from worlds.poe.poeClient import inputHelper


_debug = True

async def self_whisper_callback(line: str, ctx):
    # Implement the logic for handling self whispers here
    if "!main gems" in line:
        # Get all main skill gem items in ctx.items_received
        gems = [item for item in Items.get_main_skill_gem_items() if item["Name"] in ctx.items_received]
        await inputHelper.send_poe_text(f"@{ctx.character_name} {', '.join(gems.name)}")

    if "!support gems" in line:
        # Get all support gem items in ctx.items_received
        gems = [item for item in Items.get_support_gem_items() if item["Name"] in ctx.items_received]
        await inputHelper.send_poe_text(f"@{ctx.character_name} {', '.join(gems.name)}")

    if "!utility gems" in line:
        # Get all utility gem items in ctx.items_received
        gems = [item for item in Items.get_utility_skill_gem_items() if item["Name"] in ctx.items_received]
        await inputHelper.send_poe_text(f"@{ctx.character_name} {', '.join(gems.name)}")
        
    if "!all gems" in line:
        # Get all gem items in ctx.items_received
        gems = [item for item in Items.get_all_gems() if item["Name"] in ctx.items_received]
        await inputHelper.send_poe_text(f"@{ctx.character_name} {', '.join(gems.name)}")
        
    if "!gear" in line:
        # Get all gear items in ctx.items_received
        gear = [item for item in Items.get_gear_items() if item["Name"] in ctx.items_received]
        await inputHelper.send_poe_text(f"@{ctx.character_name} {', '.join(gear.name)}")
        
    if "!flasks" in line:
        # Get all flask items in ctx.items_received
        flasks = [item for item in Items.get_flask_items() if item["Name"] in ctx.items_received]
        await inputHelper.send_poe_text(f"@{ctx.character_name} {', '.join(flasks.name)}")
        
    if "!ascendancy" in line:
        # Get all ascendancy items in ctx.items_received
        ascendancy = [item for item in Items.get_ascendancy_items() if item["Name"] in ctx.items_received]
        await inputHelper.send_poe_text(f"@{ctx.character_name} {', '.join(ascendancy.name)}")

    if "!weapons" in line:
        # Get all weapon items in ctx.items_received
        weapons = [item for item in Items.get_weapon_items() if item["Name"] in ctx.items_received]
        await inputHelper.send_poe_text(f"@{ctx.character_name} {', '.join(weapons.name)}")
        
    if "!armor" in line:
        # Get all armor items in ctx.items_received
        armor = [item for item in Items.get_armor_items() if item["Name"] in ctx.items_received]
        await inputHelper.send_poe_text(f"@{ctx.character_name} {', '.join(armor.name)}")