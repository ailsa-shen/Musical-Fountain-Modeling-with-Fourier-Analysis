import numpy as np
import scipy.io.wavfile as wav
from scipy.fft import fft
import matplotlib.pyplot as plt
import os

# defining a function 'proc_wav' that processes a WAV file given its file path
def proc_wav(path):
    sample_rate, audio_data = wav.read(path) 
    window_size = int(0.1 * sample_rate) 
    num_windows = len(audio_data) // window_size 
    peaks = [] 

    for i in range(num_windows):
        start = i * window_size
        end = (i + 1) * window_size 
        windowed_data = audio_data[start:end] 
        fft_result = fft(windowed_data) # performing fast Fourier transform of cureent window
        frequencies = np.fft.fftfreq(window_size, 1 / sample_rate)
        amplitudes = np.abs(fft_result)
        peaks.append(np.max(amplitudes)) # calculating max amplitudes and adding it to the 'peaks'
    return peaks 

path_to_file = os.path.join(os.path.expanduser("~"), "Desktop", "monoclip2.wav")

if __name__ == '__main__':
    proc_wav(path_to_file) 