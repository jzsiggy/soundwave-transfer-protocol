from sender import Sender
from receiver import Receiver


sender = Sender(fs=48000)
sender.get_num()
sender.get_freq(5)
sender.get_rec()

receiver = Receiver(fs=48000)
receiver.play_recording()
receiver.plot_recording()
receiver.calcFFT()