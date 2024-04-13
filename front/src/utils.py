import os

def resolve_url_from_environment(host):
    if os.environ.get("RENDER", False):
        return f"https://{host}"
    else:
        return f"http://{host}"

def resolve_backend_port_from_environment():
    if os.environ.get("RENDER", False):
        return 443
    else:
        return os.environ["BACKEND_PORT"]