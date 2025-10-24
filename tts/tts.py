"""
TTS Integration for Voice Agent (Cartesia/ElevenLabs)
Company: SpaceMarvel.ai
"""
import os
import requests
from typing import Optional

class ElevenLabsTTS:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("ELEVENLABS_API_KEY")
        self.base_url = "https://api.elevenlabs.io/v1/text-to-speech/"

    def synthesize(self, text: str, voice_id: str) -> Optional[bytes]:
        url = f"{self.base_url}{voice_id}"
        payload = {"text": text}
        headers = {
            "xi-api-key": self.api_key,
            "Content-Type": "application/json"
        }
        response = requests.post(url, json=payload, headers=headers)
        if response.ok:
            return response.content
        else:
            print("TTS API Error:", response.status_code, response.text)
        return None

# Example usage:
# tts = ElevenLabsTTS()
# audio = tts.synthesize("Hello, world!", voice_id="your_voice_id")
# with open("output.wav", "wb") as f:
#     f.write(audio)
