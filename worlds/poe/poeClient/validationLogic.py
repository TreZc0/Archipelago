import asyncio

import itemFilter
import baseItemTypes
import gggAPI
import fileHelper
import inputHelper

character_name = "DefaultCharacter"
found_items_dict = {}
found_items_set = set()
save_path = "found_items.txt"
total_items = set()
is_char_in_logic = True
_debug = True
total_items.update(baseItemTypes.get_base_item_types())



async def when_enter_new_zone(line: str):
    """
    Callback function that is called when a new zone is entered.
    It validates the character and updates the item filter accordingly.

    Args:
        line (str): The line from the log file indicating the new zone entry.
    """
    global is_char_in_logic
    await validate_and_update(character_name)
    await asyncio.sleep(0.5)  # Allow some time for the filter to update
    await inputHelper.send_poe_text("/itemfilter __ap")

async def validate_and_update(character_name: str = character_name) -> bool:
    """
    Validates the character and updates the item filter if the character is valid.
    This function checks if the character exists and then updates the item filter with the found items.

    Args:
        character_name (str): The name of the character to validate.

    Returns:
        bool: True if the character is valid and the filter was updated, False otherwise.
    """
    global is_char_in_logic
    try:
        is_char_in_logic = await validate_char(character_name)
    except Exception as e:
        print(f"Error validating character: {e}")
        return False
    found_items_set.update(await get_found_items(character_name))
    await fileHelper.write_set_to_file(found_items_set, save_path)
    await update_filter()



async def validate_char(character_name: str = character_name) -> bool:
    return True

async def update_filter(full_items: set = total_items, found_items: set = found_items_set,) -> bool:
    missing_items = full_items - found_items
    item_filter_string = ""
    for item in missing_items:
        item_filter_string += itemFilter.generate_item_filter_block(item, f"{itemFilter.filter_sounds_dir_name}/{item.lower()}.wav") + "\n\n"

    if item_filter_string:
        itemFilter.write_item_filter(item_filter_string)
        print(f"Item filter updated with {len(missing_items)} items.")

async def update_filter_to_invalid_char_filter():
    invalid_alert_sound = "apsound/invalid.wav"
    invalid_item_filter_string = f""""Show
{itemFilter.invalid_style_string}
{invalid_alert_sound}"""
    itemFilter.write_item_filter(invalid_item_filter_string, item_filter_import=None)


async def get_found_items(character_name: str = character_name) -> set:
    """
    Fetches the found items for a given character from the GGG API.

    Args:
        character_name (str): The name of the character to fetch items for.

    Returns:
        dict: A dictionary containing the found items.
    """
    try:
        char = await gggAPI.get_character(character_name)
        for item in char.character.inventory:
            found_items_set.add(item.baseType)
            if _debug:
                print(f"[DEBUG] Item in inventory: {item.baseType}")
    except Exception as e:
        print(f"Error fetching found items: {e}")
        raise e
    return found_items_set

async def load_found_items_from_file(file_path: str = save_path ) -> set:
    """
    Loads the found items from a file.
    Returns:
        set: A set containing the found items.
    """
    global found_items_set
    found_set = set()
    try:
        found_set = await fileHelper.read_set_from_file(file_path)
    except Exception as e:
        print(f"Error loading found items: {e}")

    found_items_set.update(found_set)
    return found_items_set