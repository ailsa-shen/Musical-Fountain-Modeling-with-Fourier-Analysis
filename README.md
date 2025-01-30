# Musical Fountain Modeling with Fourier Analysis

## Project Overview
This project models a dynamic and synchronized musical fountain using Fourier analysis. By decomposing audio signals into frequency components and mapping these to visual particle simulations, it brings music to life as a visually immersive fountain display. The particle visualization model responds dynamically to audio amplitude changes in real-time, creating a synchronization between sound and virtual fountain particles.

## Features
- Audio Signal Processing: Analyzes audio signals by dividing them into 0.1-second windows for detailed frequency extraction using Fast Fourier Transform (FFT).
- Fourier Analysis: Extracts dominant frequency peaks and amplitudes from audio segments.
- Particle Visualization Model: Particle-based fountain visualization in Python where each particle's height and movement correspond to audio peaks.
  Real-Time Synchronization: Ensures fountain particles dynamically respond as the audio file plays.

## Libraries Used
- NumPy for FFT and signal processing
- SciPy for handling audio data
- Pygame for particle visualization
- Matplotlib for data plotting (optional for debugging)

## How It Works
- Audio Processing: The code reads the audio file and splits it into 0.1-second windows. FFT is applied to extract frequency components and calculate amplitude peaks.
- Frequency Mapping: Audio peaks are scaled between 0 and 480 to fit the screen height for particle visualization.
- Particle Simulation: Particles are generated and moved dynamically according to the mapped audio amplitudes. Each particle represents a synchronized water jet.
- Real-Time Updates: Pygame handles real-time updates, continuously adjusting particle heights as the music plays.

## Potential Improvements
- Increase granularity by reducing segment sizes to capture faster transitions.
- Implement 3D visualization with light and color effects.
- Conduct physical testing with an actual musical fountain system.
