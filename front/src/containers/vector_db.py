"""Streamlit container displaying the state of the vector database."""

import logging

import requests
import streamlit as st


def vector_db_container(backend_url: str, backend_port: str):
    """Streamlit container displaying the state of the vector database."""
    st.header("Vector Database state")

    # health check on the vector database

    request_url = f"{backend_url}:{backend_port}/vector_db_health"
    logging.info(f"Checking the health of the vector database at {request_url}")
    res = requests.get(request_url)
    vector_db_is_up = res.json()["vector_db_is_up"]
    if vector_db_is_up:
        message = "Vector database is up."
        logging.info(message)
        st.info(message)
    else:
        message = "Vector database coudl not be reached."
        logging.info(message)
        st.error(message)

    # Retrieve the number of documents in the collection
    request_url = f"{backend_url}:{backend_port}/vector_db"
    logging.info(f"Get documents with this url: {request_url}")
    with st.spinner("Querying vector database..."):
        res = requests.get(request_url)
    if res.status_code == 200:  # noqa: PLR2004
        st.metric("Number of documents in the collection:", len(res.json()["documents"]["ids"]))
    else:
        st.error("Could not query vector database.")
