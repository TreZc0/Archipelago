import os
import sys
vendor_dir = os.path.join(os.path.dirname(__file__), "vendor")
if vendor_dir not in sys.path:
    sys.path.insert(0, vendor_dir)

import asyncio
import pygetwindow as gw
import time
from pynput.keyboard import Controller, Key

keyboard_controller = Controller()
_debug = True
_last_called = None
_debounce_time = 5  # seconds

def get_clipboard():
    import tkinter as tk
    root = tk.Tk()
    root.withdraw()
    try:
        value = root.clipboard_get()
    except tk.TclError:
        value = ""
    root.destroy()
    return value

def set_clipboard(value):
    import tkinter as tk
    root = tk.Tk()
    root.withdraw()
    root.clipboard_clear()
    root.clipboard_append(value)
    root.update()  # Ensure clipboard is set before destroying
    root.destroy()
    
def get_then_set_clipboard(new_value: str) -> str:
    import tkinter as tk
    root = tk.Tk()
    root.withdraw()
    try:
        value = root.clipboard_get()
    except tk.TclError:
        value = ""
    root.clipboard_clear()
    root.update()
    root.clipboard_append(new_value)
    root.update()  # Ensure clipboard is set before destroying
    root.destroy()
    return value

async def important_send_poe_text(command: str, retry_times: int = 9001, retry_delay: float = 0.5):
    return await send_poe_text(command, retry_times, retry_delay)

async def send_poe_text(command:str, retry_times:int = 0, retry_delay:float = 0):
    window = gw.getActiveWindow()
    global _last_called
    # if windows is active
    if window is not None and window.title == "Path of Exile":
        if _debug:
            print("[DEBUG] Found active Path of Exile window")

        now = time.monotonic()
        if _last_called is not None and now - _last_called < 5:
            if _debug:
                print("[DEBUG] Debounced: send_poe_text called too soon.")
            return
        _last_called = now

        clipboard_value = get_then_set_clipboard(command)

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

        set_clipboard(clipboard_value)
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


