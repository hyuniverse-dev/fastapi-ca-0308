# utils/crypto.py
from passlib.context import CryptContext


class Crypto:

    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")  # 암호화 객체 생성 + 옵션 설정(암호화 알고리즘 선택)

    def encrypt(self, secret: str) -> str:
        """
        비밀번호를 해시합니다.
        :param secret: 비밀번호
        :return:해시된 비밀번호
        """
        return self.pwd_context.hash(secret)

    def verity(self, secret: str, hashed: str) -> bool:
        """
        비밀번호를 검증합니다.
        :param secret: 비밀번호(평문)
        :param hashed: 비밀번호(해시)
        :return: True or False
        """
        return self.pwd_context.verify(secret, hashed)


if __name__ == "__main__":
    crypto = Crypto()
    hashed_password = crypto.encrypt("my_password")
    print(f"해시된 비밀번호: {hashed_password}") # 암호화 결과 예시: $2b$12$n25NMsm6zZhbITZEaWnnKOCztrDNoTWqylP6KrWKYf78njl7IsFDK

    is_verified = crypto.verity("my_password", hashed_password)
    print(f"비밀번호 일치여부: {is_verified}")
