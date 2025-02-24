import random

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
        r = self.session.get(f"{self.base_url}", timeout=self.timeout)
        r.raise_for_status()

    def register_user(self):
        """ nuff said """

        body = {
            "username": self.user.username,
            "password": self.user.password,
        }
        r = requests.post(f"{self.base_url}/register", data=body, timeout=self.timeout)

        # don't raise on existed user  # TODO: errors in api
        if r.status_code != 400:
            r.raise_for_status()
        else:
            pass

    def login_user(self):
        """ nuff said """
        body = {
            "username": self.user.username,
            "password": self.user.password,
        }
        r = self.session.post(f"{self.base_url}/login", data=body, timeout=self.timeout)
        r.raise_for_status()

        if r.status_code == 400:
            r.raise_for_status()
        else:
            pass
        ...

    def create_public(self): # TODO: generate new values everytime
        """ creates public abomination, leaves no flag """
        body = {
            "name": self.user.abom_name,
            "gender": self.user.abom_gender,
            "head": self.user.abom_head,
            "eye": self.user.abom_eye,
            "body": self.user.abom_body,
            "arm": self.user.abom_arm,
            "leg": self.user.abom_leg
        }
        r = self.session.post(f"{self.base_url}/create_abomination", data=body, timeout=self.timeout)
        r.raise_for_status()
        # TODO: http code error

        ...

    def create_private(self):
        """ creates private abomination, FLAG HERE !!!"""
        body = {
            "name": self.user.abom_name,
            "gender": self.user.abom_private_gender,
            "head": self.user.abom_head,
            "eye": self.user.abom_eye,
            "body": self.user.abom_body,
            "arm": self.user.abom_arm,
            "leg": self.user.abom_leg,
            "is_private": self.user.private
        }
        r = self.session.post(f"{self.base_url}/create_abomination", data=body, timeout=self.timeout)
        r.raise_for_status()
        # TODO: http code error

        ...

    def check_public(self, abom_id: int):
        """ checks public abomination for accessibility and info """
        r = self.session.get(f"{self.base_url}/api/abomination/{abom_id}", timeout=self.timeout)
        r.raise_for_status()
        print(r.json())
        # TODO: http code error
        ...

    def check_private(self, abom_id: int, flag):
        """ checks private abomination for accessibility and FLAG """
        r = self.session.get(f"{self.base_url}/api/abomination/{abom_id}", timeout=self.timeout)
        r.raise_for_status()
        print(r.json())
        if flag != r.json()[1]:
            raise Exception("Flag is not found in post profile")

        # TODO: http code error
        ...

    def check_abominations(self, flag):
        r = self.session.get(f"{self.base_url}/api/my_abominations", timeout=self.timeout)
        r.raise_for_status()
        abom_ids = [abom[0] for abom in r.json()]  # Consider there are 2 ids: 1. public; 2. private
        self.check_public(abom_ids[0])
        self.check_private(abom_ids[1], flag)

    def logout(self):
        """logout"""
        r = self.session.get(f"{self.base_url}/logout", timeout=self.timeout)
        r.raise_for_status()


user = generate_user('FLAGFLAGFLAG', str(random.randint(1, 1000)), True)
ses = Session('127.0.0.1', user)

ses.register_user()
ses.login_user()
ses.create_public()
ses.create_private()

ses.check_abominations('penis')
