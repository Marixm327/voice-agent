"""
Streamlit Voice Agent UI
Company: SpaceMarvel.ai
"""
import time
import streamlit as st
from streamlit_webrtc import webrtc_streamer, AudioProcessorBase
from memory.memory import ConversationMemory
from llm.llm import GeminiLLM
#from agent.agent import agent_respond
from stt.whisper_stt import WhisperSTT
import numpy as np

def agent_respond(text):
    return f"[STT OK] You said: {text}"

st.set_page_config(page_title="Voice Agent", layout="centered")
st.title("SpaceMarvel Voice Agent")

# Session state for memory
if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationMemory()
if "history" not in st.session_state:
    st.session_state["history"] = []

# Display chat history
st.subheader("Conversation History")
for msg in st.session_state["history"]:
    st.markdown(f"**{msg['role'].capitalize()}:** {msg['message']}")

# Microphone input (audio streaming)
st.subheader("Talk to the Agent")
st.info("Press Start to begin speaking. Your audio will be processed and responded to by the agent.")

class AudioProcessor(AudioProcessorBase):
    def __init__(self):
        super().__init__()
        self.stt = WhisperSTT()

    def recv(self, frame):
        # Convert audio frame to numpy array
        audio_data = frame.to_ndarray().astype("float32")

        # Transcribe directly from memory (no temp file)
        text, language = self.stt.transcribe_audio(audio_data)


        stt_latency = stt_end - stt_start
        print(f"[LATENCY] STT time: {stt_latency:.3f} seconds")


        if text:
            # Store detected language for future multilingual routing
            st.session_state["last_language"] = language

            response = agent_respond(text)
            st.session_state["history"].append({"role": "user", "message": text})
            st.session_state["history"].append({"role": "agent", "message": response})

        return frame


webrtc_streamer(key="voice-agent", audio_processor_factory=AudioProcessor)

# Text input fallback
user_text = st.text_input("Type your message:")
if st.button("Send") and user_text:
    response = agent_respond(user_text)
    st.session_state["history"].append({"role": "user", "message": user_text})
    st.session_state["history"].append({"role": "agent", "message": response})
    st.experimental_rerun()
