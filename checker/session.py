import faker
import requests
from user import *


class Session:
    base_url = str
    port = 5000
    timeout = 3
    session = requests.Session
    current_user = User

    def __init__(self, host: str, user: User):
        self.session = requests.session()
        self.base_url = f"http://{host}:{self.port}"
        self.user = user
        # body = {
        #     "username": user.username,
        #     "password": user.password,
        # }
        # todo: connection test ?
        # r = self.session.post(
        #     f"{self.base_url}/session", data=body, timeout=self.timeout
        # )
        r = self.session.get(f"{self.base_url}", timeout=self.timeout)
        r.raise_for_status()
        # self.current_user = user
        ...

    def register_user(self):
        """ nuff said """

        body = {
            "username": self.user.username,
            "password": self.user.password,
        }
        r = requests.post(f"{self.base_url}/register", data=body, timeout=self.timeout)

        # don't raise on existed user  # TODO: errors in api
        # if r.status_code != 400 or r.json() != {
        #     "detail": f"User {user.username} already registered"
        # }:
        #     r.raise_for_status()
        # else:
        #     pass

    def login_user(self):
        """ nuff said """
        body = {
            "username": self.user.username,
            "password": self.user.password,
        }
        r = self.session.post(f"{self.base_url}/login", data=body, timeout=self.timeout)

        # TODO: errors
        # if r.status_code != 400 or r.json() != {
        #     "detail": f"User {user.username} already registered"
        # }:
        #     r.raise_for_status()
        # else:
        #     pass
        ...

    def create_public(self):
        """ creates public abomination, leaves no flag """  # TODO: save abom_id to check later? check url? check my_aboms?
        body = {
            "name": user.abom_name,
            "gender": user.abom_gender,
            "head": user.abom_head,
            "eye": user.abom_eye,
            "body": user.abom_body,
            "arm": user.abom_arm,
            "leg": user.abom_leg
        }
        r = self.session.post(f"{self.base_url}/login", data=body, timeout=self.timeout)
        # TODO: http code error

        ...

    def create_private(self):  # TODO: save abom_id to check later?
        """ creates private abomination, FLAG HERE !!!"""
        body = {
            "name": user.abom_name,
            "gender": user.abom_private_gender,
            "head": user.abom_head,
            "eye": user.abom_eye,
            "body": user.abom_body,
            "arm": user.abom_arm,
            "leg": user.abom_leg,
            "is_private": user.private
        }
        r = self.session.post(f"{self.base_url}/create_abomination", data=body, timeout=self.timeout)
        # TODO: http code error

        ...

    def check_public(self, abom_id: int):
        """ checks public abomination for accessibility and info """
        r = self.session.post(f"{self.base_url}/abomination/{abom_id}", timeout=self.timeout)
        # TODO: http code error
        ...

    def check_private(self, abom_id: int):
        """ checks private abomination for accessibility and FLAG """
        r = self.session.post(f"{self.base_url}/abomination/{abom_id}", timeout=self.timeout)
        # TODO: http code error
        ...


user = generate_user('123', '123', True)
# ses = Session('127.0.0.1', user)
print(user)
# print(ses)