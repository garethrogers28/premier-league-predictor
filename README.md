# Premier League High Scorer Predictor

## Project Overview

This project is a data analytics and machine learning application designed to support player recruitment decisions for a Premier League football club.

The project analyses historical Premier League player performance data across nine seasons, from 2015/16 to 2023/24, to investigate the characteristics associated with high-scoring players.

A supervised machine learning model is developed to classify whether a player demonstrates the characteristics of a `HighScorer`, defined as a player who scores 10 or more goals in a season. Goals scored are excluded from the predictor features to prevent data leakage and ensure the model identifies high-scoring characteristics using other player performance statistics.

The results of the data analysis and machine learning model are presented through an interactive Streamlit dashboard. The dashboard allows users to explore the key analytical findings, review the performance of the machine learning model, and enter player statistics to generate an interactive high-scorer prediction.

The application is intended to support recruitment analysis and scouting decisions rather than replace wider football knowledge and professional scouting processes.

## Dataset Content

The dataset contains historical Premier League player performance statistics covering nine seasons from **2015/16 to 2023/24**.

The original data was provided across nine CSV files, with each file representing a single Premier League season. These files were combined into a single dataset during the data collection stage, with a `Season` column added to identify the season associated with each player record.

The data contains player-level performance statistics including:

- Appearances and playing position
- Shooting and attacking statistics
- Assists and creative statistics
- Passing statistics
- Discipline and defensive statistics
- Goalkeeper specific stats

During data cleaning, duplicate records, invalid player-season records and inconsistent data formats were identified and handled. Missing values were also investigated to distinguish between structural missing values and genuinely unavailable statistics.

Following data cleaning, the dataset contains **8,196 player-season records** across the nine Premier League seasons.

For machine learning, a binary target variable named `HighScorer` was created. A player is classified as a high scorer when they scored **10 or more goals in a season**.

Feature engineering and feature selection produced **17 predictor features** for the final machine learning model. Goals scored and other features that directly reveal goals scored were excluded from the predictors to prevent data leakage.

## Business Requirements

The project is designed as a player recruitment analysis service for a Premier League football club. The aim is to use historical player performance data to support recruitment teams in identifying players who demonstrate the characteristics of high scorers.

The project has three business requirements:

1. Analyse Premier League player performance data to identify the characteristics associated with high-scoring players.

2. Develop and evaluate a machine learning model that can reliably identify potential high scorers using performance statistics other than goals scored, supporting player recruitment decisions.

3. Present the key analytical findings and machine learning results through an interactive Streamlit dashboard to support the club's recruitment analysis.

## Epics and User Stories

The project was developed around three main epics that reflect the business requirements and the needs of a recruitment analyst using the application.

### Epic 1 - Player Performance Analysis

The aim of this epic is to investigate the characteristics associated with high-scoring Premier League players.

**User Story 1**

As a recruitment analyst, I want to explore and compare historical player performance statistics so that I can understand the characteristics associated with high-scoring players.

### Epic 2 - High Scorer Machine Learning Model

The aim of this epic is to develop and evaluate a machine learning model capable of identifying players who demonstrate characteristics associated with high scorers.

**User Story 2**

As a recruitment analyst, I want a machine learning model that can reliably identify potential high scorers using performance statistics other than goals scored so that I can use the prediction to support recruitment decisions.

### Epic 3 - Interactive Recruitment Dashboard

The aim of this epic is to make the project's analysis and machine learning results accessible through an interactive dashboard.

**User Story 3**

As a recruitment analyst, I want to view the player analysis and model performance and enter player statistics to generate a high-scorer prediction so that I can use the project's findings through a simple interactive interface.

## The rationale to map the business requirements to the Data Visualizations and ML tasks

### Business Requirement 1 - Data Analysis and Visualisation

Exploratory data analysis and visualisations were used to investigate the characteristics associated with high-scoring Premier League players. Relevant player statistics and playing positions were compared against the `HighScorer` target to identify meaningful patterns and relationships.

### Business Requirement 2 - Machine Learning

