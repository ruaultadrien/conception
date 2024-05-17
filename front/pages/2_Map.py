"""Experimental page to display a map."""

import streamlit as st
import streamlit.components.v1 as components


def map():
    """Experimental Streamlit container to display a map."""
    st.warning("This is an experimental feature.")

    components.iframe(
        "https://www.meteosuisse.admin.ch/previsions-locales/lausanne/1003.html#forecast-tab=detail-view",
        height=800,
        width=800,
    )


map()
