# Do the vendor imports
from . import fileHelper
fileHelper.load_vendor_modules()

import os
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from worlds.poe.Client import PathOfExileContext

from . import itemFilter
from . import inputHelper
from . import validationLogic
from . import gggAPI
from . import tts
import asyncio
import threading
import time
import logging
from pynput import keyboard
from pathlib import Path


logger = logging.getLogger("poeClient.main")
_generate_wav = True  # Set to True if you want to generate the wav files
_debug = True  # Set to True for debug output, False for production
validate_char_debounce_time = 2  # seconds
loop_timer = 0.1  # Time in seconds to wait before reloading the item filter
context = {}
_run_update_item_filter = False
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
            logger.info(f"Error executing function for key {key}: {e}")

last_ran_validate_char = 0
def validate_char(ctx: "PathOfExileContext" = context):
    
    # add a debounce timer to the validate_char function. I want this function to run at most every 5 seconds
    global last_ran_validate_char, _run_update_item_filter
    current_time = time.time()
    if current_time - last_ran_validate_char < validate_char_debounce_time:
        if _debug:
            logger.info(f"[DEBUG] Debounced: validate_char called too soon. Last ran at {last_ran_validate_char}, current time is {current_time}.")
        return

    if _debug:
        logger.info(f"[DEBUG] Validating character: {ctx.character_name} at {current_time}")
    sync_run_async(validationLogic.validate_and_update(ctx))
    _run_update_item_filter = True
    last_ran_validate_char = time.time()

async def async_load(ctx: "PathOfExileContext" = None):
    # TODO: store / load character name, path to client.txt and base item filter from the context to a file


    await gggAPI.async_get_access_token()
    
    global context
    ctx = ctx if ctx is not None else context

    tts.generate_tts_tasks_from_missing_locations(ctx)
    threading.Thread(target=tts.run_tts_tasks, daemon=True).start()  # Run TTS tasks in a separate thread

    itemFilter.update_item_filter_from_context(ctx)

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    await inputHelper.important_send_poe_text("/itemfilter __ap")



async def timer_loop():
    ticks = 0.1
    global _run_update_item_filter
    while True:
        await asyncio.sleep(loop_timer)  # Adjust the sleep time as needed
        ticks += 0.1
        if _run_update_item_filter: # every hour
            await inputHelper.send_poe_text("/itemfilter __ap")
            _run_update_item_filter = False


        if ticks % 1 < 0.1:
            pass
            
            

def run():
    try:
        if asyncio.get_event_loop().is_running():
            # If already in an event loop, schedule as a task
            asyncio.create_task(main_async())
        else:
            asyncio.run(main_async())
    except KeyboardInterrupt:
        logger.info("Main Loop stopped by user.")

def client_start(ctx: "PathOfExileContext"):
    global context, path_to_client_txt
    context = ctx
    validationLogic.defaultContext = ctx
    path_to_client_txt = ctx.client_text_path if ctx.client_text_path else path_to_client_txt
    path_to_client_txt = Path(path_to_client_txt)

    run()
    
async def main_async():
    import time

    try:
        await async_load(context)
        async def enter_new_zone_callback(line: str):
            await validationLogic.when_enter_new_zone(context, line) # add the context to the callback


        async def chat_commands(line: str):
            from worlds.poe.poeClient.textUpdate import chat_commands_callback
            await chat_commands_callback(context, line)
            


        logger.info("Starting Main Loop...")
        tasks = [
            fileHelper.callback_on_file_change(path_to_client_txt, [enter_new_zone_callback, chat_commands]),
            timer_loop()]
        await asyncio.gather(*tasks)
    except KeyboardInterrupt:
        logger.info("Main Loop stopped by user.")

if __name__ == '__main__':
    # Set the character name here or pass it as an argument
#    context.character_name = "merc_MY_FIREEE"  # Replace with your character name

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
#             logger.info(f"Detected change in {path_to_client_txt}, reloading item filter...")
#             validate_char()
#             await inputHelper.send_poe_text("/itemfilter __ap")
#             client_txt_last_modified_time = current_mod_time
#         else:
#             logger.info(f"Path to client.txt does not exist: {path_to_client_txt}")


