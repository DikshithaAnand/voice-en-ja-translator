import whisper
import tempfile
import os
from utils.vad import trim_silence

# Load Whisper model once (important for performance)
model = whisper.load_model("base")


def audio_to_text(audio_bytes, language):
    """
    Converts audio bytes to text using Whisper.
    Returns text, word timestamps, confidence, and silence ratio.
    """

    temp_file = tempfile.NamedTemporaryFile(
        suffix=".wav",
        delete=False
    )

    cleaned_path = None

    try:
        # 1️⃣ Save raw audio bytes to temp WAV
        temp_file.write(audio_bytes)
        temp_file.close()

        # 2️⃣ Trim silence (energy-based VAD)
        cleaned_path, silence_ratio = trim_silence(temp_file.name)

        # 3️⃣ Whisper transcription with word timestamps
        result = model.transcribe(
            cleaned_path,
            language="en" if language == "English" else "ja",
            fp16=False,
            word_timestamps=True,
            verbose=False
        )

        text = result["text"].strip()

        # 4️⃣ Collect word timestamps + duration-weighted confidence
        words = []
        weighted_confidence_sum = 0.0
        total_duration = 0.0

        for segment in result.get("segments", []):
            avg_logprob = segment.get("avg_logprob", -1)
            duration = segment.get("end", 0) - segment.get("start", 0)

            if duration > 0:
                weighted_confidence_sum += avg_logprob * duration
                total_duration += duration

            for w in segment.get("words", []):
                words.append({
                    "word": w["word"],
                    "start": round(w["start"], 2),
                    "end": round(w["end"], 2)
                })

        # 5️⃣ Final confidence calculation (FIXED)
        if total_duration > 0:
            avg_logprob = weighted_confidence_sum / total_duration
            confidence = round(min(1.0, max(0.0, avg_logprob + 1)), 2)
        else:
            confidence = 0.0

        return {
            "text": text,
            "words": words,
            "confidence": confidence,
            "silence_ratio": round(silence_ratio, 2)
        }

    finally:
        # 6️⃣ Cleanup temp files (no disk usage)
        if os.path.exists(temp_file.name):
            os.remove(temp_file.name)
        if cleaned_path and os.path.exists(cleaned_path):
            os.remove(cleaned_path)
