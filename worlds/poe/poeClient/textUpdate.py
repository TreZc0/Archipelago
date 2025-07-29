import asyncio
import base64
import logging
import random
import re
from NetUtils import ClientStatus
from worlds.poe import Items
from worlds.poe.poeClient import inputHelper
from worlds.poe.poeClient import fileHelper
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from worlds.poe.Client import PathOfExileContext
    from worlds.poe import PathOfExileWorld

_debug = True
_random_string = ""
logger = logging.getLogger("poeClient.textUpdate")

def get_zone_from_line(ctx: "PathOfExileContext", line: str) -> str:
    # Implement the logic for handling self goals here
    match = re.search(r'] : You have entered (.+)\.$', line)
    zone = ""
    if match:
        zone = match.group(1)
    ctx.last_entered_zone = zone
    return zone
  

def get_char_name_and_message_from_line(line: str) -> tuple[str, str]:
    # Extract character name from the line
    match = re.search(r']\s?(<.*>)?\s?(@To|@From)?\s?(.+): (\\x00)?(.*)', line)
    if match:
        return (match.group(3), match.group(5))
    return ("", "")

async def callback_if_valid_char(ctx: "PathOfExileContext", callback: callable):
    global _random_string


    def verify_character_callback(line: str):
        try:
            if _debug:
                logger.info(f"[DEBUG] verify_character_callback: {line}")
            char_name, message = get_char_name_and_message_from_line(line)
            if not f"{_random_string}" in message:
                return
            if not char_name == ctx.character_name:
                logger.info(f"[DEBUG] FALSE ALARM, Chars don't match: char_name={char_name}, ctx.character_name={ctx.character_name}")
                chat_command_external_callbacks.pop(_random_string, None)
                callback(False)
                return            
            chat_command_external_callbacks.pop(_random_string, None)
            callback(True)
        except Exception as e:
            callback(False)

    global chat_command_external_callbacks
    chat_command_external_callbacks[_random_string] = verify_character_callback
    _random_string = random.randbytes(8).hex()
    await inputHelper.send_poe_text(f"{_random_string}")


chat_command_external_callbacks : dict[str, callable]  = dict()

async def chat_commands_callback(ctx: "PathOfExileContext", line: str):
    # Implement the logic for handling self whispers here
    global _random_string
    char_name, message = get_char_name_and_message_from_line(line)
    if "!ap char" in message:
        _random_string = random.randbytes(8).hex()
        await inputHelper.send_poe_text(f"char_{_random_string}")
    if "char_" in message:
        parts = line.split("char_")
        if parts[1] == _random_string:
            if _debug:
                logger.info(f"[DEBUG] self_whisper_callback: {parts}")
            ctx.character_name = char_name
            await inputHelper.send_poe_text_ignore_debounce(f"@{ctx.character_name} Welcome to Archipelago!")
            await fileHelper.save_settings(ctx)
            return


    if not char_name == ctx.character_name:
        return
    item_ids = [item.item for item in ctx.items_received]
    if "!main gems" in message:
        # Get all main skill gem items in item_ids
        gems = [item for item in Items.get_main_skill_gem_items() if item["id"] in item_ids]
        # sort by required level
        gems.sort(key=lambda x: x.get("requiredLevel", 0))  # Sort by required level
        await split_send_message(ctx,', '.join(gem['name'] for gem in gems))

    if "!support gems" in message:
        # Get all support gem items in item_ids
        gems = [item for item in Items.get_support_gem_items() if item["id"] in item_ids]
        await split_send_message(ctx,', '.join(gem['name'] for gem in gems))

    if "!utility gems" in message:
        # Get all utility gem items in item_ids
        gems = [item for item in Items.get_utility_skill_gem_items() if item["id"] in item_ids]
        await split_send_message(ctx,', '.join(gem['name'] for gem in gems))
        
    if "!all gems" in message or "!gems" in message:
        # Get all gem items in item_ids
        gems = [item for item in Items.get_all_gems() if item["id"] in item_ids]
        await split_send_message(ctx,', '.join(gem['name'] for gem in gems))

    if "!usable gems" in message:
        # Get all usable skill gems in item_ids
        usable_gems = [item for item in Items.get_main_skill_gems_by_required_level(0, ctx.last_character_level) if item["id"] in item_ids]
        usable_gems.sort(key=lambda x: x.get("requiredLevel", 0), reverse=True)  # Sort by required level descending
        await split_send_message(ctx,', '.join(gem['name'] for gem in usable_gems))

    if "!gear" in message:
        # Get all gear items in item_ids
        gear = [item for item in Items.get_gear_items() if item["id"] in item_ids]
        await split_send_message(ctx,', '.join(gear['name'] for gear in gear))

    if "!links" in message:
        # Get all linked items in item_ids
        links = [item for item in Items.get_max_links_items() if item["id"] in item_ids]
        await split_send_message(ctx,', '.join(link['name'] for link in links))

    if "!flasks" in message:
        # Get all flask items in item_ids
        flasks = [item for item in Items.get_flask_items() if item["id"] in item_ids]
        await split_send_message(ctx,', '.join(flask['name'] for flask in flasks))

    if "!ascendancy" in message:
        # Get all ascendancy items in item_ids
        ascendancy = [item for item in Items.get_ascendancy_items() if item["id"] in item_ids]
        await split_send_message(ctx,', '.join(ascendancy['name'] for ascendancy in ascendancy))

    if "!weapons" in message:
        # Get all weapon items in item_ids
        weapons = [item for item in Items.get_weapon_items() if item["id"] in item_ids]
        await split_send_message(ctx,', '.join(weapons['name'] for weapons in weapons))

    if "!armor" in message:
        # Get all armor items in item_ids
        armor = [item for item in Items.get_armor_items() if item["id"] in item_ids]
        await split_send_message(ctx,', '.join(armor['name'] for armor in armor))
        
async def split_send_message(ctx, message: str, max_length: int = 500):
    """
    Splits a message into chunks and sends each chunk separately.
    """
    if not message:
        message = "None"
    prefix = f"@{ctx.character_name} "
    max_length = max_length - len(prefix)  # Adjust for character name prefix
    if len(message) <= max_length:
        await inputHelper.send_poe_text(message)
        return

    # Split the message into chunks, only at a comma
    chunks = [message[i:i + max_length] for i in range(0, len(message), max_length)]
    
    # Send each chunk
    for chunk in chunks:
        await inputHelper.send_poe_text(prefix + chunk, retry_times=len(chunks) + 1, retry_delay=0.5)