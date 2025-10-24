import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Voice Agent", layout="centered")
st.title("SpaceMarvel Voice Agent with LiveKit")

st.subheader("LiveKit Audio Room")
st.info("Connect and talk in real-time using LiveKit. Your audio will be processed by the AI agent.")

# Replace with your LiveKit server URL, room name, and token
LIVEKIT_URL = "wss://cold-5rfc4yin.livekit.cloud"
TOKEN = "APIJSdkZDuScSgG"
ROOM_NAME = "voice-agent-room"

livekit_html = f"""
<!DOCTYPE html>
<html>
  <head>
    <script src='https://cdn.jsdelivr.net/npm/livekit-client/dist/livekit-client.min.js'></script>
  </head>
  <body>
    <button onclick='connectLiveKit()'>Connect to LiveKit</button>
    <script>
      async function connectLiveKit() {{
        const {{ Room, createLocalTracks }} = window.livekitClient;
        const room = new Room();
        await room.connect('{LIVEKIT_URL}', '{TOKEN}');
        const tracks = await createLocalTracks({{ audio: true }});
        room.localParticipant.publishTrack(tracks[0]);
        room.on('trackSubscribed', (track, publication, participant) => {{
          if (track.kind === 'audio') {{
            track.attach(document.body);
          }}
        }});
      }}
    </script>
  </body>
</html>
"""

components.html(livekit_html, height=400)

st.subheader("Conversation History")
# ...existing code for chat history and text input...
