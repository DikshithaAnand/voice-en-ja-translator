import streamlit as st
import json
from audio_recorder_streamlit import audio_recorder
from speech_to_text import audio_to_text
from translate import translate_text
from text_to_speech import text_to_speech_bytes
from streamlit.components.v1 import html

st.set_page_config(
    page_title="Voice EN ↔ JA Translator",
    layout="centered"
)

# 🎨 UI Styling for better visibility
st.markdown(
    """
    <style>
    .en-text {
        font-size: 20px;
        line-height: 1.7;
        color: #1f2937; /* dark slate */
        background-color: #f9fafb;
        padding: 14px;
        border-radius: 8px;
        border: 1px solid #e5e7eb;
        margin-bottom: 12px;
    }

    .jp-text {
        font-size: 22px;
        line-height: 1.8;
        color: #111827;
        background-color: #eef2ff;
        padding: 16px;
        border-radius: 8px;
        border: 1px solid #c7d2fe;
        margin-bottom: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🎙️ Voice-Based English ↔ Japanese Translator")
st.caption("Press record ▶ speak ▶ stop ⏹️ to translate accurately")

# Language selection (will be removed in Level 2)
source_lang = st.selectbox("Source Language", ["English", "Japanese"])
target_lang = "Japanese" if source_lang == "English" else "English"

st.divider()

# 🎤 Voice Recorder (browser-based)
audio_bytes = audio_recorder(
    text="🎤 Record / Stop",
    recording_color="#ff4b4b",
    neutral_color="#6aa36f",
    icon_name="microphone",
    icon_size="2x"
)

if audio_bytes:
    st.success("✅ Recording completed")

    # 🔥 ASR with timestamps
    result = audio_to_text(audio_bytes, source_lang)

    if result and result["text"]:
        # 📝 Recognized English text (high visibility)
        st.markdown("### 📝 Recognized Text")
        st.markdown(
            f"<div class='en-text'>{result['text']}</div>",
            unsafe_allow_html=True
        )

        # 📊 Transparency metrics
        col1, col2 = st.columns(2)
        with col1:
            st.metric("ASR Confidence", f"{int(result['confidence'] * 100)}%")
        with col2:
            st.metric("Silence Ratio", f"{int(result['silence_ratio'] * 100)}%")

        if result["confidence"] < 0.6:
            st.warning("⚠️ Low confidence transcription. Please speak clearly.")

        # 🌐 Translation
        translated = translate_text(
            result["text"],
            source_lang,
            target_lang
        )

        # 🌐 Japanese text (extra readable)
        st.markdown("### 🌐 Translated Text")
        st.markdown(
            f"<div class='jp-text'>{translated}</div>",
            unsafe_allow_html=True
        )

        # 🔊 INPUT audio playback (screen only)
        st.audio(audio_bytes, format="audio/wav")

        # 🟨 Word highlighting synced with input audio
        words = result["words"]

        highlight_html = f"""
        <div style="font-size:18px; line-height:2;">
        {" ".join([
            f'<span id="w{i}" style="padding:2px;">{w["word"]}</span>'
            for i, w in enumerate(words)
        ])}
        </div>

        <script>
        const audio = document.querySelector("audio");
        const words = {json.dumps(words)};

        audio.ontimeupdate = () => {{
            const t = audio.currentTime;
            words.forEach((w, i) => {{
                const el = document.getElementById("w" + i);
                if (t >= w.start && t <= w.end) {{
                    el.style.backgroundColor = "#ffe066";
                }} else {{
                    el.style.backgroundColor = "transparent";
                }}
            }});
        }};
        </script>
        """

        html(highlight_html, height=200)

        # 🔊 TRANSLATED voice (screen only, in-memory)
        tts_audio = text_to_speech_bytes(translated, target_lang)
        st.audio(tts_audio, format="audio/mp3")

    else:
        st.error("❌ Speech not recognized. Please try again.")
