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

## 🧠 Why This Project Stands Out

Unlike basic speech translation applications, this system is designed with production-level considerations:

- **Confidence & Uncertainty Exposure**  
  Displays model confidence scores to improve transparency and user trust.

- **Memory-Safe Architecture**  
  Avoids storing audio files permanently, making it safer and deployment-friendly.

- **Word-Level Timestamping**  
  Enables precise UI synchronization with real-time word highlighting.

- **Modular System Design**  
  Clearly separates audio capture, speech recognition (ASR), translation, and text-to-speech (TTS) components for maintainability and scalability.

Because of these design decisions, the project is suitable for:

- Real-world deployment scenarios  
- Technical demonstrations  
- AI/ML interviews and portfolio showcases  

---

## 🛠️ Tech Stack

### 👨‍💻 Core Language
- **Python** – Backend logic, audio processing, and AI integration

### 🎨 Frontend / UI
- **Streamlit** – Interactive web interface and real-time UI rendering

### 🧠 Speech & NLP
- **OpenAI Whisper** – Offline multilingual speech recognition  
- **Google Translate API** – Neural text translation (EN ↔ JA)  
- **gTTS (Google Text-to-Speech)** – Speech synthesis for translated output  

### 🔊 Audio Processing
- **NumPy & SciPy** – Signal processing, waveform handling, and silence trimming  

### 🔧 DevOps & Version Control
- **Git & GitHub** – Source control, collaboration, and project management

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

To further strengthen the system and expand its real-world usability, the following improvements are planned:

- 🌍 **Automatic Language Detection**  
  Eliminate manual language selection by dynamically identifying the spoken language.

- 💬 **Conversation / Multi-Turn Mode**  
  Enable context-aware translations to support natural, back-and-forth dialogue.

- 🇯🇵 **Japanese Romanization (Romaji) Support**  
  Provide Romaji output alongside Japanese text to assist language learners.

- 🌙 **Dark Mode UI**  
  Improve accessibility and enhance user experience with an optimized  best dark interface.
  

- ☁️ **Cloud Deployment**  
  Deploy using **Streamlit Cloud** or **Docker** for scalable and production-grade hosting.

- 🌐 **Multi-Language Expansion**  
  Extend support beyond English and Japanese to additional global languages.
---

## 👩‍💻 Author

**Dikshitha Anand**
Computer Science and Engineering  
Interests: **Artificial Intelligence / Machine Learning · NLP · Speech Processing**  
GitHub: [https://github.com/DikshithaAnand](https://github.com/DikshithaAnand)

