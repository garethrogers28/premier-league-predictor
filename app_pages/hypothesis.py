import pandas as pd
import plotly.express as px
import streamlit as st
from scipy.stats import mannwhitneyu


def hypothesis_page():
    st.title("Project Hypothesis")

    st.markdown("""
    ### Hypothesis

    **Premier League players classified as high scorers will demonstrate
    stronger attacking statistics, particularly shots and shots on target,
    than players who are not classified as high scorers.**

    ---

    ### How the Hypothesis Was Validated

    The hypothesis was investigated during the exploratory data analysis
    by comparing the shooting statistics of players classified as high
    scorers with those who were not.
    """)

    # Create the HighScorer classification
    df = pd.read_csv("data/processed/all_players_cleaned.csv")
    df["HighScorer"] = df["Goals"] >= 10

    # Calculate average shooting statistics for each class
    shooting_stats = (
        df.groupby("HighScorer")[
            ["Shots", "Shots on target", "Shooting accuracy %"]
        ]
        .mean()
        .reset_index()
    )

    shooting_stats["HighScorer"] = shooting_stats["HighScorer"].map({
        False: "Non-High Scorer",
        True: "High Scorer"
    })

    shooting_stats = shooting_stats.melt(
        id_vars="HighScorer",
        var_name="Statistic",
        value_name="Average"
    )

    # Plot the comparison
    fig = px.bar(
        shooting_stats,
        x="Statistic",
        y="Average",
        color="HighScorer",
        barmode="group",
        title="Average Shooting Statistics by High-Scorer Classification"
    )

    st.plotly_chart(fig, width="stretch")

    st.markdown("""
    High scorers demonstrated substantially stronger shooting statistics:

    - **Shots:** 80.23 compared with 11.41
    - **Shots on target:** 34.35 compared with 3.81
    - **Shooting accuracy:** 43.46% compared with 15.62%
    """)

    # One-sided Mann-Whitney U test: shooting stats are right-skewed
    shooting_test_df = df.dropna(subset=["Shots", "Shots on target"])

    shots_high = shooting_test_df.loc[
        shooting_test_df["HighScorer"], "Shots"
    ]
    shots_non_high = shooting_test_df.loc[
        ~shooting_test_df["HighScorer"], "Shots"
    ]

    sot_high = shooting_test_df.loc[
        shooting_test_df["HighScorer"], "Shots on target"
    ]
    sot_non_high = shooting_test_df.loc[
        ~shooting_test_df["HighScorer"], "Shots on target"
    ]

    _, shots_p = mannwhitneyu(
        shots_high, shots_non_high, alternative="greater"
    )
    _, sot_p = mannwhitneyu(
        sot_high, sot_non_high, alternative="greater"
    )

    st.markdown(f"""
    ### Statistical Significance

    A one-sided **Mann-Whitney U test** was used to confirm these
    differences are statistically significant, rather than relying on
    averages alone:

    - **Shots:** p = {shots_p:.2e}
    - **Shots on target:** p = {sot_p:.2e}

    Both p-values are far below the 0.05 significance threshold.
    """)

    st.markdown("""
    ### Outcome

    **The hypothesis was supported, and the null hypothesis was rejected
    on statistical grounds.** High scorers demonstrate a significantly
    higher number of shots and shots on target.
    """)
