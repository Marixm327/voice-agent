"""
LLM & Context Management for Voice Agent
Company: SpaceMarvel.ai
"""
import os
import requests
from typing import List, Dict, Any

class GeminiLLM:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("GOOGLE_AI_STUDIO_API_KEY")
        self.api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

    def generate_response(self, prompt: str) -> str:
        payload = {
            "contents": [
                {"parts": [{"text": prompt}]}
            ]
        }
        headers = {
            "Content-Type": "application/json",
            "X-goog-api-key": self.api_key
        }
        response = requests.post(self.api_url, json=payload, headers=headers)
        if response.ok:
            data = response.json()
            try:
                return data["candidates"][0]["content"]["parts"][0]["text"]
            except Exception as e:
                print("Gemini API response parsing error:", e, data)
                return "Error parsing Gemini response."
        else:
            print("Gemini API Error:", response.status_code, response.text)
            return "Sorry, I couldn't process your request."

# Example usage:
# llm = GeminiLLM()
# reply = llm.generate_response("What can you do?")
