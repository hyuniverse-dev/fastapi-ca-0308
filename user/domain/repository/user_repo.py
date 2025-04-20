'''
user/domain/repository/user_repo.py

User 도메인 영속화하기 위한 모듈이다.
    - 실제 구현체가 아닌 추상화된 모듈이다.
    - 따라서 '무엇을' 만 정의하고, '어떻게(실제 실행되는 코드)'는 별도의 모듈에서 관리한다.
    - 그래야 의존성을 제거할 수 있다.

추상화된 모듈 - 추상 클래스 생성
    - 실제 실행되는 코드를 작성하지 않는다. '무엇을' 만 작성한 클래스이다.
    - 추상 클래스로 만드는 방법은 abc 모듈에 정의된 메타클래스로 선언하는 것이다.
    - abc 모듈은 Abstract Base Class 약자이다.
    - 의존성 역전되면 나중에 구현체가 변경되더라도 사용하는 쪽(고수준 계층)에는 영향이 없다.
'''
from abc import ABCMeta


class IUserRepository(metaclass=ABCMeta):
    pass