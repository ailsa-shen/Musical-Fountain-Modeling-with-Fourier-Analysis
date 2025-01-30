import numpy as np
import matplotlib.pyplot as plt
import os
import librosa

# setting the path to the audio file (in my desktop "Math EE" folder)
path_to_file = os.path.join(os.path.expanduser("~"), "Desktop", "Math EE", "monoclip2.wav")

clip, sr = librosa.load(path_to_file)

# computing Fourier transform of the audio
clip_ft = np.fft.fft(clip)
magnitude_spectrum_clip = np.abs(clip_ft)

# function to plot the magnitude spectrum
def plot_magnitude_spectrum(signal, title, sr, f_ratio=1):  
    ft = np.fft.fft(signal)  
    magnitude_spectrum = np.abs(ft)  
    plt.figure(figsize=(18, 5))
    frequency = np.linspace(0, sr, len(magnitude_spectrum))  
    num_frequency_bins = int(len(frequency) * f_ratio)  
    plt.plot(frequency[:num_frequency_bins], magnitude_spectrum[:num_frequency_bins])
    plt.xlabel("Frequency (Hz)")
    plt.title(title)
    plt.show()  

# plotting
plot_magnitude_spectrum(clip, "Magnitude Spectrum", sr, 1)