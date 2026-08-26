import pandas as pd
import streamlit as st
import plotly.express as px


def player_analysis_page():

    st.title("Player Analysis")

    st.write(
        """
        **Business Requirement 1:** Analyse Premier League player performance data
        to identify the characteristics associated with high-scoring players.

        An exploratory data analysis (EDA) was conducted on the Premier League
        player dataset. The analysis explores positional, attacking, passing and
        creative stats associated with the `HighScorer` target.
        """
    )

    df = pd.read_csv("data/processed/all_players_cleaned.csv")
    df["HighScorer"] = df["Goals"] >= 10

    position_high_scorer = (
        df.groupby("Position")["HighScorer"]
        .mean()
        .mul(100)
    )

    st.subheader("Percentage of High Scorers by Position")
    st.bar_chart(position_high_scorer)
    st.markdown(
    """
    **Interpretation:**

    Forwards have the highest percentage of players classified as high scorers,
    followed by midfielders. Defenders and goalkeepers rarely or never reach
    the 10-goal threshold.

    This indicates that playing position is associated with high-scoring
    performance, with attacking players substantially more likely to be
    classified as high scorers.
    """
    )

    attacking_columns = [
    "Assists",
    "Big chances created",
    "Big chances missed",
    "Hit woodwork",
    "Offsides"
    ]

    attacking_stats_means = (
        df.groupby("HighScorer")[attacking_columns]
        .mean()
    )

    attacking_stats_plot=attacking_stats_means.reset_index()

    attacking_stats_plot["HighScorer"] = attacking_stats_plot["HighScorer"].map({
    False: "Not High Scorer",
    True: "High Scorer"
    })

    fig = px.bar(
    attacking_stats_plot,
    x="HighScorer",
    y=attacking_columns,
    barmode="group",
    title="Average Attacking Statistics by High Scorer Classification"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
    """
    **Interpretation:**

    High scorers show higher average values across the attacking statistics
    analysed. The largest differences can be seen in statistics associated
    with attacking involvement and goal-scoring opportunities.

    This suggests that these attacking performance characteristics may be
    useful indicators when identifying players with a high-scoring profile.
    """
    )

    passing_columns = [
    "Passes per match",
    "Crosses",
    "Cross accuracy %",
    "Through balls"
    ]

    passing_stats_means = df.groupby("HighScorer")[passing_columns].mean()

    passing_stats_plot=passing_stats_means.reset_index()

    passing_stats_plot["HighScorer"] = passing_stats_plot["HighScorer"].map({
    False: "Not High Scorer",
    True: "High Scorer"
    })

    fig = px.bar(
        passing_stats_plot,
        x="HighScorer",
        y=passing_columns,
        barmode="group",
        title="Average Passes and Creative Statistics by High Scorer Classification"
    )
    
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
    """
    **Interpretation:**

    High scorers show higher average values across the passing and creative
    statistics analysed, including passes per match, crosses, cross accuracy
    and through balls.

    This suggests that high-scoring players are not only associated with
    stronger attacking statistics, but also demonstrate greater involvement
    in passing and creative play.
    """
    )

    st.subheader("Conclusion")

    st.markdown(
    """
    The exploratory analysis identified several characteristics associated
    with high-scoring Premier League players:

    - **Playing position is important**, with forwards having the highest
      proportion of high scorers, followed by midfielders.
    - **High scorers demonstrate stronger attacking statistics**, including
      greater involvement in assists, goal-scoring opportunities and other
      attacking actions.
    - **Passing and creative statistics also differ between the two groups**,
      suggesting that high scorers tend to contribute more broadly to
      attacking and creative play.

    Overall, the analysis demonstrates that high scorers have identifiable
    performance characteristics beyond goals scored. These findings support
    the use of player performance statistics as predictors when developing
    the machine learning model for **Business Requirement 2**.
    """
)



   
    
    
