# Musical Fountain Modeling with Fourier Analysis

## Project Overview
This project models a dynamic and synchronized musical fountain using Fourier analysis. The goal is to visually represent music by creating a synchronized water fountain display driven by audio signals. The audio signals are decomposed into frequency components using Fast Fourier Transform (FFT) and mapped to visual particles that simulate the motion of water jets in the fountain. The visual particles' height and movement are dynamically adjusted in real-time to match the audio amplitude, bringing the music to life as a visually immersive fountain  display.

## Features
- Audio Signal Processing: The audio is divided into 0.1-second windows, each analyzed using Fast Fourier Transform (FFT) to extract the frequency components and dominant amplitudes.
- Fourier Analysis: By performing FFT, the project extracts the dominant frequency peaks and their amplitudes, which are used to influence the behavior of the particles in the fountain.
- Particle Visualization Model: This model simulates the motion of water jets using particles in Python, where each particle’s height and movement correspond to the audio peaks.
  Real-Time Synchronization: The particle system dynamically responds to the audio file's playback, creating a synchronized fountain display in real-time.

## Libraries Used
- NumPy for FFT and signal processing
- SciPy for handling audio data
- Pygame for handling real-time particle visualization, drawing, and animation.
- Matplotlib for data plotting (optional for debugging)

## How It Works
- Audio Processing: The audio file is read and processed in segments of 0.1 seconds. For each segment, Fast Fourier Transform (FFT) is applied to extract frequency components and amplitudes. A list of frequency peaks is obtained by analyzing the maximum amplitude for each segment.
- Frequency Mapping: The amplitude peaks are scaled to fit within the screen dimensions for the particle simulation (from 0 to 480, representing the height of the screen). 
- Particle Simulation: Pygame is used to generate particles that simulate water jets in the fountain. The height of each particle corresponds to the amplitude of the audio signal at that particular moment in time. Particles are updated in real-time as the music plays, moving according to the mapped audio amplitudes.
- Real-Time Updates: The system continuously updates particle positions, allowing the fountain simulation to change dynamically based on the audio’s frequency content and amplitude.

## Potential Improvements
- Increase granularity by reducing segment sizes to capture faster transitions.
- Implement 3D visualization with light and color effects.
- Conduct physical testing with an actual musical fountain system.
