# Premier-League-Match-Prediction

## Project Overview
In this project, we will select the teams and kickoff time to predict the outcome of the match.

## Dataset
* Last 2 years Premier League Scores and Fixtures table and Shooting table for each team was scraped from a popular football staistics website and stored [here](https://github.com/dachuvg/Premier-League-Match-Prediction/blob/main/all_matches.csv)

## Model
* Data is cleaned and processed.
* Use the team, opponent, venue, kickoff columns as the features and the xG is set as the target.
* Train the data using a ridge regression model.
* Predictions from the model are used in a function where we compare the xG of both the teams to give the predicted outcome of the match.

  You can find the code [here](https://github.com/dachuvg/Premier-League-Match-Prediction/blob/main/Football%20Match%20Prediction.ipynb)

## Client App
* Streamlit based app.
* Feel free to take a look at the app [here](https://plmatchpred-bydarshanvg.streamlit.app/)

## Screenshots
![Pic1](https://github.com/dachuvg/Premier-League-Match-Prediction/blob/main/screenshots/pic1.png)
![Pic2](https://github.com/dachuvg/Premier-League-Match-Prediction/blob/main/screenshots/pic2.png)
