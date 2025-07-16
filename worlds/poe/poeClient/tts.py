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

import pyttsx3
import threading
from pathlib import Path

_debug = True
_engine = pyttsx3.init()
_engine_lock = threading.Lock()

def safe_tts(text, filename, rate=250, volume=1, voice_id=None, overwrite=False):
    if not overwrite and Path(filename).exists():
        if _debug:
            print(f"[DEBUG] File already exists: {filename}")
        return
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    with _engine_lock:
        try:
            if _debug:
                print(f"[DEBUG] TTS: text='{text}', filename='{filename}'")
            _engine.setProperty('rate', rate)
            _engine.setProperty('volume', volume)
            if voice_id is not None:
                _engine.setProperty('voice', voice_id)
            _engine.save_to_file(text, filename)
            _engine.runAndWait()
            if Path(filename).exists():
                print(f"[DEBUG] File created: {filename}")
            else:
                print(f"[ERROR] File NOT created: {filename}")
        except Exception as e:
            print(f"[ERROR] Exception during TTS: {e}")