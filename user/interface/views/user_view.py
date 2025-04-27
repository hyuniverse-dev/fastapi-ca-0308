from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

router = APIRouter(prefix="/view/users")

common_templates = Jinja2Templates(directory="templates")
user_templates = Jinja2Templates(directory="templates/user")


@router.get("/login")
def main_view(
        request: Request
):
    return common_templates.TemplateResponse("main.html", {"request": request})
