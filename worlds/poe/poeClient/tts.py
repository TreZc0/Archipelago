import asyncio
from worlds.poe.poeClient import fileHelper
fileHelper.load_vendor_modules()

import pyttsx3
from pathlib import Path

_debug = True
WPM = 250  # Default words per minute for TTS

def get_item_name_tts_text(ctx, network_item):
    return ctx.player_names[network_item.player] + " ... " + ctx.item_names.lookup_in_slot(network_item.item,
                                                                                               network_item.player)

def safe_tts(text, filename, rate=250, volume=1, voice_id=None, overwrite=False):
    if not overwrite and Path(filename).exists():
        if _debug:
            print(f"[DEBUG] File already exists: {filename}")
        return
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    try:
        if _debug:
            print(f"[DEBUG] Initializing TTS engine for text: {text}")
        engine = pyttsx3.init()  # No driver specified
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

async def safe_tts_async(text, filename, rate=250, volume=1, voice_id=None):
    # Run sequentially to avoid COM/threading issues
    if _debug:
        print(f"[DEBUG] Async TTS: text='{text}', filename='{filename}'")

    safe_tts(text, filename, rate, volume, voice_id)

async def async_test():
    tasks = []
    for i in range(100):
        tasks.append(safe_tts_async(f"Hello {i}", f"test{i}.wav"))
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(async_test())
   # text = "Hello, this is a test of the text-to-speech system."
   # filename = Path('C:/Users/StuBob/Documents/My Games/Path of Exile/apsound') / 'test_tts.wav'
   # safe_tts(text, filename, rate=WPM, overwrite=True)

