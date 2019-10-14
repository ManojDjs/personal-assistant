import sounddevice as sd
from scipy.io.wavfile import write
import time
import speech_recognition as sr
import os
from pydub import AudioSegment

fs = 44100  # Sample rate
seconds = 3  # Duration of recording
k=os.getcwd()
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('outpu.mp3', fs, myrecording)  # Save as WAV file
time.sleep(0.5)
# convert mp3 file to wav
sound = AudioSegment.from_mp3(k+'/'+"outpu.mp3")
sound.export("transcript.wav", format="wav")
# transcribe audio file
AUDIO_FILE = "transcript.wav"

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file
        print("Transcription: " + r.recognize_google(audio))
