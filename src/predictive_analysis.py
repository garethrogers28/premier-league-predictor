def predict_high_scorer(player_data, pipeline):
    """
    Run the fitted ML pipeline on user-provided player data and return
    the predicted class and high-scorer probability.
    """
    prediction = pipeline.predict(player_data)[0]
    probability = pipeline.predict_proba(player_data)[0][1] * 100

    return prediction, probability