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
    ...


def check(host: str, flag_id: str, flag: str):
    ...


def handler(host: str, command, flag_id: str, flag: str):
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
