"""Page to display details about the Vector Database status."""

import os

from src.containers.vector_db import vector_db_container
from src.utils import resolve_backend_port_from_environment, resolve_url_from_environment


def vector_db_page():
    """Streamlit container displaying the state of the vector database."""
    backend_url = resolve_url_from_environment(os.environ["BACKEND_HOST"])
    backend_port = resolve_backend_port_from_environment()
    vector_db_container(backend_url, backend_port)
    pass


vector_db_page()