from gtts import gTTS
import io

def text_to_speech_bytes(text, language):
    """
    Converts text to speech and returns audio bytes.
    No files are saved to disk.
    """

    lang_code = "en" if language == "English" else "ja"

    mp3_fp = io.BytesIO()
    tts = gTTS(text=text, lang=lang_code)
    tts.write_to_fp(mp3_fp)

    mp3_fp.seek(0)
    return mp3_fp.read()
