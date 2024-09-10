import faker
import requests
from user import User


class Session:
    base_url = str
    port = 5000
    timeout = 3
    session = requests.Session
    current_user = User

    def __init__(self, host: str, user: User):
        self.session = requests.session()
        self.base_url = f"http://{host}:{self.port}"
        body = {
            "username": user.username,
            "password": user.password,
        }
        r = self.session.post(
            f"{self.base_url}/session", data=body, timeout=self.timeout
        )
        r.raise_for_status()
        self.current_user = user
        ...

    def register_user(self, host: str, user: User):  # todo: return cookie / save session with cookie
        """ nuff said """
        base_url = f"http://{host}:{self.port}"
        body = {
            "username": user.username,
            "password": user.password,
        }
        r = requests.post(f"{base_url}/register", json=body, timeout=self.timeout)

        # don't raise on existed user
        if r.status_code != 400 or r.json() != {
            "detail": f"User {user.username} already registered"
        }:
            r.raise_for_status()
        else:
            pass  # todo: user already exist

    def login_user(self, cookie: str):  # todo: need it? already have cookie
        """ nuff said """
        ...

    def create_public(self, cookie: str, info: str):
        """ creates public abomination, leaves no flag """
        ...

    def create_private(self, cookie: str, flag: str):
        """ creates private abomination, FLAG HERE !!!"""
        ...

    def check_public(self, cookie: str):
        """ checks public abomination for accessibility and info """
        ...

    def check_private(self, cookie: str):
        """ checks private abomination for accessibility and FLAG """
        ...
