import streamlit as st


def project_summary_page():

    st.title("Premier League High Scorer Predictor")

    st.subheader("Project Overview")

    st.write(
        """
        This application is designed to support a Premier League football club
        with player recruitment decisions by identifying players who are likely
        to be high scorers based on their performance statistics.

        The project uses historical Premier League player data to analyse
        patterns associated with high-scoring players and applies machine
        learning to classify players as high scorers or non-high scorers.
        """
    )
    st.subheader("Project Dataset")

    st.write(
        """
        The project uses historical Premier League player performance data covering
        nine seasons from 2015/16 to 2023/24.

        Following data collection, cleaning and feature engineering, the modelling
        dataset contains 8,196 player-season records and 17 predictive features.
        These features include player appearances, assists, shots, shots on target,
        shooting accuracy, passing statistics and player position.

        The machine learning target is `HighScorer`, which identifies whether a
        player scored 10 or more Premier League goals in a season.

        Goals scored are not included as an input feature because they are used to
        create the `HighScorer` target. Including goals as a predictor would cause
        data leakage and would not provide a meaningful prediction of high-scoring
        potential.
        """
)

    st.subheader("Business Requirements")

    st.markdown(
        """
        The project has three business requirements:

        1. Analyse Premier League player performance data to identify the characteristics associated with high-scoring players.
        2. Develop and evaluate a machine learning model that can reliably identify potential high scorers using performance statistics other than goals scored, supporting player recruitment decisions.
        3. Present the key analytical findings and machine learning results through an interactive Streamlit dashboard to support the club's recruitment analysis.
        """
    )

    st.subheader("ML Business Case")

    st.markdown(
        """
        The machine learning task supports **Business Requirement 2** by predicting
        whether a Premier League player belongs to the `HighScorer` class.

        The model uses supervised binary classification to identify potential high
        scorers from player performance statistics without using goals scored as a
        predictor.

        **Model Success Criteria:**

        - **Precision** for the `HighScorer=True` class is the primary success metric.
        - A false-positive prediction is considered more costly because it could lead
        a club to invest time and money in a player who does not demonstrate the
        required high-scoring profile.
        - Missing a genuine high scorer is considered less costly, so recall is treated
        as a secondary metric.
        - The model is considered successful if it achieves at least **0.75 precision**
        for the `HighScorer` class on unseen test data.

        The model is intended to support recruitment analysis rather than replace
        wider scouting and recruitment decision-making.
        """
    )