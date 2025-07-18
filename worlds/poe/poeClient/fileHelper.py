import asyncio
import hashlib
import re
from collections import deque
from pathlib import Path

_debug = True
client_txt_last_modified_time = None


callbacks_on_file_change: list[callable] = []

def safe_filename(filename: str) -> str:
    # Replace problematic characters with underscores
    return re.sub(r"[^\w\-_\. ]", "_", filename)

def get_last_zone_log(filepath: Path, maxlines: int = 100 ) -> str:
    # read the last `maxlines` lines from the file, and returns the most recent line that contains "Entered" or "Left"
    global client_txt_last_modified_time
    if filepath.exists():
        current_mod_time = filepath.stat().st_mtime
        if current_mod_time != client_txt_last_modified_time:
            client_txt_last_modified_time = current_mod_time
            try:
                with open(filepath, 'r') as f:
                    lines = deque(f, maxlen=maxlines)
                    for line in reversed(lines):
                        if "] : You have entered" in line:
                            return line.strip()

            except FileNotFoundError:
                print(f"ERROR! client.txt at {filepath} not found.")
    return ""


async def callback_on_zone_change(filepath: Path, async_callback: callable):
    async def zone_change_callback(line: str):
        if "] : You have entered" in line:
            await async_callback(line)
    await callback_on_file_line_change(filepath, zone_change_callback)

async def callback_on_whisper_from_char(filepath: Path, character_name: str, async_callback: callable):
    async def chat_callback(line: str):
        if f"] @From {character_name}: " in line:
            await async_callback(line)
    await callback_on_file_line_change(filepath, chat_callback)

_looping = False
callbacks: list[callable] = []
poll_time = 0.3  # seconds
async def callback_on_file_line_change(filepath: Path, async_callback: callable):
    global _looping, callbacks
    callbacks.append(async_callback)
    if _looping:
        print("[DEBUG] Already running a file line change callback loop.")
        return
    
    with open(filepath, 'r') as f:
        f.seek(0, 2)  # Move the cursor to the end of the file
        _looping = True
        while True:
            line = f.readline()
            if not line:
                await asyncio.sleep(poll_time)
                continue

            line = line.strip()
            for callback in callbacks:
                if callable(callback):
                    await callback(line)


def get_last_n_lines_of_file(filepath, n=1):
    with open(filepath, 'r') as f:
        return list(deque(f, n))


def short_hash(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest()[:8]

async def write_set_to_file(data: set, file_path: str):
    """
    Writes a set to a file in a readable format.

    Args:
        data (set): The set to write.
        file_path (Path): The path to the file where the set will be written.
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(f"{item}\n")
    if _debug:
        print(f"[DEBUG] Writing set with {len(data)} items to file: {file_path}")


async def read_set_from_file(file_path: str) -> set:
    """
    Reads a set from a file.

    Args:
        file_path (Path): The path to the file to read.

    Returns:
        set: The set read from the file.
    """
    data = set()
    if not Path(file_path).exists():
        print(f"File {file_path} does not exist.")
        return data

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            item = line.strip()
            if item:
                data.add(item)
    print(f"Data read from {file_path}")
    return data

async def write_dict_to_file(data: dict, file_path: Path):
    """
    Writes a dictionary to a file in a readable format.

    Args:
        data (dict): The dictionary to write.
        file_path (Path): The path to the file where the dictionary will be written.
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        for key, value in data.items():
            f.write(f"{key}: {value}\n")
    print(f"Data written to {file_path}")

async def read_dict_from_file(file_path: Path) -> dict:
    """
    Reads a dictionary from a file.

    Args:
        file_path (Path): The path to the file to read.

    Returns:
        dict: The dictionary read from the file.
    """
    data = {}
    if not file_path.exists():
        print(f"File {file_path} does not exist.")
        return data

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if ': ' in line:
                key, value = line.split(': ', 1)
                data[key.strip()] = value.strip()
    print(f"Data read from {file_path}")
    return data