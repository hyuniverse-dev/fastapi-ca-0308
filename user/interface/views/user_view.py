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


@router.get("/signup")
def signup_view(
        request: Request
):
    return user_templates.TemplateResponse("signup.html", {"request": request})


@router.get("/login/basic")
def basic_login_view(
        request: Request
):
    return user_templates.TemplateResponse("basic_login.html", {"request": request})


@router.get("/celebrate")
def celebrate_view(
        request: Request
):
    return common_templates.TemplateResponse("celebration.html", {"request": request})
