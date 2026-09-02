# Premier League High Scorer Predictor

## Project Overview

This project is a data analytics and machine learning application designed to support player recruitment decisions for a Premier League football club.

The project analyses historical Premier League player performance data across nine seasons, from 2015/16 to 2023/24, to investigate the characteristics associated with high-scoring players.

A supervised machine learning model is developed to classify whether a player demonstrates the characteristics of a `HighScorer`, defined as a player who scores 10 or more goals in a season. Goals scored are excluded from the predictor features to prevent data leakage and ensure the model identifies high-scoring characteristics using other player performance statistics.

The results of the data analysis and machine learning model are presented through an interactive Streamlit dashboard. The dashboard allows users to explore the key analytical findings, review the performance of the machine learning model, and enter player statistics to generate an interactive high-scorer prediction.

The application is intended to support recruitment analysis and scouting decisions rather than replace wider football knowledge and professional scouting processes.

## Dataset Content

- Describe your dataset. Choose a dataset of reasonable size to avoid exceeding the repository's maximum size and to have a shorter model training time. If you are doing an image recognition project, we suggest you consider using an image shape that is 100px × 100px or 50px × 50px, to ensure the model meets the performance requirement but is smaller than 100Mb for a smoother push to GitHub. A reasonably sized image set is ~5000 images, but you can choose ~10000 lines for numeric or textual data.

## Business Requirements

The project is designed as a player recruitment analysis service for a Premier League football club. The aim is to use historical player performance data to support recruitment teams in identifying players who demonstrate the characteristics of high scorers.

The project has three business requirements:

1. Analyse Premier League player performance data to identify the characteristics associated with high-scoring players.

2. Develop and evaluate a machine learning model that can reliably identify potential high scorers using performance statistics other than goals scored, supporting player recruitment decisions.

3. Present the key analytical findings and machine learning results through an interactive Streamlit dashboard to support the club's recruitment analysis.

## Hypothesis and how to validate?

- List here your project hypothesis(es) and how you envision validating it (them)

## The rationale to map the business requirements to the Data Visualizations and ML tasks

### Business Requirement 1 - Data Analysis and Visualisation

Exploratory data analysis and visualisations will be used to investigate the characteristics associated with high-scoring Premier League players. Relevant player statistics and playing positions will be compared against the `HighScorer` target to identify meaningful patterns and relationships.

### Business Requirement 2 - Machine Learning

A supervised binary classification task will be used to predict whether a player belongs to the `HighScorer` class.

Goals scored are excluded from the predictor features because they directly represent the outcome the model is intended to identify.

Multiple classification algorithms will be evaluated using training and unseen test data. As high scorers represent a small minority of the dataset, overall accuracy alone is not an appropriate measure of model success.

Particular attention will be given to precision for the `HighScorer` class. In the context of player recruitment, a false-positive prediction could lead to a club investing time and money in a player who does not demonstrate the required high-scoring profile. Therefore, reliable positive predictions are more important than identifying every possible high scorer.

### Business Requirement 3 - Dashboard

The key analytical findings and machine learning results will be presented through an interactive Streamlit dashboard, supported by clear visualisations and interpretations.

## ML Business Case

The machine learning task supports **Business Requirement 2** by predicting whether a Premier League player belongs to the `HighScorer` class.

### Aim

Develop a binary classification model capable of reliably identifying potential high scorers from player performance statistics without using goals scored as a predictor.

The model is intended to support player recruitment decisions by highlighting players whose performance statistics demonstrate characteristics associated with high scorers.

### Learning Method

Supervised binary classification will be used because the historical training data contains a known `HighScorer` target.

Multiple classification algorithms will be compared before selecting and optimising the final model.

### Ideal Outcome and Success/Failure Metrics

The ideal model should make reliable positive predictions so that players identified as potential high scorers are likely to genuinely belong to the `HighScorer` class.

Precision for the `HighScorer=True` class will be used as the primary success metric. A false-positive prediction could lead to a club investing time and money in a player who does not demonstrate the required high-scoring profile.

Missing a genuine high scorer is considered less costly than incorrectly recommending a player as a high scorer. Recall will therefore be treated as a secondary metric.

F1-score will also be considered to provide additional context on the balance between precision and recall.

The final model will be considered successful if it achieves a precision of at least **0.75** for the `HighScorer` class on unseen test data.

Training and test performance will also be compared to identify potential overfitting.

### Model Output

The model will output a binary prediction indicating whether a player is classified as a potential high scorer.

### Relevance to the User

The model provides a data-driven tool to support player recruitment by identifying players whose performance statistics resemble those associated with high scorers.

The prediction is intended to support recruitment analysis rather than replace wider scouting and decision-making processes.

### Heuristics and Training Data

The model uses the processed historical Premier League player dataset prepared during the project. Predictor features include player performance statistics and playing position, while goals scored are excluded from the predictors.

The dataset is split into training and test sets using stratification to preserve the proportion of high scorers. Missing predictor values are imputed using values learned from the training data to prevent test data from influencing model training.

## Dashboard Design

- List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
- Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).

## Unfixed Bugs

- You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment

### Heroku

The application is deployed on Heroku and can be accessed here:

[Premier League High Scorer Predictor](https://premier-league-highscorer-f334f7b727e7.herokuapp.com/)

To deploy the application to Heroku:

1. Create an account at Heroku and create a new application, choosing a unique application name.

2. Ensure the project contains the required deployment files, including `requirements.txt`, `Procfile`, `setup.sh` and `.python-version`.

3. Push the completed project to a GitHub repository.

4. From the Heroku application dashboard, open the **Deploy** section and select **GitHub** as the deployment method.

5. Connect Heroku to GitHub, search for the project repository and select **Connect**.

6. Select the `main` branch and choose **Deploy Branch**.

7. Heroku will install the dependencies from `requirements.txt` and start the Streamlit application using the command defined in the `Procfile`.

8. Once the build has completed successfully, select **Open App** to launch the deployed Streamlit application.

## Main Data Analysis and Machine Learning Libraries

- Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.

## Credits

- In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism.
- You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site

## Acknowledgements (optional)

- Thank the people who provided support through this project.
