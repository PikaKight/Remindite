
from typing import List


class Sign_up:

    def username(self,username: str) -> str:
        self._username = username
        return self._username

    def email(self, email: str) -> str:
        self._email = email
        return self._email

    def password(self,password: int) -> int:
        self._password = password
        return self._password

class Login:

    def check_username(self, username: str, user: str) -> bool:
        if username is user: return True
        else: return False

    def check_password(self, password: int, user: List) -> bool:
        if password in user: return True
        else: return False

    def forget_password(self, email: str, user: List) -> bool:
        if email in user: return True
        else: return False
        

