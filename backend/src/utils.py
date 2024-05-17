"""Utility functions for backend."""

import os


def resolve_http_or_https_from_environment(host):
    """Resolve the HTTP or HTTPS protocol based on the environment."""
    if os.environ.get("RENDER", False):
        return f"https://{host}"
    else:
        return f"http://{host}"


