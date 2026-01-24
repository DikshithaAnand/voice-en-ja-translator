import numpy as np
from scipy.io import wavfile
import tempfile


def trim_silence(wav_path, energy_threshold=300):
    sample_rate, audio = wavfile.read(wav_path)

    if audio.ndim > 1:
        audio = audio[:, 0]

    frame_size = int(sample_rate * 0.03)  # 30 ms
    voiced_frames = []
    total_frames = 0
    speech_frames = 0

    for i in range(0, len(audio), frame_size):
        frame = audio[i:i + frame_size]
        if len(frame) == 0:
            continue

        total_frames += 1
        energy = np.mean(np.abs(frame))

        if energy > energy_threshold:
            speech_frames += 1
            voiced_frames.extend(frame)

    silence_ratio = 1.0
    if total_frames > 0:
        silence_ratio = 1 - (speech_frames / total_frames)

    if not voiced_frames:
        return wav_path, silence_ratio

    cleaned_audio = np.array(voiced_frames, dtype=np.int16)

    cleaned_path = tempfile.NamedTemporaryFile(
        suffix=".wav",
        delete=False
    ).name

    wavfile.write(cleaned_path, sample_rate, cleaned_audio)
    return cleaned_path, silence_ratio
