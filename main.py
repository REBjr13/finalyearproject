from vosk import Model, KaldiRecognizer
import os
import pyaudio
import pyttsx3


# Speech Synthesis model
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


#Speech Recognition model

model = Model("model")
rec = KaldiRecognizer(model, 16000)

#opens microphone for listening
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

while True:
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        text = rec.Result()
        
        print(text)
        speak(text)