# Do the vendor imports
import os
import sys

    
vendor_dir = os.path.join(os.path.dirname(__file__), "vendor")
if vendor_dir not in sys.path:
    sys.path.insert(0, vendor_dir)
for subdir in os.listdir(vendor_dir):
    full_path = os.path.join(vendor_dir, subdir)
    if full_path not in sys.path:
        if os.path.isdir(full_path):
            sys.path.insert(0, full_path)

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from worlds.poe.Client import PathOfExileContext
    
from . import fileHelper
from . import itemFilter
from . import baseItemTypes
from . import inputHelper
from . import validationLogic
from . import gggAPI
from . import tts
import asyncio
from pynput import keyboard
from pathlib import Path


character_name = "merc_MY_FIREEE"
_generate_wav = True  # Set to True if you want to generate the wav files
validate_char_debounce_time = 5  # seconds
loop_timer = 60  # Time in seconds to wait before reloading the item filter
_debug = True  # Set to True for debug output, False for production
context = {}
possible_paths_to_client_txt = [
    Path("C:/Program Files (x86)/Grinding Gear Games/Path of Exile/logs/client.txt"),
    Path("C:/Program Files (x86)/Steam/steamapps/common/Path of Exile/logs/client.txt"),
    Path("D:/games/poe/logs/Client.txt"),
    Path.home() / "Documents" / "My Games" / "Path of Exile" / "Client.txt",
]
path_to_client_txt = Path("D:/games/poe/logs/Client.txt")


key_functions = {
    #keyboard.KeyCode: lambda: validate_char(),
    # numpad 1
    keyboard.Key.f12: lambda : validate_char(context),
    #keyboard.Key.f11: lambda : ,
}

def sync_run_async(coroutine):
    """Run an async coroutine in a synchronous context.
    If an event loop is already running, it creates a task and returns a Future.
    If no event loop is running, it uses asyncio.run to execute the coroutine.
    """
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        # No event loop running, safe to use asyncio.run
        return asyncio.run(coroutine)
    else:
        # Already in an event loop, create a task and return a Future
        return asyncio.create_task(coroutine)

def on_press(key):
    # key is a keycode, key or none.
    if key in key_functions:
        try:
            key_functions[key]()
        except Exception as e:
            print(f"Error executing function for key {key}: {e}")

last_ran_validate_char = 0
def validate_char(ctx: "PathOfExileContext" = context):
    
    # add a debounce timer to the validate_char function. I want this function to run at most every 5 seconds
    global last_ran_validate_char
    current_time = time.time()
    if current_time - last_ran_validate_char < validate_char_debounce_time:
        if _debug:
            print(f"[DEBUG] Debounced: validate_char called too soon. Last ran at {last_ran_validate_char}, current time is {current_time}.")
        return

    if _debug:
        print(f"[DEBUG] Validating character: {character_name} at {current_time}")
    sync_run_async(validationLogic.validate_and_update(character_name, ctx))
    last_ran_validate_char = time.time()

async def load_async(ctx: "PathOfExileContext" = None):
    validationLogic.character_name = character_name
    #TODO GET THIS FROM AP
    #await validationLogic.load_found_items_from_file()

    await gggAPI.async_get_access_token()
    base_items = baseItemTypes.get_base_item_types()
    item_filter_str = ""
    tts_tasks = []
    global context
    ctx = ctx if ctx is not None else context

    missing_location_ids = ctx.missing_locations
    for base_item_location_id in missing_location_ids:
        network_item = ctx.locations_info[base_item_location_id]
        item_text = ctx.player_names[network_item.player] + " world's " + ctx.item_names.lookup_in_slot(network_item.item, network_item.player)
        filename =  f"{item_text.lower()}_{tts.WPM}.wav"

        relativePath = f"{itemFilter.filter_sounds_dir_name}/{filename.lower()}"
        fullPath = itemFilter.filter_sounds_path / f"{filename}"
        if _generate_wav:
            if not os.path.exists(fullPath):
                tts_tasks.append(
                    tts.text_to_speech(
                        text=item_text,
                        filename=fullPath
                    )
                )
        item_filter_str += itemFilter.generate_item_filter_block(
            ctx.location_names.lookup_in_game(base_item_location_id),
            relativePath
        ) + "\n\n"
    await asyncio.gather(*tts_tasks)
    itemFilter.write_item_filter(item_filter_str)

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    await inputHelper.important_send_poe_text("/itemfilter __ap")


# make a loop that runs every 5 seconds to loop the item filter command
async def timer_loop():
    while True:
        validate_char()
        await inputHelper.send_poe_text("/itemfilter __ap")
        await asyncio.sleep(loop_timer)  # Adjust the sleep time as needed
def run():
    try:
        if asyncio.get_event_loop().is_running():
            # If already in an event loop, schedule as a task
            asyncio.create_task(main_async())
        else:
            asyncio.run(main_async())
    except KeyboardInterrupt:
        print("Main Loop stopped by user.")

def client_start(ctx: "PathOfExileContext"):
    global context
    context = ctx
    validationLogic.defaultContext = ctx
    run()
    
async def main_async():
    import time

    try:
        start_time = time.time()
        await load_async()

        elapsed_time = time.time() - start_time
        print(f"Generated item filter and TTS files in {elapsed_time:.2f} seconds.")
        print(f"Starting polling, watching for changes at {path_to_client_txt}...")

        async def enter_new_zone_callback(line: str):
            await validationLogic.when_enter_new_zone(line, context) # add the context to the callback
        await fileHelper.callback_on_zone_change(path_to_client_txt, enter_new_zone_callback)

        print(f"Starting Main Loop...")
        await timer_loop()
    except KeyboardInterrupt:
        print("Main Loop stopped by user.")

if __name__ == '__main__':
    # Set the character name here or pass it as an argument
    character_name = "merc_MY_FIREEE"  # Replace with your character name

    run()

































#
# polling_interval = 3  # seconds
# client_txt_last_modified_time = path_to_client_txt.stat().st_mtime
# last_entered = ""
# async def polling_loop():
#     global client_txt_last_modified_time
#     while True:
#         await asyncio.sleep(polling_interval)  # Polling interval
#         entered = fileHelper.get_last_zone_log(str(path_to_client_txt))
#         if entered == last_entered:
#             return #we are done here, no change detected
#
#             print(f"Detected change in {path_to_client_txt}, reloading item filter...")
#             validate_char()
#             await inputHelper.send_poe_text("/itemfilter __ap")
#             client_txt_last_modified_time = current_mod_time
#         else:
#             print(f"Path to client.txt does not exist: {path_to_client_txt}")


