import pyttsx3
from pathlib import Path
import asyncio
import threading

_debug = True
_engine = pyttsx3.init()
_engine_lock = threading.Lock()
WPM = 250  # Default words per minute for TTS
async def text_to_speech(text, filename: str, tts_rate_wpm=WPM, volume=1, voice_id=None):
    loop = asyncio.get_event_loop()
    def run_tts():
        with _engine_lock:
            if _debug:
                print(f"[DEBUG] Starting TTS: text='{text}', filename='{filename}', rate={tts_rate_wpm}, volume={volume}, voice_id={voice_id}")
            _engine.setProperty('rate', tts_rate_wpm)
            _engine.setProperty('volume', volume)
            if voice_id is not None:
                _engine.setProperty('voice', voice_id)
            _engine.save_to_file(text, filename)
            _engine.runAndWait()
            if _debug:
                print(f"[DEBUG] Finished TTS: text='{text}' file saved to '{filename}'")
    await loop.run_in_executor(None, run_tts)

async def text_to_speech_if_doesnt_exist(text, filename: str, tts_rate_wpm=WPM, volume=1, voice_id=None):
    if not Path(filename).exists():
        await text_to_speech(text, filename, tts_rate_wpm, volume, voice_id)