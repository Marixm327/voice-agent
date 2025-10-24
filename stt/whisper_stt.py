"""
Whisper STT Integration for Voice Agent
Company: SpaceMarvel.ai
"""
import whisper
from typing import Optional

class WhisperSTT:
    def __init__(self, model_name: str = "base"):
        self.model = whisper.load_model(model_name)

    def transcribe(self, audio_path: str) -> Optional[str]:
        result = self.model.transcribe(audio_path)
        return result.get("text")

# Example usage:
# stt = WhisperSTT()
# text = stt.transcribe("audio.wav")
