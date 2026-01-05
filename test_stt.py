import time
import numpy as np
from stt.whisper_stt import WhisperSTT

audio = np.zeros(16000, dtype="float32")

stt = WhisperSTT()

start = time.time()
text, language = stt.transcribe_audio(audio)
end = time.time()

print("STT latency:", round(end - start, 3), "seconds")
print("Text:", text)
print("Language:", language)
