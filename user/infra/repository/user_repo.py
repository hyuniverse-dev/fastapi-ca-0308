'''
user/infra/repository/user_repo.py

IUserRepository의 구현체
    - 실제로 '어떻게' 할 것인지를 구현한 클래스이다.
'''
from user.domain.repository.user_repo import IUserRepository
from user.domain.user import User
from user.infra.db_models.user import User as UserVO
from utils.json_helper import JsonHelper


class UserRepository(IUserRepository):

    def __init__(self):
        self.json_helper = JsonHelper("./database/user.json")

    def save(self, user: User):
        users = self.json_helper.read_json()
        users.append(user.__dict__)
        return self.json_helper.save_json(users)

    def find_by_email(self, email: str) -> UserVO | None:
        users = self.json_helper.read_json()
        for user in users:
            if user["email"] == email:
                return UserVO(
                    id=user["id"],
                    email=user["email"],
                    password=user["password"],
                    created_at=user["created_at"],
                    updated_at=user["updated_at"]
                )

        return None