A supervised binary classification task was used to predict whether a player belongs to the `HighScorer` class.

Goals scored are excluded from the predictor features because they directly represent the outcome the model is intended to identify.

Multiple classification algorithms were evaluated using training and unseen test data. As high scorers represent a small minority of the dataset, overall accuracy alone is not an appropriate measure of model success.

Particular attention was given to precision for the `HighScorer` class. In the context of player recruitment, a false-positive prediction could lead to a club investing time and money in a player who does not demonstrate the required high-scoring profile. Therefore, reliable positive predictions are more important than identifying every possible high scorer.

### Business Requirement 3 - Dashboard

The key analytical findings and machine learning results were presented through an interactive Streamlit dashboard, supported by clear visualisations and interpretations.

## ML Business Case

The machine learning task supports **Business Requirement 2** by predicting whether a Premier League player belongs to the `HighScorer` class.

### Aim

Develop a binary classification model capable of reliably identifying potential high scorers from player performance statistics without using goals scored as a predictor.

The model is intended to support player recruitment decisions by highlighting players whose performance statistics demonstrate characteristics associated with high scorers.

### Learning Method

Supervised binary classification was used because the historical training data contains a known `HighScorer` target.

Multiple classification algorithms were compared before selecting and optimising the final model.

### Ideal Outcome and Success/Failure Metrics

The ideal model should make reliable positive predictions so that players identified as potential high scorers are likely to genuinely belong to the `HighScorer` class.

Precision for the `HighScorer=True` class was used as the primary success metric. A false-positive prediction could lead to a club investing time and money in a player who does not demonstrate the required high-scoring profile.

Missing a genuine high scorer is considered less costly than incorrectly recommending a player as a high scorer. Recall was therefore treated as a secondary metric.

F1-score was also considered to provide additional context on the balance between precision and recall.

The final model was considered successful if it achieved a precision of at least **0.75** for the `HighScorer` class on unseen test data.

Training and test performance were also compared to identify potential overfitting.

### Model Output

The model outputs a binary prediction indicating whether a player is classified as a potential high scorer.

### Relevance to the User

The model provides a data-driven tool to support player recruitment by identifying players whose performance statistics resemble those associated with high scorers.

The prediction is intended to support recruitment analysis rather than replace wider scouting and decision-making processes.

### Heuristics and Training Data

The model uses the processed historical Premier League player dataset prepared during the project. Predictor features include player performance statistics and playing position, while goals scored are excluded from the predictors.

The dataset is split into training and test sets using stratification to preserve the proportion of high scorers. Missing predictor values are imputed using values learned from the training data to prevent test data from influencing model training.

## Dashboard Design

The project results are presented through an interactive Streamlit dashboard consisting of five pages.

### Project Summary

The Project Summary page introduces the project and provides context for the analysis and machine learning tasks. It includes:

- An overview of the project and its purpose.
- A summary of the dataset used.
- The three business requirements.
- The machine learning business case and success criteria.

### Player Analysis

The Player Analysis page supports **Business Requirement 1** by presenting the main findings from the exploratory data analysis.

The page includes:

- Analysis of the relationship between playing position and high scorers.
- Comparison of attacking statistics between high scorers and other players.
- Comparison of passing and creative statistics between high scorers and other players.
- Written interpretations explaining the key findings from each visualisation.

### Project Hypothesis

The Project Hypothesis page presents the project hypothesis and the evidence used to validate it during the exploratory data analysis.

The hypothesis proposes that Premier League players classified as high scorers will demonstrate stronger attacking statistics, particularly shots and shots on target, than players who are not classified as high scorers.

The page includes:

- The project hypothesis.
- A comparison of average shooting statistics between high scorers and non-high scorers.
- The key figures identified during the analysis.
- The outcome of the hypothesis validation.

### Model Performance

The Model Performance page supports **Business Requirement 2** by presenting the development and evaluation of the machine learning model.

The page includes:

