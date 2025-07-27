import base64
import random
import re
from NetUtils import ClientStatus
from worlds.poe import Items
from worlds.poe.poeClient import inputHelper

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from worlds.poe.Client import PathOfExileContext
    from worlds.poe import PathOfExileWorld

_debug = True
_random_string = ""

async def self_goal_callback(line: str, ctx: "PathOfExileContext"):
    # Implement the logic for handling self goals here
    if not f"] : You have entered Karui Shores." in line:
        return
    if _debug:
        print(f"[DEBUG] self_goal_callback: {line}")
    await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
    ctx.finished_game = True

async def self_whisper_callback(line: str, ctx: "PathOfExileContext"):
    # Implement the logic for handling self whispers here
    global  _random_string
    if "!ap char" in line:
        _random_string = base64.b64encode(random.randbytes(8)).strip(b'=').decode('utf-8')
        await inputHelper.send_poe_text(f"apchar_{_random_string}")
    if "apchar_" in line:
        line = line.split("apchar_")
        if line[1] == _random_string:
            if _debug:
                print(f"[DEBUG] self_whisper_callback: {line}")
            match = re.search(r'\] (\S+):', line[0])
            if match:
                ctx.character_name = match.group(1).strip()
                await inputHelper.send_poe_text(f"@{ctx.character_name} Welcome to Archipelago!",5)
            else:
                if _debug:
                    print("[DEBUG] No char found in line:", line[0])
            return
        

    if not f"] @From {ctx.character_name}: " in line:
        return
    item_ids = [item.item for item in ctx.items_received]
    if "!main gems" in line:
        # Get all main skill gem items in item_ids
        gems = [item for item in Items.get_main_skill_gem_items() if item["id"] in item_ids]
        # sort by required level
        gems.sort(key=lambda x: x.get("requiredLevel", 0) * -1)  # Sort by required level descending
        await inputHelper.send_poe_text(f"@{ctx.character_name} {', '.join(gem['name'] for gem in gems)}")

    if "!support gems" in line:
        # Get all support gem items in item_ids
        gems = [item for item in Items.get_support_gem_items() if item["id"] in item_ids]
        await inputHelper.send_poe_text(f"@{ctx.character_name} {', '.join(gem['name'] for gem in gems)}")

    if "!utility gems" in line:
        # Get all utility gem items in item_ids
        gems = [item for item in Items.get_utility_skill_gem_items() if item["id"] in item_ids]
        await inputHelper.send_poe_text(f"@{ctx.character_name} {', '.join(gem['name'] for gem in gems)}")
        
    if "!all gems" in line or "!gems" in line:
        # Get all gem items in item_ids
        gems = [item for item in Items.get_all_gems() if item["id"] in item_ids]
        await inputHelper.send_poe_text(f"@{ctx.character_name} {', '.join(gem['name'] for gem in gems)}")
        
    if "!gear" in line:
        # Get all gear items in item_ids
        gear = [item for item in Items.get_gear_items() if item["id"] in item_ids]
        await inputHelper.send_poe_text(f"@{ctx.character_name} {', '.join(gear['name'] for gear in gear)}")

    if "!links" in line:
        # Get all linked items in item_ids
        links = [item for item in Items.get_max_links_items() if item["id"] in item_ids]
        await inputHelper.send_poe_text(f"@{ctx.character_name} {', '.join(link['name'] for link in links)}")

    if "!flasks" in line:
        # Get all flask items in item_ids
        flasks = [item for item in Items.get_flask_items() if item["id"] in item_ids]
        await inputHelper.send_poe_text(f"@{ctx.character_name} {', '.join(flask['name'] for flask in flasks)}")

    if "!ascendancy" in line:
        # Get all ascendancy items in item_ids
        ascendancy = [item for item in Items.get_ascendancy_items() if item["id"] in item_ids]
        await inputHelper.send_poe_text(f"@{ctx.character_name} {', '.join(ascendancy['name'] for ascendancy in ascendancy)}")

    if "!weapons" in line:
        # Get all weapon items in item_ids
        weapons = [item for item in Items.get_weapon_items() if item["id"] in item_ids]
        await inputHelper.send_poe_text(f"@{ctx.character_name} {', '.join(weapons['name'] for weapons in weapons)}")

    if "!armor" in line:
        # Get all armor items in item_ids
        armor = [item for item in Items.get_armor_items() if item["id"] in item_ids]
        await inputHelper.send_poe_text(f"@{ctx.character_name} {', '.join(armor['name'] for armor in armor)}")