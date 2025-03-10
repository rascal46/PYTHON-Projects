import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

def record(duration,filename):
    
    sample = 44100 #sample rate

    print("Recording started...")

    audio = sd.rec(int(duration * sample), samplerate=sample, channels=1, dtype=np.int16)
#   variable      start      total no. of samples       sample rate         mono      data type=16 bit int

    #sample is a single data point in digital audio. It is a measurement of the amplitude of the sound wave at a particular time.

    sd.wait() #stops recording

    print("Recording stopped...")

    write(filename, sample, audio)

#________________________________________________________
    
def save(filename, sample, audio):
    write(filename, sample, audio)
    print(f"Recording saved as {filename}")

#________________________________________________________

def main():
    duration = int(input("enter duration of recording:"))
    filename = "recorded_audio.wav"

    record(duration,filename)

    print("Recording saved as recorded_audio.wav")



main()
