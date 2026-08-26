import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def model_performance_page():

    st.title("Model Performance")

    st.write(
        """
        This page evaluates how well the final machine learning model performs
        against the success criteria defined in the ML Business Case.
        """
    )

    st.subheader("ML Business Target")

    st.markdown(
    """
    The primary success metric for the model is **precision** for the
    `HighScorer=True` class.

    The model is considered successful if it achieves a precision of at least
    **0.75** on unseen test data.
    """
    )

    st.metric(
    label="Final Test Precision",
    value="0.80",
    delta="+0.05 above target"
)

    st.subheader("Pipeline Steps")

    st.markdown(
    """
    The final machine learning pipeline consists of two stages applied in order:

    1. **Missing Value Imputation**
       - `SimpleImputer(strategy="median")` is used to replace missing predictor
         values with the median values learned from the training data.
       - This ensures the same preprocessing is applied consistently when the
         model receives new data.

    2. **Classifier**
       - `XGBClassifier` performs the binary classification of players as
         high scorers or non-high scorers.
       - The classifier was optimised using `GridSearchCV` with 5-fold
         cross-validation, using precision as the scoring metric.

    The best hyperparameters identified during optimisation were:

    - `learning_rate`: **0.01**
    - `max_depth`: **3**
    - `n_estimators`: **100**
    - `scale_pos_weight`: **1**

    The final fitted pipeline is saved and used by the High Scorer Predictor
    to apply the same preprocessing and classification steps to new player data.
    """
)

    st.subheader("Baseline Model Comparison")

    model_comparison = pd.DataFrame({
    "Model": [
        "Logistic Regression",
        "Random Forest",
        "XGBoost"
    ],
    "Precision": [
        0.412371,
        0.674419,
        0.700000
    ],
    "Recall": [
        0.952381,
        0.690476,
        0.666667
    ],
    "F1 Score": [
        0.575540,
        0.682353,
        0.682927
    ]
})

    st.dataframe(model_comparison, hide_index=True)
    fig = px.bar(
    model_comparison,
    x="Model",
    y=["Precision", "Recall", "F1 Score"],
    barmode="group",
    title="Baseline Model Performance Comparison"
)

    fig.add_hline(
    y=0.75,
    line_dash="dash",
    annotation_text="Business Target: 0.75 Precision"
)

    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
    """
    **Interpretation:**

    XGBoost achieved the highest baseline precision at **0.70**, making it the
    closest model to the required precision of **0.75**.

    Random Forest achieved a similar F1-score, while Logistic Regression
    achieved the highest recall but substantially lower precision.

    XGBoost was therefore selected for hyperparameter optimisation because it
    performed best against the primary business metric.
    """
)

    st.subheader("Tuned XGBoost Performance")

    tuned_metrics = pd.DataFrame({
    "Dataset": [
        "Training",
        "Test"
    ],
    "Precision": [
        0.94,
        0.80
    ],
    "Recall": [
        0.54,
        0.38
    ],
    "F1 Score": [
        0.68,
        0.52
    ]
})

    st.dataframe(tuned_metrics, hide_index=True)

    fig = px.bar(
    tuned_metrics,
    x="Dataset",
    y=["Precision", "Recall", "F1 Score"],
    barmode="group",
    title="Tuned XGBoost Performance"
)

    fig.add_hline(
    y=0.75,
    line_dash="dash",
    annotation_text="Business Target: 0.75 Precision"
)

    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
    """
    **Interpretation:**

    After hyperparameter optimisation, the tuned XGBoost model achieved a
    precision of **0.80** on unseen test data, exceeding the business target
    of **0.75**.

    Recall decreased to **0.38**, meaning that the model misses more genuine
    high scorers. This trade-off is acceptable within the defined business
    case because reliable positive predictions are prioritised over identifying
    every possible high scorer.

    The final model therefore meets the defined ML business requirement.
    """
)

    st.subheader("Test Confusion Matrix")

    confusion_matrix = [
    [1594, 4],
    [26, 16]
]

    fig = go.Figure(
    data=go.Heatmap(
        z=confusion_matrix,
        x=["Predicted: Not High Scorer", "Predicted: High Scorer"],
        y=["Actual: Not High Scorer", "Actual: High Scorer"],
        text=confusion_matrix,
        texttemplate="%{text}"
    )
)

    fig.update_layout(
    title="Tuned XGBoost Test Confusion Matrix",
    xaxis_title="Predicted Class",
    yaxis_title="Actual Class"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
        """
        **Interpretation:**
    
        On the unseen test data, the tuned XGBoost model:
    
        - Correctly classified **1,594 non-high scorers**.
        - Incorrectly classified **4 non-high scorers as high scorers**.
        - Missed **26 genuine high scorers**.
        - Correctly identified **16 high scorers**.
    
        Of the 20 players predicted as high scorers, 16 were correctly classified.
        This resulted in a precision of **0.80** for the `HighScorer=True` class,
        exceeding the project's minimum target of **0.75**.
    
        The relatively low number of false-positive predictions aligns with the
        business objective of prioritising reliable high-scorer recommendations.
        """
        )

    st.subheader("Feature Importance")

    feature_importance = pd.DataFrame({
    "Feature": [
        "Shots on target",
        "Assists",
        "Passes per match",
        "Shooting accuracy %",
        "Crosses",
        "Assists per Appearance",
        "Shots",
        "Hit woodwork",
        "Blocked shots",
        "Big chances created",
        "Position_Forward",
        "Offsides"
    ],
    "Importance": [
        0.818528,
        0.033573,
        0.030430,
        0.026043,
        0.020773,
        0.017925,
        0.015932,
        0.011664,
        0.008016,
        0.007565,
        0.004924,
        0.004627
    ]
    })

    feature_importance = feature_importance.sort_values(
    "Importance",
    ascending=True
)

    fig = px.bar(
    feature_importance,
    x="Importance",
    y="Feature",
    orientation="h",
    title="Tuned XGBoost Feature Importance"
)

    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
    """
    **Interpretation:**

    `Shots on target` is by far the most influential feature in the tuned
    XGBoost model, accounting for substantially more feature importance than
    any other predictor.

    Other features, including assists, passes per match, shooting accuracy
    and crosses, make smaller contributions to the model's predictions.

    This indicates that shots on target is the strongest predictor used by
    the final model when distinguishing between high scorers and non-high
    scorers.
    """
)

    st.subheader("Conclusion")

    st.markdown(
    """
    The tuned XGBoost model achieved a precision of **0.80** for the
    `HighScorer=True` class on unseen test data, exceeding the project's
    minimum business target of **0.75**.

    The optimisation increased precision at the cost of recall, meaning the
    final model makes fewer false-positive high-scorer predictions but misses
    more genuine high scorers. This trade-off aligns with the defined business
    case, where reliable positive predictions are prioritised.

    Feature importance analysis identified **shots on target** as the dominant
    predictor used by the final model, with other attacking, passing and
    creative statistics making smaller contributions.

    Overall, the final model satisfies **Business Requirement 2** and provides
    a suitable basis for the interactive High Scorer Predictor.
    """
)