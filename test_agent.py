"""
Test script to connect and validate Memory, LLM, STT, and TTS modules
"""
from memory.memory import ConversationMemory
from llm.llm import GeminiLLM
from tts.tts import ElevenLabsTTS
# from stt.whisper_stt import WhisperSTT  # Uncomment if you have an audio file to test
import os

# Load API keys from environment
os.environ["GOOGLE_AI_STUDIO_API_KEY"] = "AIzaSyDpTtHqcPWniH6kTRoeWWHVJ8RiV2dXyHE"
os.environ["ELEVENLABS_API_KEY"] = "sk_dc5e49cfab8c5d4a594ba1745a73eb7b845c87fdb0e1f011"

# Initialize modules
memory = ConversationMemory()
llm = GeminiLLM()
tts = ElevenLabsTTS()
# stt = WhisperSTT()  # Uncomment if you want to test STT

# Simulate a conversation
session_id = "customer_001"
user_message = "Hello, I want to know more about your AI automation services."
memory.add_message(session_id, "user", user_message)
history = memory.get_history(session_id)

# Generate LLM response
llm_response = llm.generate_response(user_message)
memory.add_message(session_id, "agent", llm_response)
print("LLM Response:", llm_response)

# Synthesize response with TTS
# You may need to specify a valid voice_id for ElevenLabs
voice_id = "zubqz6JC54rePKNCKZLG"
audio = tts.synthesize(llm_response, voice_id=voice_id)
if audio:
    with open("agent_response.wav", "wb") as f:
        f.write(audio)
    print("TTS audio saved as agent_response.wav")
else:
    print("TTS synthesis failed.")

# Optional: Test STT (requires an audio file)
# audio_path = "path_to_audio.wav"
# transcribed_text = stt.transcribe(audio_path)
# print("Transcribed text:", transcribed_text)
