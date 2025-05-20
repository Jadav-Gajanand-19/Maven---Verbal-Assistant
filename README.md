![Maven Logo](maven poster.png)

# Maven - Your Verbal Assistant 🎙️

Maven is a simple command-line-based verbal assistant using Python. It can:
- Speak typed sentences aloud
- Change its voice
- Read from text files
- Convert text into MP3 audio files using Google Text-to-Speech

## 🚀 Features

1. Text-to-speech using `pyttsx3`
2. MP3 conversion using `gTTS`
3. Read any `.txt` file aloud
4. Save spoken content to `.mp3` files

## 🛠️ Requirements

- Python 3.7+
- pyttsx3
- gTTS

## 🔧 Installation

```bash
pip install -r requirements.txt
```

## ▶️ Usage

Run the assistant:
```bash
python maven_main.py
```

### Menu Options:
- **1**: Speak user input aloud
- **2**: Change voice
- **3**: Read aloud from a file
- **4**: Convert text to MP3 file
- **-1**: Exit

## 📂 Sample Files

- `sample.txt`: Example file for "Read from file" option
- `sample.mp3`, `success.mp3`: Generated MP3 files for demo

## 📜 License

This project is licensed under the MIT License.

---
