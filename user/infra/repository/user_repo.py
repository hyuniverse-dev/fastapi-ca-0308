'''
user/infra/repository/user_repo.py

IUserRepository의 구현체
    - 실제로 '어떻게' 할 것인지를 구현한 클래스이다.
'''
from user.domain.repository.user_repo import IUserRepository


class UserRepository(IUserRepository):
    pass