from fastapi import APIRouter
from core.ui_generator import generate_basic_ui

ui = APIRouter()

@ui.post("/design/ui")
def design_ui(title: str, theme: str = "dark"):
    html = generate_basic_ui(title, theme)
    file_path = f"projects/{title.replace(' ', '_')}/index.html"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    return {"message": f"UI generated for {title}", "path": file_path}
