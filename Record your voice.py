import sounddevice as sd
import wavio
import numpy as np


def record_audio(filename, sample_rate=44100):

    print("Press 'Enter' to start recording. Press 'Enter' again to stop recording.")
    input()
    print("Recording started...")

    recording = []
    def callback(indata, frames, time, status):
        recording.append(indata.copy())
    
    stream = sd.InputStream(samplerate=sample_rate, channels=2, callback=callback, dtype='int16')
    with stream:
        input()
    print("Recording stopped.")

    recording = np.concatenate(recording, axis=0)
    wavio.write(filename, recording, sample_rate, sampwidth=2)
    print(f"Audio saved to {filename}")

filename = input("enter the name of file : ")
filename += ".wav"
record_audio(filename)