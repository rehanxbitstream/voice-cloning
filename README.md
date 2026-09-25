# AI Voice Cloning and Speech Generation

A Python-based desktop application for AI voice cloning and speech generation using the **ElevenLabs API**. The application provides a simple graphical interface where users can enter text, select an AI voice, generate speech, play the generated audio, and stop playback.

> **Note:** The current demo uses a pre-existing ElevenLabs voice because Instant Voice Cloning requires a supported ElevenLabs subscription/feature. The project can be adapted to use a permitted voice clone by replacing the Voice ID with the ID of a clone created with appropriate rights and permission.

## Features

- Text-to-speech generation using ElevenLabs
- Multiple AI voice options
- Tkinter graphical user interface
- Generate and save speech as MP3
- Play and stop generated audio
- Environment-variable based API key configuration
- Clean structure for academic demonstration

## Technologies Used

- **Python 3**
- **Tkinter** — GUI
- **ElevenLabs API** — AI voice generation
- **Pygame-CE** — Audio playback
- **python-dotenv** — Environment variable management

## Project Structure

```text
voice-cloning/
│
├── src/
│   ├── main.py
│   ├── voice_clone.py
│   └── test_env.py
│
├── output/
│   └── .gitkeep
│
├── .gitignore
├── readme.md
└── requirements.txt
```

### File Description

| File | Description |
|---|---|
| `src/main.py` | Main Tkinter GUI application |
| `src/voice_clone.py` | ElevenLabs speech generation logic |
| `src/test_env.py` | Checks API key configuration |
| `output/` | Stores generated audio files locally |
| `.gitignore` | Prevents sensitive/generated files from being committed |
| `requirements.txt` | Python dependencies |

## How It Works

```text
User enters text
       ↓
Selects an AI voice
       ↓
Python application
       ↓
ElevenLabs API
       ↓
AI speech generation
       ↓
generated_voice.mp3
       ↓
Play / Stop audio
```

## Requirements

- Python 3.x
- ElevenLabs account and API key
- Internet connection

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/rehanxbitstream/voice-cloning.git
cd voice-cloning
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## API Key Configuration

Create a `.env` file in the project root:

```env
ELEVENLABS_API_KEY=your_api_key_here
```

Replace the placeholder with your ElevenLabs API key.

**Never upload your real API key to GitHub.**

The `.gitignore` file keeps `.env` out of the repository.

## Run the Application

From the project root:

```bash
python src/main.py
```

The GUI will open. Enter your text, select a voice, and click **Generate Speech**.

## Output

Generated audio is saved locally as:

```text
output/generated_voice.mp3
```

Generated MP3 files are intentionally ignored by Git.

## Voice Cloning

This project is designed as a voice-cloning and AI speech-generation demonstration.

For actual voice cloning, use only:

- Your own voice, or
- A voice for which you have explicit permission.

The current implementation uses an existing ElevenLabs voice because Instant Voice Cloning is not available on the current account. If a permitted voice clone is created later, its Voice ID can be configured in the application.

## Testing API Configuration

Run:

```bash
python src/test_env.py
```

This verifies that the API key is loaded correctly.

## Security

Do not commit sensitive files such as:

```text
.env
```

The project also ignores generated audio:

```gitignore
output/*.mp3
*.wav
```

## Academic Project

This project demonstrates:

- Artificial Intelligence
- Generative AI
- Text-to-Speech technology
- Voice synthesis
- Python programming
- API integration
- GUI development
- Audio processing

It can be used as a **Multimedia Systems project** demonstrating how AI-generated speech can be integrated into a desktop multimedia application.

## Future Improvements

- Support for permitted custom voice cloning
- Voice preview
- Adjustable speech settings
- Multiple audio formats
- Progress indicator
- Voice history
- Improved GUI design
- Additional multimedia features

## Disclaimer

This project is intended for educational and authorized use. Voice cloning and synthetic speech should not be used to impersonate, deceive, defraud, or misrepresent another person.

## Author

**Rehan Khan**

GitHub: `rehanxbitstream`

---

⭐ If you find this project useful, consider giving the repository a star.
