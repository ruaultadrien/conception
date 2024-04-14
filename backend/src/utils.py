"""Utility functions for backend."""

import logging
import os

import chromadb
import chromadb.api
import chromadb.config


def get_vector_db_chroma_client() -> chromadb.api.ClientAPI:
    """Get a Chroma client for the vector database."""
    use_ssl = os.environ.get("RENDER", False)
    logging.info(f"Chroma host used for Chroma client creation: {os.environ['CHROMA_HOST']}")
    chroma_port = resolve_chroma_port_from_environment()
    return chromadb.HttpClient(
        host=os.environ["CHROMA_HOST"],
        port=chroma_port,
        settings=chromadb.config.Settings(anonymized_telemetry=False),
        ssl=use_ssl,
    )


def resolve_http_or_https_from_environment(host):
    """Resolve the HTTP or HTTPS protocol based on the environment."""
    if os.environ.get("RENDER", False):
        return f"https://{host}"
    else:
        return f"http://{host}"


def resolve_chroma_port_from_environment():
    """Resolve the Chroma port based on the environment."""
    if os.environ.get("RENDER", False):
        return 443
    else:
        return os.environ["CHROMA_PORT"]
