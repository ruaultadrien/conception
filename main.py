"""Entrypoint of the application."""

import logging

from src.conception import app

logging.getLogger().setLevel(logging.INFO)


def main() -> None:
    app()
    



if __name__ == "__main__":
    main()
