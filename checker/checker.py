import requests
import argparse
from enum import IntEnum
from session import *
from user import *
# TODO: status checks

PUT_COMMAND = "put"
CHECK_COMMAND = "check"


class StatusCode(IntEnum):
    OK = 101
    CORRUPT = 102
    MUMBLE = 103
    DOWN = 104


def put(host: str, flag_id: str, flag: str):
    user1 = generate_user(flag, flag_id, True)
    ses = Session(host, user1)
    ses.register_user()
    ses.login_user()
    ses.create_private()
    ses.create_public()
    ses.logout()

    return StatusCode.OK


def check(host: str, flag_id: str, flag: str):
    user1 = generate_user(flag, flag_id, True)
    ses = Session(host, user1)
    ses.login_user()
    # todo: abom_ids
    # ses.check_public()
    # ses.check_private()
    ses.logout()

    return StatusCode.OK


def handler(host: str, command, flag_id: str, flag: str):
    if not ping(host):
        local_logger.info("host is not answering")
        exit(StatusCode.DOWN)

    if command == PUT_COMMAND:
        put(host, flag_id, flag)

    if command == CHECK_COMMAND:
        check(host, flag_id, flag)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="unpleasant checker")
    parser.add_argument("host")
    parser.add_argument("command", choices=(PUT_COMMAND, CHECK_COMMAND))
    parser.add_argument("flag_id")
    parser.add_argument("flag")
    args = parser.parse_args()

    handler(
            host=args.host,
            command=args.command,
            flag_id=args.flag_id,
            flag=args.flag,
        )
