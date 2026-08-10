#! python

import argparse
import logging
import os

from fibmeowicci import meow

DEFAULT_LOGGING = "ERROR"


def init_logging() -> logging.Logger:
    """Initialize logging based on PYTHON_LOG"""
    logging.basicConfig(
        level=logging.getLevelNamesMapping().get(
            os.environ.get("PYTHON_LOG", DEFAULT_LOGGING).upper(), DEFAULT_LOGGING
        )
    )
    return logging.getLogger("fibmeowicci")


def get_config() -> argparse.Namespace:
    """Fetch configuration values"""
    parser = argparse.ArgumentParser(
        description="Fib_Meow_icci: It's still not dinner time"
    )
    parser.add_argument("--limit", "-d", help="when to give up")
    parser.add_argument("--sleep_factor", type=float, help="wait between rounds")

    return parser.parse_args()


def main(args: argparse.Namespace = get_config()) -> None:
    """Meow."""
    logger.info("😺 Is it dinner?")
    meow(limit=args.limit, sleep_factor=args.sleep_factor)


logger = init_logging()

if __name__ == "__main__":
    main()
