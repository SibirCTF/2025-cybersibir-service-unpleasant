import random
import faker
import dataclasses
import hashlib

MAX_IMPLANTS = 3


@dataclasses.dataclass
class User:
    username: str
    password: str
    abom_name: str
    abom_gender: str
    abom_private_gender: str  # flag
    abom_head: int
    abom_eye: int
    abom_body: int
    abom_arm: int
    abom_leg: int
    private: bool


def hash_int(string: str) -> int:
    return int(hashlib.sha1(string.encode("utf8")).hexdigest(), 16)


def gen_username(flag_id: str) -> str:
    return f"user#{str(hash_int('username' + flag_id))[:16]}"


def generate_user(flag: str, flag_id: str, private: bool) -> User:
    username = str(gen_username(flag_id))
    password = str(hash_int(flag_id))
    user = User(
        username=username,
        password=password,
        abom_name="str",  # TODO: FAKER / RANDOMIZE NAMES
        abom_gender=genders[random.randint(0, len(genders))],
        abom_private_gender=flag,  # flag
        abom_head=random.randint(1, MAX_IMPLANTS),
        abom_eye=random.randint(1, MAX_IMPLANTS),
        abom_body=random.randint(1, MAX_IMPLANTS),
        abom_arm=random.randint(1, MAX_IMPLANTS),
        abom_leg=random.randint(1, MAX_IMPLANTS),
        private=private
    )
    return user

