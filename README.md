# 🎙️ Voice-Based English ↔ Japanese Translator

## 📌 Overview
This project is a **production-ready NLP and Speech Processing system** that performs **speech-to-speech translation** between **English and Japanese**.

Users can **record their voice directly in the browser**, and the system automatically:
1. Converts speech to text  
2. Translates the text  
3. Plays translated speech  
4. Displays confidence and quality metrics  
5. Highlights words in sync with audio  

The system is designed with **accuracy, transparency, and scalability** in mind.

---

## ✨ Key Features
- 🎤 **Browser-based voice recording** (Start / Stop control)
- 🧠 **High-accuracy speech recognition using OpenAI Whisper**
- 🌐 **English ↔ Japanese translation**
- 🔊 **Text-to-speech output (in-memory, no files saved)**
- 🟨 **Word-by-word highlighting synced with audio**
- 📊 **ASR Confidence score**
- 🔇 **Silence ratio analysis (audio quality indicator)**
- 🖥️ **Clean and professional Streamlit UI**

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

Voice Input
↓
Silence Trimming
↓
Speech Recognition (Whisper)
↓
Text + Confidence + Word Timestamps
↓
Translation (EN ↔ JA)
↓
Speech Output + UI Highlighting


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

**Dikshitha A**  
Computer Science Engineering  
Interests: **AI / ML · NLP · Speech Processing**  
GitHub: [https://github.com/DikshithaAnand](https://github.com/DikshithaAnand)

