# user/interface/controllers/user_controller.py
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field, EmailStr

from containers import Container
from user.application.user_service import UserService

router = APIRouter(prefix="/api/users")  # FastAPI 가 제공하는 APIRouter 객체를 사용한다. 해당 객체는 user 도메인에서만 사용된다.


class CreateUserBody(BaseModel):  # 파이단틱을 사용해서 요청 본문에 대한 유효성 검사
    name: str = Field(min_length=2, max_length=32)
    email: EmailStr = Field(max_length=64)
    password: str = Field(min_length=8, max_length=32)


class UserResponse(BaseModel):
    id: str
    # name: str
    email: str
    created_at: str
    updated_at: str


@router.post("", status_code=201)  # post 메소드를 사용하고 성공했을 때는 201 HTTP 상태코드를 반환한다.
@inject
def create_user(
        user: CreateUserBody,
        user_service: UserService = Depends(Provide[Container.user_service])
) -> UserResponse:
    user = user_service.create_user(name=user.name, email=user.email, password=user.password)
    return user
