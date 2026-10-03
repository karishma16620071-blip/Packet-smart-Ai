from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from ..services.gemini_service import generate_response

router = APIRouter()

@router.get("/party", response_class=HTMLResponse)
def party_page(request: Request):
    return request.app.state.templates.TemplateResponse(
        "party.html", {"request": request}
    )

@router.post("/generate-party")
def generate_party(
    budget: int = Form(...),
    guests: int = Form(...),
    occasion: str = Form("Birthday")
):
    prompt = f"""
Plan a {occasion} party for {guests} guests within ₹{budget}.
Include food, decoration, venue/space ideas, activities, and a realistic
budget split. Keep it practical for India and clearly label estimates.
"""
    return {"category": "Party Planner", "result": generate_response(prompt)}
