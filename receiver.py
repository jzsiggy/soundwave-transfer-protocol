from matplotlib import pyplot as plt
import sounddevice as sd
import numpy as np
from scipy.fftpack import fft, fftshift
from scipy.io.wavfile import write
import soundfile as sf
import peakutils

class Receiver:
    def __init__(self, fs, recording=None):
        self.fs = fs
        self.recording = recording
        self.hash = {
            0 : [941, 1336],
            1 : [697, 1209],
            2 : [697, 1336],
            3 : [697, 1477],
            4 : [770, 1209],
            5 : [770, 1336],
            6 : [770, 1477],
            7 : [852, 1209],
            8 : [852, 1336],
            9 : [852, 1477],
        }

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
        self.fftX = X
        self.fftY = Y
        
    def get_number(self):
        index = peakutils.indexes(np.abs(self.fftY), thres=0.3, min_dist=50)
        print("index de picos {}" .format(index))
        frequencies = []
        for freq in self.fftX[index]:
            if freq > 0:
                print("freq de pico --> {}" .format(int(freq)))
                frequencies.append(int(freq))
                
        for number in self.hash:
            print(frequencies, self.hash[number])
            if (np.array(frequencies)==np.array(self.hash[number])).all():
                print(number)
                break


receiver = Receiver(fs=48000)
receiver.record(seconds=2)
receiver.save_rec('recording.wav')
receiver.plot_recording()
receiver.calcFFT()
receiver.get_number()