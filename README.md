# PocketSmart AI

PocketSmart AI is a FastAPI + SQLite + Gemini powered budget and recommendation assistant.

## Features
- Home decor planner
- Party planner
- Jewelry planner
- User registration/login
- SQLite database
- Planning history page
- Responsive frontend
- Gemini AI integration
- Swagger API docs

## 1. Create virtual environment

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

## 2. Install packages

```bash
pip install -r requirements.txt
```

## 3. Configure Gemini

Copy `.env.example` to `.env` and put your Gemini API key in:

```env
GEMINI_API_KEY=your_key_here
SECRET_KEY=your_secret_here
```

Never upload your real `.env` or API key to GitHub.

## 4. Start the application

```bash
uvicorn backend.main:app --reload
```

Open:

http://127.0.0.1:8000

API documentation:

http://127.0.0.1:8000/docs

## Project structure

```text
PocketSmartAI/
├── backend/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   ├── auth.py
│   ├── routes/
│   └── services/
├── frontend/
│   ├── templates/
│   └── static/
├── requirements.txt
├── .env.example
├── .gitignore
├── run.bat
├── run.sh
└── README.md
```

## Note

The recommendation output depends on the Gemini API configuration. If no key is configured, the UI shows a clear configuration message instead of crashing.
