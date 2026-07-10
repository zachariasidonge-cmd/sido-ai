# voice.py - Voice Input for Sido AI (English & Swahili)
import os
import tempfile
import base64
from datetime import datetime

# Note: For full voice features, install these:
# pip install speechrecognition pyaudio pygame gtts

class VoiceAssistant:
    def __init__(self):
        self.supported_languages = {
            "english": "en-US",
            "swahili": "sw-KE",
            "sw-ke": "sw-KE"
        }
    
    def text_to_speech(self, text: str, language: str = "sw"):
        """Convert text to speech (simplified version)"""
        try:
            # Try to import gTTS
            try:
                from gtts import gTTS
                import pygame
                
                tts = gTTS(text=text, lang=language, slow=False)
                
                # Save to temporary file
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
                    filename = tmp.name
                    tts.save(filename)
                
                # Play audio
                pygame.mixer.init()
                pygame.mixer.music.load(filename)
                pygame.mixer.music.play()
                
                while pygame.mixer.music.get_busy():
                    continue
                
                # Cleanup
                os.remove(filename)
                return "🔊 Audio played successfully!"
                
            except ImportError:
                return """
⚠️ **Voice features not fully installed.**

To enable voice features, install:
```bash
pip install gtts pygame speechrecognition pyaudio