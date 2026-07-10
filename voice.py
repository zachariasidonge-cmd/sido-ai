# voice.py - Voice Input for Sido AI (English & Swahili)
import os
import tempfile
from datetime import datetime

# Note: For full voice features, install:
# pip install gtts pygame speechrecognition pyaudio pyttsx3

class VoiceAssistant:
    def __init__(self):
        self.supported_languages = {
            "english": "en-US",
            "swahili": "sw-KE",
            "sw-ke": "sw-KE"
        }
    
    def text_to_speech(self, text: str, language: str = "sw"):
        """Convert text to speech - works without base64"""
        try:
            # Try gTTS first
            try:
                from gtts import gTTS
                import pygame
                
                tts = gTTS(text=text, lang=language, slow=False)
                
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
                    filename = tmp.name
                    tts.save(filename)
                
                pygame.mixer.init()
                pygame.mixer.music.load(filename)
                pygame.mixer.music.play()
                
                while pygame.mixer.music.get_busy():
                    continue
                
                os.remove(filename)
                return "🔊 Audio played successfully!"
                
            except ImportError:
                # Fallback to pyttsx3 (offline, no internet required)
                try:
                    import pyttsx3
                    engine = pyttsx3.init()
                    engine.say(text)
                    engine.runAndWait()
                    return "🔊 Audio played successfully (offline mode)!"
                except ImportError:
                    return """
⚠️ **Voice features not fully installed.**

To enable voice features, install:
```bash
pip install gtts pygame speechrecognition pyaudio pyttsx3