import streamlit as st
from app_pages.project_summary import project_summary_page

st.set_page_config(
    page_title="Premier League Player Predictor",
)

page = st.sidebar.selectbox(
    "Menu",
    [
        "Project Summary",
        "Player Analysis",
        "High Scorer Predictor",
        "Model Performance",
    ]
)

project_summary_page()