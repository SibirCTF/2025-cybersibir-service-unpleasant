import faker
import requests
from user import User


class Session:
    def __init__(self, host: str, user: User):
        ...

    def register_user(self, host):
        """ nuff said """
        # requests.post(host)
        # return cookie
        ...

    def login_user(self, cookie: str):
        """ nuff said """
        ...

    def create_public(self):
        """ creates public abomination, leaves no flag """
        ...

    def create_private(self):
        """ creates private abomination, FLAG HERE !!!"""
        ...

    def check_public(self):
        """ checks public abomination for accessibility and info """
        ...

    def check_private(self):
        """ checks private abomination for accessibility and FLAG """
        ...
