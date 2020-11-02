from matplotlib import pyplot as plt
import sounddevice as sd
import numpy as np
from scipy.fftpack import fft, fftshift
from scipy.io.wavfile import write
import soundfile as sf

class Receiver:
    def __init__(self, fs, recording=None):
        self.fs = fs
        self.recording = recording

    def record(self, seconds):
        duration = seconds
        self.recording = sd.rec(int(duration * self.fs), samplerate=self.fs, channels=1)
        sd.wait()

    def save_rec(self, filename):
        write(filename, self.fs, self.recording)
        audio, samplerate = sf.read('recording.wav')
        self.recording = audio

    def plot_recording(self):
        plt.plot(self.recording)
        plt.grid()
        plt.show()

    def play_recording(self):
        sd.play(self.recording, self.fs)
        sd.wait()

    def calcFFT(self):
        signal = self.recording
        fs = self.fs
        
        N  = len(signal)
        T  = 1/fs
        xf = np.linspace(-1.0/(2.0*T), 1.0/(2.0*T), N)
        yf = fft(signal)
        X, Y = xf, fftshift(yf)

        plt.figure()
        plt.plot(X, np.abs(Y))
        plt.grid()
        plt.show()


receiver = Receiver(fs=48000)
receiver.record(seconds=2)
receiver.save_rec('recording.wav')
receiver.plot_recording()
receiver.calcFFT()