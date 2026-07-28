#! python

import argparse
import logging
import os

from fibmeowicci import meow

DEFAULT_LOGGING = "ERROR"


def init_logging() -> logging.Logger:
    logging.basicConfig(
        level=logging.getLevelNamesMapping().get(
            os.environ.get("PYTHON_LOG", DEFAULT_LOGGING).upper(), DEFAULT_LOGGING
        )
    )
    return logging.getLogger("fibmeowicci")


def get_config():
    parser = argparse.ArgumentParser(
        description="Fib_Meow_icci: It's still not dinner time"
    )
    parser.add_argument("--limit", "-d", help="when to give up")

    return parser.parse_args()


def main(args) -> None:
    meow(limit=args.limit)


init_logging()

if __name__ == "__main__":
    logging.info("😺 Is it dinner?")
    main(get_config())
