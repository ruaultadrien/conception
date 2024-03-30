import requests
import streamlit as st
import os

from src.utils import resolve_url_from_environment


def vector_db_container():
    # Retrieve the number of documents in the collection
    backend_url = resolve_url_from_environment(os.environ["BACKEND_HOST"])
    res = requests.get(f"{backend_url}:8888/vector_db")
    if res.status_code == 200:
        st.metric("Number of documents in the collection:", len(res.json()["documents"]["ids"]))
    else:
        st.error("Could not query vector database.")

    if st.button("POST vector database"):
        requests.post(f"{backend_url}:8888/vector_db", timeout=120)
