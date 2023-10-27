import sounddevice as sd
import numpy as np
import wave

# Set the recording duration and filename
duration = 20  # seconds
filename = "recorded_audio.wav"

# Define the callback function to record audio
def audio_callback(indata, frames, time, status):
    if status:
        print("Error:", status)
    if len(indata) > 0:
        audio_frames.append(indata.copy())

# Initialize audio recording
audio_frames = []
with sd.InputStream(callback=audio_callback):
    sd.sleep(int(duration * 1000))

# Save the recorded audio to a WAV file
audio_data = np.concatenate(audio_frames, axis=0)
with wave.open(filename, "wb") as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(44100)
    wf.writeframes(audio_data.tobytes())

