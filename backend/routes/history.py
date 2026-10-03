from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import History

router = APIRouter()

@router.get("/history", response_class=HTMLResponse)
def history_page(request: Request, db: Session = Depends(get_db)):
    user_id = request.cookies.get("user_id")
    rows = []

    if user_id and user_id.isdigit():
        rows = (
            db.query(History)
            .filter(History.user_id == int(user_id))
            .order_by(History.id.desc())
            .all()
        )

    return request.app.state.templates.TemplateResponse(
        "history.html", {"request": request, "history": rows}
    )
