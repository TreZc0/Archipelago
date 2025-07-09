import sys
import os

# # Add local wheels to sys.path
# vendor_dir = os.path.join(os.path.dirname(__file__), "vendor")
# for subdir in os.listdir(vendor_dir):
#     full_path = os.path.join(vendor_dir, subdir)
#     if os.path.isdir(full_path):
#         sys.path.insert(0, full_path)

# Now safe to import
import asyncio
from ../ import pygetwindow as gw
import tkinter as tk
import time
from pynput.keyboard import Controller, Key


tkRoot = tk.Tk()
tkRoot.withdraw()


keyboard_controller = Controller()

_debug = True
_last_called = None
_debounce_time = 5  # seconds


async def important_send_poe_text(command: str, retry_times: int = 9001, retry_delay: float = 0.5):
    return await send_poe_text(command, retry_times, retry_delay)

async def send_poe_text(command:str, retry_times:int = 0, retry_delay:float = 0):
    window = gw.getActiveWindow()

    # if windows is active
    if window.title == "Path of Exile":
        if _debug:
            print("[DEBUG] Found active Path of Exile window")

        now = time.monotonic()
        if _last_called is not None and now - _last_called < 5:
            if _debug:
                print("[DEBUG] Debounced: send_poe_text called too soon.")
            return
        send_poe_text._last_called = now
        clipboard_value = ""
        try:
            clipboard_value = tkRoot.clipboard_get()
        except tk.TclError:
            print("Clipboard is empty, will not restore clipboard value after sending command")

        tkRoot.clipboard_clear()
        tkRoot.clipboard_append(command)


        # Press Enter
        keyboard_controller.press(Key.enter)
        keyboard_controller.release(Key.enter)

        await asyncio.sleep(0.05)
        # Type command
        keyboard_controller.press(Key.ctrl)
        keyboard_controller.press('v')
        keyboard_controller.release('v')
        keyboard_controller.release(Key.ctrl)

        await asyncio.sleep(0.05)
        # Press Enter again
        keyboard_controller.press(Key.enter)
        keyboard_controller.release(Key.enter)

        tkRoot.clipboard_clear()
        tkRoot.clipboard_append(clipboard_value)
        if _debug:
            print("[DEBUG] Sent command to Path of Exile:", command)
    else:
        if retry_times > 0:
            if _debug:
                print(f"Path of Exile window not active, retrying {retry_times} times with {retry_delay} seconds delay")
            for i in range(retry_times):
                await asyncio.sleep(retry_delay)
                return await send_poe_text(command, retry_times - 1, retry_delay)
        else:
            if _debug:
                print("[DEBUG] Path of Exile window not active, will not retry, will not send command")


