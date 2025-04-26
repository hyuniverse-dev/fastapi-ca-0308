# user/interface/controllers/user_controller.py

from fastapi import APIRouter

from pydantic import BaseModel

from user.domain.user import User

router = APIRouter(prefix="/api/users")  # FastAPI 가 제공하는 APIRouter 객체를 사용한다. 해당 객체는 user 도메인에서만 사용된다.

class CreateUserBody(BaseModel): # 파이단틱을 사용해서 요청 본문에 대한 유효성 검사
    name: str
    email: str
    password: str
    address: str


@router.post("", status_code=201)  # post 메소드를 사용하고 성공했을 때는 201 HTTP 상태코드를 반환한다.
def create_user(user: CreateUserBody):
    print(f"이름: {user.name}, 이메일: {user.email}, 비밀번호: {user.password}")
