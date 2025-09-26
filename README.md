# Alina-AI (Elina)

Alina-AI is a Python-based voice assistant inspired by Alexa and Google Assistant. It can perform tasks like opening websites, playing music, fetching news, and answering questions using OpenAI’s GPT models. The assistant listens for the wake word **"Alina"** and responds with voice feedback.

---

## Features

- **Voice Activation**: Listens for the wake word `Alina`.
- **Web Automation**: Opens websites like Google, YouTube, Facebook, LinkedIn, GitHub.
- **Music Playback**: Plays Spotify albums or songs from a custom music library.
- **News Updates**: Fetches top headlines using NewsAPI.
- **AI Conversations**: Handles custom user queries using OpenAI’s GPT-4.1-mini model.
- **Text-to-Speech**: Responds with voice using `pyttsx3`.
- **Environment Variables**: Securely stores API keys using a `.env` file.

---

## Installation

1. **Clone the repository**:

```bash
git clone https://github.com/rana-ji0001/Alina-AI.git
cd Alina-AI
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
pip install -r requirements.txt
OPENAI_API_KEY=your_openai_api_key_here
NEWSAPI_KEY=your_newsapi_key_here
Usage

Run the assistant:

python main.py


The assistant will start listening for the wake word "Alina".

Once activated, speak your commands, such as:

“Open Google”

“Play music on Spotify”

“Give me the news”

Any general query for OpenAI

Supported Commands

Web: Open Google, YouTube, Facebook, LinkedIn, GitHub profile.

Music: Play Spotify album or songs from musiclibrary.py.

News: Fetches top headlines from NewsAPI.

AI Chat: Any other command is processed by OpenAI GPT.

Project Structure
Alina-AI/
│
├─ main.py              # Main program file
├─ client.py            # OpenAI integration
├─ musiclibrary.py      # Music links library
├─ .env                 # Environment variables (not committed)
├─ requirements.txt     # Python dependencies
├─ README.md
└─ .gitignore

Dependencies

speech_recognition – For microphone input

pyttsx3 – Text-to-speech

python-dotenv – Load environment variables

requests – API requests

openai – OpenAI GPT integration

Install all dependencies with:

pip install -r requirements.txt

Security Notes

Never commit API keys. Use .env and add it to .gitignore.

GitHub secret scanning is enabled to prevent accidental leaks.

Karan Rana :- https://github.com/rana-ji0001

---

I can also **create a ready-to-use `requirements.txt`** and update your repo structure so someone can clone and run the project immediately.  

Do you want me to do that next?
