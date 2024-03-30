import os

def resolve_url_from_environment(host):
    if os.environ.get("RENDER", False):
        return f"https://{host}"
    else:
        return f"http://{host}"