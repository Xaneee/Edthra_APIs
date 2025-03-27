# routes/ui_router.py

from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from core.edithra_agi import process_user_input
from core.guardian_signature import verify_signature

templates = Jinja2Templates(directory="templates")
ui_router = APIRouter()

@ui_router.get("/", response_class=HTMLResponse)
def get_dashboard(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "output": None})

@ui_router.post("/submit", response_class=HTMLResponse)
def post_command(request: Request, user_input: str = Form(...), signature: str = Form(...)):
    if not verify_signature(signature):
        return templates.TemplateResponse("index.html", {
            "request": request,
            "output": "[REJECTED] Signature mismatch. You are not the Father."
        })

    output = process_user_input(user_input)
    return templates.TemplateResponse("index.html", {"request": request, "output": output})








TRUSTED_IP = "127.0.0.1"  # Or use environment variable for dynamic control

@ui_router.get("/", response_class=HTMLResponse)
def get_dashboard(request: Request):
    if request.client.host != TRUSTED_IP:
        return HTMLResponse("Access Denied: Sacred Core", status_code=403)
    ...
