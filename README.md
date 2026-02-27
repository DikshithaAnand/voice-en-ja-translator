# 🎙️ Voice-Based English ↔ Japanese Translator

## 📌 Overview

This project is a **production-ready NLP and speech processing system** designed to perform seamless **speech-to-speech translation** between **English and Japanese**.

Users can record their voice directly within the browser, and the system automatically:

1. Converts spoken audio into text (Speech-to-Text)  
2. Translates the recognized text into the target language  
3. Generates and plays the translated speech (Text-to-Speech)  
4. Displays confidence scores and audio quality metrics  
5. Highlights words in real time, synchronized with playback  

The system is engineered with a strong emphasis on **accuracy, explainability, performance, and scalability**, making it suitable for real-world deployment.


---

## ✨ Key Features
- 🎤 **In-browser voice recording** with intuitive start/stop controls  
- 🧠 **Accurate speech recognition powered by OpenAI Whisper**  
- 🌐 **Bidirectional English ↔ Japanese translation**  
- 🔊 **Real-time text-to-speech playback (no audio files stored)**  
- 🟨 **Word-level highlighting synchronized with speech audio**  
- 📊 **Automatic ASR confidence scoring**  
- 🔇 **Silence ratio detection for audio quality assessment**  
- 🖥️ **Clean, responsive, and professional Streamlit interface**

---

## 🧠 Why This Project Is Different
Unlike basic speech apps, this system:
- Exposes **confidence and uncertainty**
- Avoids saving audio files (memory-safe & deployable)
- Uses **word-level timestamps** for precise UI sync
- Separates **audio capture, ASR, translation, and TTS** cleanly

This makes it suitable for **real-world applications**, demos, and interviews.

---

## 🛠️ Tech Stack
- **Python**
- **Streamlit** – UI & frontend
- **OpenAI Whisper** – Speech recognition (offline, multilingual)
- **Google Translate API** – Text translation
- **gTTS** – Text-to-speech
- **NumPy & SciPy** – Audio processing
- **Git & GitHub** – Version control

---

## 🔄 System Workflow

```text
┌──────────────────────────────┐
│        🎤 Voice Input        │
│  (Browser Audio Recording)   │
└───────────────┬──────────────┘
                ↓
┌──────────────────────────────┐
│      ✂️ Silence Trimming     │
│   (Energy / VAD Processing)  │
└───────────────┬──────────────┘
                ↓
┌──────────────────────────────┐
│  🧠 Speech Recognition       │
│       (Whisper Model)        │
└───────────────┬──────────────┘
                ↓
┌──────────────────────────────┐
│ 📝 Text Output + Confidence  │
│   + Word-Level Timestamps    │
└───────────────┬──────────────┘
                ↓
┌──────────────────────────────┐
│ 🌐 Translation (EN ↔ JA)     │
│     (Neural Translation)     │
└───────────────┬──────────────┘
                ↓
┌──────────────────────────────┐
│ 🔊 Speech Output (TTS)       │
│ + Real-Time UI Highlighting  │
└──────────────────────────────┘
```
---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/DikshithaAnand/voice-en-ja-translator.git
cd voice-en-ja-translator

```
2️⃣ Create & activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate

```

3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

4️⃣ Run the application

```bash
streamlit run app.py
```


Open your browser at:

```bash
http://localhost:8501

```

🧪 How to Use

- Click 🎤 Record

- Speak in English or Japanese

- Click Stop

- View:

   - Recognized text

   - Translation

   - Confidence & silence metrics

   - Word highlighting

- Listen to translated speech directly on screen

## 🧠 Speech Recognition

The system uses **OpenAI Whisper** for multilingual speech recognition.

Whisper was chosen because it:
- Works **offline**
- Handles **accents and pauses** effectively
- Provides **word-level timestamps**
- Supports **automatic language detection**

---

## 🔇 Audio Preprocessing

Before transcription, the audio is processed using **energy-based Voice Activity Detection (VAD)** to remove silence segments.

This preprocessing step improves:
- **Transcription accuracy**
- **Sentence completeness**
- **Confidence reliability**

## 🚀 Future Enhancements

Planned improvements to extend the system’s capabilities include:
- **Automatic language detection** to remove manual language selection
- **Conversation / multi-turn mode** for context-aware translation
- **Japanese romanization (Romaji) support** for language learners
- **Dark mode UI** for improved accessibility and user experience
- **Cloud deployment** using Streamlit Cloud or Docker
- **Support for additional languages** beyond English and Japanese

---

## 👩‍💻 Author

**Dikshitha Anand**
Computer Science and Engineering  
Interests: **Artificial Intelligence / Machine Learning · NLP · Speech Processing**  
GitHub: [https://github.com/DikshithaAnand](https://github.com/DikshithaAnand)

