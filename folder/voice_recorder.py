import sounddevice
from scipy.io.wavfile import write 

fs=44100

second=int(input("enter the recording time in seconds:"))
print("recording.../n")
record_voice=sounddevice.rec(int(second * fs), samplerate=fs, channels=2)
sounddevice.wait()
write("myRecoding.wav", fs, record_voice)
print("recording is done please check your folder to listen recording")