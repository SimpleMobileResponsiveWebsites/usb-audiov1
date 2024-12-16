import streamlit as st
import sounddevice as sd
import numpy as np
import wavio
from io import BytesIO
import time

# Function to record audio
def record_audio(duration, samplerate):
    st.write("Recording...")
    audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='float32')
    sd.wait()  # Wait until the recording is finished
    st.write("Recording complete!")
    return audio_data

# Function to save the recorded audio as WAV
def save_wav(audio_data, samplerate):
    buffer = BytesIO()
    wavio.write(buffer, audio_data, samplerate, sampwidth=2)
    buffer.seek(0)
    return buffer

# Streamlit App
st.title("Audio Recorder")
st.markdown("Record audio using a USB interface directly in your browser!")

# User input for recording duration
duration = st.number_input("Enter duration of recording (seconds):", min_value=1, max_value=60, value=5)
samplerate = st.number_input("Enter sampling rate (Hz):", min_value=8000, max_value=44100, value=44100)

if st.button("Start Recording"):
    audio_data = record_audio(duration, samplerate)

    # Playback the recorded audio
    st.audio(save_wav(audio_data, samplerate), format="audio/wav")

    # Download the audio
    wav_file = save_wav(audio_data, samplerate)
    st.download_button("Download Recording", wav_file, file_name="recording.wav")

st.markdown("---")
st.info("Make sure your USB microphone is connected and working.")
