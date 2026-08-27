import pandas as pd
import streamlit as st
import joblib


def high_scorer_predictor_page():

    st.title("High Scorer Predictor")

    st.subheader("Player High Scorer Prediction")

    st.markdown(
        """
        **Business Requirement 2:** Develop and evaluate a machine learning model
        that can reliably identify potential high scorers using performance
        statistics other than goals scored, supporting player recruitment decisions.

        This page applies the final fitted machine learning pipeline to new player
        performance data to generate a High Scorer prediction and meets Business Requirment 3: Present the key analytical findings and machine learning results through an interactive Streamlit dashboard to support the club's recruitment analysis

        Enter a player's performance statistics below to generate a prediction
        using the final fitted machine learning pipeline.
        """
    )

    pipeline = joblib.load(
    "outputs/ml_pipeline/high_scorer_pipeline.pkl"
    )

    st.subheader("Player Statistics")

    position = st.selectbox(
        "Position",
        ("Goalkeeper","Defender", "Midfielder", "Forward")
    )
    appearances = st.number_input(
        "Appearances",
        min_value=1,
        step=1
    )

    shots = st.number_input(
        "Shots",
        min_value=0,
        step=1
    )

    shots_on_target = st.number_input(
        "Shots on target",
        min_value=0,
        step=1
    )

    blocked_shots = st.number_input(
        "Blocked shots",
        min_value=0,
        step=1
    )

    assists = st.number_input(
        "Assists",
        min_value=0,
        step=1

    )

    passes_per_match = st.number_input(
        "Passes per match",
        min_value=0.0
    )

    big_chances_created = st.number_input(
        "Big chances created",
        min_value=0,
        step=1
    )
    big_chances_missed = st.number_input(
        "Big chances missed",
        min_value=0,
        step=1
    )
    crosses = st.number_input(
        "Crosses",
        min_value=0,
        step=1
    )
    offsides = st.number_input(
        "Offsides",
        min_value=0,
        step=1
    )
    hit_woodwork = st.number_input(
        "Hit Woodwork",
        min_value=0,
        step=1
    )

    assists_per_appearance = assists / appearances

    shooting_accuracy = (
        shots_on_target / shots * 100
        if shots > 0 
        else 0
    )

    position_goalkeeper = int(position == "Goalkeeper")
    position_defender = int(position == "Defender")
    position_midfielder = int(position == "Midfielder")
    position_forward = int(position == "Forward")

    player_data = pd.DataFrame({
        "Appearances": [appearances],
        "Blocked shots": [blocked_shots],
        "Assists": [assists],
        "Passes per match": [passes_per_match],
        "Big chances created": [big_chances_created],
        "Crosses": [crosses],
        "Offsides": [offsides],
        "Hit woodwork": [hit_woodwork],
        "Shots": [shots],
        "Shots on target": [shots_on_target],
        "Shooting accuracy %": [shooting_accuracy],
        "Big chances missed": [big_chances_missed],
        "Position_Defender": [position_defender],
        "Position_Forward": [position_forward],
        "Position_Goalkeeper": [position_goalkeeper],
        "Position_Midfielder": [position_midfielder],
        "Assists per Appearance": [assists_per_appearance]
})

    if st.button("Predict High Scorer"):

        prediction = pipeline.predict(player_data)[0]
        probability = pipeline.predict_proba(player_data)[0][1] * 100

        if prediction:
            st.success("Prediction: Potential High Scorer")
            st.write(
                """
                The player's performance statistics demonstrate characteristics
                associated with high-scoring Premier League players.
                """
    )
        else:
            st.info(
                "Prediction: Not a High Scorer")
            st.write(
                """
                The player's performance statistics do not currently demonstrate
                the characteristics the model associates with high-scoring
                Premier League players.
                """
    )    
        st.write(f"High Scorer model probability: **{probability:.1f}%**")


       




    
    
    





    



    
