# voice.py - Voice Input for Sido AI (Optional Features)
import os
import tempfile
from datetime import datetime

class VoiceAssistant:
    def __init__(self):
        self.supported_languages = {
            "english": "en-US",
            "swahili": "sw-KE",
            "sw-ke": "sw-KE"
        }
        self.voice_available = self._check_voice_availability()
    
    def _check_voice_availability(self):
        """Check if voice features are available"""
        try:
            import gtts
            import pygame
            return True
        except ImportError:
            return False
    
    def text_to_speech(self, text: str, language: str = "sw"):
        """Convert text to speech - optional feature"""
        if not self.voice_available:
            return """
🔊 **Voice features are optional.**

Voice features (gTTS, pygame, pyaudio) can be installed locally but are not required for Sido AI to work.

💡 **Voice is available locally**, but for the web version, text responses work perfectly.

**Try these features instead:**
- "Speak Habari" (will work locally with audio libraries)
- Regular text responses work everywhere
"""
        
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
            
        except Exception as e:
            return f"⚠️ Voice error: {str(e)}"
    
    def speech_to_text(self, language: str = "sw-KE"):
        """Convert speech to text - optional feature"""
        return """
🎤 **Voice input is optional.**

For voice input, install locally:
```bash
pip install speechrecognition pyaudio