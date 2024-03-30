import requests
import streamlit as st
import os


def vector_db_container():
    # Retrieve the number of documents in the collection
    res = requests.get(f"http://{os.environ['BACKEND_HOST']}:8888/vector_db")
    if res.status_code == 200:
        st.metric("Number of documents in the collection:", len(res.json()["documents"]["ids"]))
    else:
        st.error("Could not query vector database.")

    if st.button("POST vector database"):
        requests.post(f"http://{os.environ['BACKEND_HOST']}:8888/vector_db", timeout=120)