- The machine learning business target and primary success metric.
- An overview of the final machine learning pipeline.
- Comparison of the baseline classification models.
- Performance of the optimised XGBoost model on training and unseen test data.
- A confusion matrix showing the final model's classifications.
- Feature importance showing which player statistics contributed most strongly to the model.
- An interpretation of the final model's performance against the business requirement.

### High Scorer Predictor

The High Scorer Predictor page supports **Business Requirements 2 and 3** by allowing the user to interact with the final trained machine learning pipeline.

The user can enter player performance statistics including appearances, position, shooting, attacking, passing and creative statistics.

The submitted values are transformed into the same feature structure used during model training and passed to the saved machine learning pipeline.

The dashboard then displays:

- A classification indicating whether the player is identified as a potential high scorer.
- The model probability associated with the high-scorer class.
- A short explanation of the prediction.

The prediction is intended to support recruitment analysis and should be considered alongside wider scouting information rather than as a standalone recruitment decision.

## Testing

Testing was carried out throughout the project to ensure that the data processing, machine learning pipeline, Streamlit dashboard and deployed application functioned as expected.

### Data and Machine Learning Testing

The Jupyter notebooks were run during development to verify that each stage of the data pipeline completed successfully.

The following areas were checked:

- The nine Premier League season datasets were successfully combined into a single dataset.
- Duplicate and invalid player-season records were identified and handled during data cleaning.
- Data types and missing values were inspected and handled appropriately.
- The `HighScorer` target was correctly created using the threshold of 10 or more goals in a season.
- Features that directly revealed goals scored were excluded from the predictor features to prevent data leakage.
- Training and test data were separated using a stratified split to preserve the proportion of high scorers.
- Missing predictor values were handled within the machine learning pipeline.
- Logistic Regression, Random Forest and XGBoost classifiers were evaluated on unseen test data.
- The final optimised XGBoost model achieved a precision of **0.80** for the `HighScorer=True` class on unseen test data, exceeding the project success criterion of **0.75**.
- The fitted machine learning pipeline was saved and successfully loaded by the Streamlit application.

### Streamlit Dashboard Testing

The Streamlit dashboard was manually tested to ensure that the application pages, visualisations and interactive predictor worked as expected.

| Feature               | Test Performed                      | Expected Result                                                      | Result |
| --------------------- | ----------------------------------- | -------------------------------------------------------------------- | ------ |
| Application           | Launch the Streamlit application    | Application loads without errors                                     | Pass   |
| Sidebar Navigation    | Select each page from the sidebar   | Selected page loads correctly                                        | Pass   |
| Project Summary       | Open the Project Summary page       | Project information and business requirements are displayed          | Pass   |
| Player Analysis       | Open the Player Analysis page       | Analysis and interactive visualisations are displayed correctly      | Pass   |
| Project Hypothesis    | Open the Project Hypothesis page    | Hypothesis, validation evidence and outcome are displayed correctly  | Pass   |
| Model Performance     | Open the Model Performance page     | Model metrics, confusion matrix and feature importance are displayed | Pass   |
| High Scorer Predictor | Open the predictor page             | Player input controls and prediction interface are displayed         | Pass   |
| Predictor Inputs      | Enter player performance statistics | Submitted values are accepted by the application                     | Pass   |
| Predictor Output      | Submit player statistics            | A High Scorer or Not High Scorer classification is returned          | Pass   |
| Model Probability     | Submit player statistics            | Model probability is displayed alongside the classification          | Pass   |
| Position Input        | Select different playing positions  | Selected position is correctly included in the model input           | Pass   |
| Heroku Deployment     | Open the deployed application       | Application loads and functions correctly on Heroku                  | Pass   |

### Deployment Testing

Following deployment to Heroku, the live application was manually checked to confirm that:

- The application loaded successfully.
- All five dashboard pages were accessible.
- Interactive Plotly visualisations displayed correctly.
- The saved machine learning pipeline loaded correctly.
- Player statistics could be submitted through the High Scorer Predictor.
- Predictions and model probabilities were returned successfully.

## Unfixed Bugs and Limitations

There are currently no known unfixed functional bugs within the application.

