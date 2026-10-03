from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import User
from ..auth import hash_password, verify_password

router = APIRouter()

@router.get("/register", response_class=HTMLResponse)
def register_page(request: Request):
    return request.app.state.templates.TemplateResponse(
        "register.html", {"request": request, "error": None}
    )

@router.post("/register")
def register(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    if db.query(User).filter(User.username == username).first():
        return request.app.state.templates.TemplateResponse(
            "register.html",
            {"request": request, "error": "Username already exists."}
        )

    user = User(username=username, password=hash_password(password))
    db.add(user)
    db.commit()
    return RedirectResponse("/login", status_code=303)

@router.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return request.app.state.templates.TemplateResponse(
        "login.html", {"request": request, "error": None}
    )

@router.post("/login")
def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.username == username).first()

    if not user or not verify_password(password, user.password):
        return request.app.state.templates.TemplateResponse(
            "login.html",
            {"request": request, "error": "Invalid username or password."}
        )

    response = RedirectResponse("/", status_code=303)
    response.set_cookie("user_id", str(user.id), httponly=True, samesite="lax")
    response.set_cookie("username", user.username, httponly=False, samesite="lax")
    return response

@router.get("/logout")
def logout():
    response = RedirectResponse("/", status_code=303)
    response.delete_cookie("user_id")
    response.delete_cookie("username")
    return response
