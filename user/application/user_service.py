from datetime import datetime
from fastapi import HTTPException

from ulid import ULID

from user.domain.repository.user_repo import IUserRepository
from user.domain.user import User
from user.infra.repository.user_repo import UserRepository
from utils.crypto import Crypto


class UserService:
    def __init__(self):
        self.user_repo: IUserRepository = UserRepository()
        self.ulid = ULID()
        self.crypto = Crypto()

    def create_user(self, name: str, email: str, password: str) -> User:

        # 중복 유저 검사 - 초기화
        _user = None

        try:
            _user = self.user_repo.find_by_email(
                email)  # (중복 유저 검사-1) 저장된 데이터에서 email로 유저를 찾는다. 새로 생성할 유저와 구분하기 위해 _(언더바) 사용
        except HTTPException as e:
            if e.status_code != 422:  # 리소스 생성 시에 중복된 데이터 존재하면 422 코드를 사용하기로 정한다.
                raise e

        if _user:
            raise HTTPException(status_code=422,
                                detail="이미 존재하는 이메일입니다.")  # (중복 유저 검사-2) _user 가 True이면 중복된 것으로 간주하고 422 예외를 발생시킨다.

        now = datetime.now()  # 요청 시간을 생성한다.

        user = User(  # 유저 객체를 생성한다.
            id=self.ulid.generate(),  # ulid 라이브러리르 사용해서 id 값 대입
            name=name,
            email=email,
            password=self.crypto.encrypt(password), # 비밀번호 암호화 적용
            created_at=str(now),  # datetime 타입을 str 로 형변환
            updated_at=str(now)
        )

        self.user_repo.save(user)  # save 메소드 구현 예정

        return user
