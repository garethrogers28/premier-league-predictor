import streamlit as st

from app_pages.project_summary import project_summary_page
from app_pages.player_analysis import player_analysis_page
from app_pages.model_performance import model_performance_page
from app_pages.high_scorer_predictor import high_scorer_predictor_page


st.set_page_config(
    page_title="Premier League Player Predictor"
)

page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Project Summary",
        "📊 Player Analysis",
        "🎯 Model Performance",
        "⚽ High Scorer Predictor"
    ]
)

if page == "🏠 Project Summary":
    project_summary_page()

elif page == "📊 Player Analysis":
    player_analysis_page()

elif page == "🎯 Model Performance":
    model_performance_page()

elif page == "⚽ High Scorer Predictor":
    high_scorer_predictor_page()