from matplotlib import pyplot as plt
import numpy as np
import sounddevice as sd

start_idx = 0

class Sender():
    def __init__(self, fs):
        self.sound_device = 0
        self.fs = fs
        self.num = None
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

    def get_num(self):
        num = int(input('choose number between 0-9: '))
        while (num < 0 or num > 9):
            num = int(input ('Invalid Number - choose again -- '))
        
        self.num = num

    def generateSin(self, freq, x):
        return np.sin(freq*x*2*np.pi)

    def get_freq(self, time):
        n = time * self.fs
        y = np.zeros(n)
        x = np.linspace(0.0, time, n)

        freq_tuple = self.hash[self.num]
        for freq in freq_tuple:
            y += self.generateSin(freq, x)

        self.freq = y

    def play_tone(self, amplitude):
        freq = self.freq * amplitude
        
        sd.play(freq, self.fs)
        sd.wait()

        plt.figure()
        plt.plot(freq[:500], '.-')
        plt.show()
        


sender = Sender(48000)
sender.get_num()
sender.get_freq(5)
sender.play_tone(1)




# from scipy.fftpack import fft, fftshift

# def calcFFT(signal, fs):
#     N  = len(signal)
#     T  = 1/fs
#     xf = np.linspace(-1.0/(2.0*T), 1.0/(2.0*T), N)
#     yf = fft(signal)
#     X, Y = xf, fftshift(yf)

#     plt.figure()
#     plt.stem(X,np.abs(Y))
#     plt.xlim(0, 2000)
#     plt.show()

# calcFFT(sender.freq, 48000)