The following limitations should be considered:

- **Class imbalance** - Only approximately **2.6%** of player-season records are high scorers, making the classification task challenging.
- **Precision and recall** - The final model achieved **0.80 precision**, exceeding the target of **0.75**, but recall was **0.38**. This reflects the project's priority of reducing false-positive recruitment recommendations.
- **Feature importance** - `Shots on target` has a strong influence on the model. Feature importance should not be interpreted as causation or a universal threshold for identifying high scorers.
- **Historical data** - The model was trained on Premier League data from **2015/16 to 2023/24** and may become less representative as player and league patterns change.
- **Recruitment decisions** - The model identifies characteristics associated with historical high scorers and does not guarantee future goal-scoring performance. It should support, rather than replace, professional scouting.

## Deployment

### Heroku

The application is deployed on Heroku and can be accessed here:

[Premier League High Scorer Predictor](https://premier-league-highscorer-f334f7b727e7.herokuapp.com/)

To deploy the application to Heroku:

1. Create a Heroku account and create a new application with a unique application name.

2. Ensure the project contains the required deployment files, including `requirements.txt`, `Procfile` and `.python-version`.

3. The `Procfile` should contain the command used to start the Streamlit application:

   `web: streamlit run app.py --server.port=$PORT`

4. Streamlit configuration and theme settings are stored in `.streamlit/config.toml`.

5. Push the completed project to a GitHub repository.

6. From the Heroku application dashboard, open the **Deploy** section and select **GitHub** as the deployment method.

7. Connect Heroku to GitHub, search for the project repository and select **Connect**.

8. Select the `main` branch and choose **Deploy Branch**.

9. Heroku will install the dependencies from `requirements.txt` and start the Streamlit application using the command defined in the `Procfile`.

10. Once the build has completed successfully, select **Open App** to launch the deployed Streamlit application.

## Technologies Used

### Languages

- **Python** - Used for data collection, data cleaning, exploratory data analysis, feature engineering, machine learning and the Streamlit application.
- **Markdown** - Used throughout the Jupyter notebooks and project documentation to explain the analysis, findings and development process.

### Python Packages

- **Pandas** - Used to load, combine, clean, transform and analyse the Premier League player datasets.
- **NumPy** - Used for numerical operations and data manipulation during the analysis and machine learning workflow.
- **Matplotlib** - Used to create data visualisations during exploratory data analysis and model evaluation.
- **Plotly** - Used to create interactive visualisations for the Streamlit dashboard.
- **Scikit-learn** - Used for train/test splitting, preprocessing, model pipelines, baseline classification models, model evaluation and hyperparameter optimisation.
- **XGBoost** - Used to build the final `XGBClassifier` high-scorer classification model.
- **Joblib** - Used to save and load the fitted machine learning pipeline.
- **Streamlit** - Used to build the interactive dashboard and High Scorer Predictor.

## Credits

### Learning and Development Resources

- **Code Institute** - The Predictive Analytics course material and walkthrough projects were used as guidance for the overall project structure, machine learning workflow and Streamlit dashboard development.
- **Pandas Documentation** - Used as a reference for data manipulation, cleaning and analysis.
- **Scikit-learn Documentation** - Used as a reference for machine learning pipelines, preprocessing, model training, hyperparameter optimisation and model evaluation.
- **XGBoost Documentation** - Used as a reference when developing and configuring the `XGBClassifier` model.
- **Streamlit Documentation** - Used as a reference when developing and configuring the interactive dashboard.
- **Plotly Documentation** - Used as a reference when creating interactive dashboard visualisations.
- **ChatGPT** - Used as a development support tool for troubleshooting issues, explaining programming and machine learning concepts, and helping to quickly locate relevant areas of official documentation. All project code, analysis and implementation decisions were reviewed and understood as part of the development process.

### Dataset

The Premier League player statistics used in this project were obtained from the Kaggle dataset [English Premier League EPL Player Stats(till23/24)](https://www.kaggle.com/datasets/krishanthbarkav/english-premier-leagueepl-player-statistics).
