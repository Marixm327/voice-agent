"""
Whisper STT Integration for Voice Agent
Company: SpaceMarvel.ai
"""
import whisper
import numpy as np
from typing import Optional, Tuple

class WhisperSTT:
    def __init__(self, model_name: str = "base"):
        self.model = whisper.load_model(model_name)

    def transcribe_audio(self, audio: np.ndarray) -> Tuple[Optional[str], Optional[str]]:
        """
        Transcribe audio from a numpy array.
        Returns: (text, detected_language)
        """
        result = self.model.transcribe(audio, fp16=False)
        text = result.get("text")
        language = result.get("language")
        return text, language
