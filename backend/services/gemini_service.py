import os

try:
    import google.generativeai as genai
except ImportError:
    genai = None

from ..config import GEMINI_API_KEY

if genai and GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

def generate_response(prompt: str) -> str:
    if not GEMINI_API_KEY or not genai:
        return (
            "Gemini API key is not configured. Add GEMINI_API_KEY to your .env file "
            "and restart the server."
        )

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text or "No recommendation was generated."
    except Exception as exc:
        return f"Gemini error: {exc}"
