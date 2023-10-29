"""Entrypoint of the application."""

import logging

from src.conception.app import app

logging.getLogger().setLevel(logging.INFO)


def main() -> None:
    """Run the application."""
    app()


if __name__ == "__main__":
    main()
