# ./containers.py
from dependency_injector import containers, providers

from user.application.user_service import UserService
from user.infra.repository.user_repo import UserRepository


# 의존성 주입을 관리해주는 모듈(설정 모듈)
class Container(containers.DeclarativeContainer):
    # (1) 의존성을 사용할 모듈을 선언한다.
    wiring_config = containers.WiringConfiguration(modules=["user.interface.controllers.user_controller"])

    # (2) 의존성을 제공할 모듈을 팩토리에 등록한다.
    user_repo = providers.Factory(UserRepository)

    # (3) UserService 객체를 생성한다. UserService 는 UserRepository 를 의존한다.
    #     따라서 컨테이너에서 UserService 를 생성할 때 의존성을 같이 주입해준다.
    user_service = providers.Factory(UserService, user_repo=user_repo)

