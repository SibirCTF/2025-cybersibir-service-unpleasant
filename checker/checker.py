import requests
import os
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
    user1 = generate_user(flag_id)
    ses = Session(host, user1)
    ses.register_user()
    ses.login_user()
    ses.create_abomination()
    ses.create_abomination(flag)
    ses.logout()

    return StatusCode.OK


def check(host: str, flag_id: str, flag: str):
    user1 = generate_user(flag_id)
    ses = Session(host, user1)
    ses.login_user()
    ses.check_my_abominations(flag)
    ses.logout()

    return StatusCode.OK


def ping(host) -> bool:
    ping_timeout = 2
    response = os.system(f"timeout {ping_timeout}s ping -c 1 {host} > /dev/null 2>&1")
    return response == 0


def handler(host: str, command, flag_id: str, flag: str):
    if not ping(host):
        # local_logger.info("host is not answering")
        exit(StatusCode.DOWN)

    if command == PUT_COMMAND:
        status_code = put(host, flag_id, flag)
        # local_logger.info("put command has ended with %d status code", status_code)
        exit(status_code)

    if command == CHECK_COMMAND:
        status_code = check(host, flag_id, flag)
        # local_logger.info("check command has ended with %d status code", status_code)
        exit(status_code)

    exit(StatusCode.MUMBLE)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="unpleasant checker")
    parser.add_argument("host")
    parser.add_argument("command", choices=(PUT_COMMAND, CHECK_COMMAND))
    parser.add_argument("flag_id")
    parser.add_argument("flag")
    args = parser.parse_args()

    try:
        handler(
                host=args.host,
                command=args.command,
                flag_id=args.flag_id,
                flag=args.flag,
            )

    except requests.exceptions.Timeout:
        # local_logger.error("Timeout exception")
        exit(StatusCode.MUMBLE)

    except requests.exceptions.ConnectionError:
        # local_logger.error("ConnectionError to host. Seems that it isn't work")
        exit(StatusCode.DOWN)

    except requests.exceptions.HTTPError as exc:
        # local_logger.error("Service returned error status code %r", exc)
        exit(StatusCode.CORRUPT)

    except FlagProblem as exc:
        # local_logger.error("Flag is not found! %r", exc)
        exit(StatusCode.CORRUPT)

    except Exception as exc:
        # local_logger.error("Everything is bad :c %r", exc, exc_info=True)
        exit(StatusCode.CORRUPT)
