# user/domain/user.py

'''
도메인(엔티티) 계층
    1. 소프트웨어에서 도메인이란 해결하고자 하는 특정 주제나 분야를 얘기한다.
       해당 분야(주제)에 적용되는 속성이나 동작을 정의한다.
    2. 도메인 계층은 핵심 개념을 주로 다룬다.
    3. 예를 들면, 은행 애플리케이션을 만든다고 하면 계좌(account), 사용자(user), 거래(transaction)
       와 같은 개념들이 핵심 개념으로 도출해 낼 수 있다.
    4. 도메인 계층은 애플리케이션 가져야할 핵심 요소만 가지기 때문에
       만약 여기서 변화가 생기면 모든 코드에 반영해줘야 한다.
   
User 도메인
    1. 회원 리소스를 다루는 도메인
'''
from dataclasses import dataclass



@dataclass # 도메인 클래스로 사용될 수 있도록 지정하는 데코레이터
           # 생성자 함수를 자동으로 만들어주고, 타입을 쉽게 제공해준다.
class User:
    # 아이디(리소스 구분자), 이름, 이메일, 비밀번호, 계정 생성일시, 계정 수정일시
    id: str
    name: str
    email: str
    password: str
    created_at: str
    updated_at: str