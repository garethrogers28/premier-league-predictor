import pandas as pd
import streamlit as st


def player_analysis_page():

    st.title("Player Analysis")

    st.write(
        """
        This page explores the characteristics associated with high-scoring
        Premier League players and supports Business Requirement 1.
        """
    )

    df = pd.read_csv("data/processed/all_players_cleaned.csv")
    st.write(df.head())
