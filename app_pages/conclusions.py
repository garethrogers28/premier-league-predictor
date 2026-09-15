import streamlit as st


def conclusions_page():
    st.header("Overall Conclusions")

    st.markdown(
        """
            This project set out to identify the characteristics associated
            with high-scoring Premier League players and to build a machine
            learning model capable of supporting recruitment decisions.

            The exploratory analysis showed that **playing position, shots,
            shots on target and creative involvement** are strongly
            associated with players classified as high scorers.

            The final tuned **XGBoost model** achieved a precision of **0.80**
            for the `HighScorer=True` class on unseen test data, exceeding the
            project's minimum target of **0.75**. This means that when the
            model identifies a player as a potential high scorer, it is
            correct in the large majority of cases.

            Overall, the project demonstrates that historical performance
            statistics can meaningfully support recruitment analysis. The
            model is best used as a **supporting tool alongside professional
            scouting**, rather than as a standalone recruitment decision.
        """
        )

    st.markdown("---")

    st.header("Future Development")

    st.markdown(
        """
        Several areas could be explored to extend this project further:

        - **Additional seasons and leagues:** Incorporating more recent
          seasons or other leagues could improve the model's relevance
          and help assess whether the identified characteristics
          generalise beyond the Premier League.
        - **Recall improvement:** The tuned model prioritises precision
          over recall. Future work could explore alternative thresholds
          or cost-sensitive approaches to recover more genuine high
          scorers without significantly reducing precision.
        - **Position-specific models:** Training separate models for
          each playing position may better capture the different
          performance profiles associated with high scorers in each
          role.
        - **Model monitoring:** If deployed for ongoing use, the model's
          performance should be periodically reassessed as player and
          league trends evolve over time.
        """
    )
