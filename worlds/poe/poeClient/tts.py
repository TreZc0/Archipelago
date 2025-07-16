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

from pathlib import Path
_debug = True
WPM = 250  # Default words per minute for TTS


def safe_tts(text, filename, rate=250, volume=1, voice_id=None, overwrite=False):
    if not overwrite and Path(filename).exists():
        if _debug:
            print(f"[DEBUG] File already exists: {filename}")
        return
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    try:
        import pyttsx3
#        engine = pyttsx3.init()
        engine = None
        if sys.platform.startswith('win'):
            engine = pyttsx3.init('sapi5')  # Use SAPI5 for Windows
        else:
            engine = pyttsx3.init()
        if _debug:
            print(f"[DEBUG] TTS: text='{text}', filename='{filename}'")
        engine.setProperty('rate', rate)
        engine.setProperty('volume', volume)
        if voice_id is not None:
            engine.setProperty('voice', voice_id)
        voices = engine.getProperty('voices')
        if _debug:
            print("[DEBUG] Voices available:", voices)
        engine.save_to_file(text, str(filename))
        engine.runAndWait()
        if Path(filename).exists():
            print(f"[DEBUG] File created: {filename}")
        else:
            print(f"[ERROR] File NOT created: {filename}")
    except Exception as e:
        print(f"[ERROR] Exception during TTS: {e}")



if __name__ == "__main__":
    # Example usage
    text = "Hello, this is a test of the text-to-speech system."
    filename = Path('C:/Users/StuBob/Documents/My Games/Path of Exile/apsound') / 'test_tts.wav'
    safe_tts(text, filename, rate=WPM, overwrite=True)