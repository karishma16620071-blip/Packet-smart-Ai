from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from ..services.gemini_service import generate_response

router = APIRouter()

@router.get("/home", response_class=HTMLResponse)
def home_page(request: Request):
    return request.app.state.templates.TemplateResponse(
        "home.html", {"request": request}
    )

@router.post("/generate-home")
def generate_home(budget: int = Form(...), room: str = Form(...)):
    prompt = f"""
Create a practical home-decor recommendation.
Room: {room}
Budget: ₹{budget}
Give affordable item suggestions, approximate price ranges, styling ideas,
and a simple budget breakdown. Mention that prices are estimates.
"""
    return {"category": "Home Planner", "result": generate_response(prompt)}
