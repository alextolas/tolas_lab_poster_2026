from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="Tolas Ashley Lab Poster",
    page_icon="🏃",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit chrome so the embedded HTML page looks like the original app.
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .stApp {
        background: #F4F0EC;
    }

    .block-container {
        padding-top: 0;
        padding-bottom: 0;
        padding-left: 0;
        padding-right: 0;
        max-width: 100%;
    }

    iframe {
        display: block;
        border: none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

HTML_FILE = Path(__file__).parent / "elite_wearable_vo2max_validation_conference_poster.html"

if not HTML_FILE.exists():
    st.error(
        "Missing HTML file. Add 'elite_wearable_vo2max_validation_conference_poster.html' to the same folder as this Streamlit app."
    )
    st.stop()

html = HTML_FILE.read_text(encoding="utf-8")

components.html(
    html,
    height=2200,
    scrolling=True,
)
