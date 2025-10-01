
```markdown
# 🎙️ PodcastSuite

**PodcastSuite** is a Python-based web application that simplifies the podcast post-production process. It provides tools for noise reduction, silence removal, speaker diarization, and transcription — all through an intuitive web interface.

## 🚀 Features

- ✅ **Noise Reduction** – Clean up background noise automatically.
- ✂️ **Silence Removal** – Trim unnecessary silences to improve pacing.
- 🧠 **Speaker Diarization** – Detect and label different speakers.
- 🎚️ **Audio Enhancement** – Apply compression and EQ for professional sound.
- 🧾 **Transcription** – Generate accurate transcripts with speaker labels.
- 🌐 **Web Interface** – Run everything via a Gradio-based web UI.

## 📦 Requirements

- Python 3.8+
- [ffmpeg](https://ffmpeg.org/download.html) (must be in your system PATH)

## 🛠️ Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/ren276/PodcastSuite.git
cd PodcastSuite
pip install -r requirements.txt
```

## ▶️ Usage

Run the app locally:

```bash
python app.py
```

This will launch the PodcastSuite interface in your browser via Gradio.


## ⚙️ Customization

You can tweak:

- Silence threshold
- Denoising parameters
- Transcription language

Directly inside `audio_utils.py` and `transcribe.py`.

## 📚 Powered By

- [OpenAI Whisper](https://github.com/openai/whisper)
- [PyAnnote Audio](https://github.com/pyannote/pyannote-audio)
- [Gradio](https://gradio.app)

## 📄 License

This project is licensed under the MIT License. See [LICENSE](./LICENSE) for details.

---

Made with ❤️ to make podcast editing less painful.
```

---

