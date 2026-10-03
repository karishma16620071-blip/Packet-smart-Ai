from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from ..services.gemini_service import generate_response

router = APIRouter()

@router.get("/jewelry", response_class=HTMLResponse)
def jewelry_page(request: Request):
    return request.app.state.templates.TemplateResponse(
        "jewelry.html", {"request": request}
    )

@router.post("/generate-jewelry")
def generate_jewelry(
    budget: int = Form(...),
    occasion: str = Form(...),
    style: str = Form("Traditional")
):
    prompt = f"""
Suggest jewelry for an Indian user.
Occasion: {occasion}
Style: {style}
Budget: ₹{budget}
Give jewelry types, material options, styling tips, and an approximate
budget split. Do not claim live product availability or exact prices.
"""
    return {"category": "Jewelry Planner", "result": generate_response(prompt)}
