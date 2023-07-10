# IPL Win Predictor

This is a Machine Learning project built with Streamlit that predicts the outcome of an IPL (Indian Premier League) match based on various inputs such as team, city, runs scored, wickets taken, overs completed, and ball number.
Propability prediction is done using Logistic Regression with accuracy score of 82% and winner is predicted using Random Forest model with an outstanding accuracy of 98%

## Working Demo : https://ipl-win-predictor-ogkz.onrender.com

## Snapshot of Project
![snapshot](https://github.com/MZKhan18/IPL-Win-Prediction/assets/83308074/1fb30ce2-e113-437c-8c3d-2a898ce69d2b)

## EDA and Data Visualisation using Power Bi
![dashboard](https://github.com/MZKhan18/IPL-Win-Prediction/assets/83308074/816935f2-ba97-4931-b3d4-824c5ec7076b)

## Usage

1. Select the bowling team and batting team from the dropdown menus.
2. Choose the city where the match is being played.
3. Enter the first innings total scored by the batting team.
4. Provide the runs scored, wickets taken, overs completed, and ball number in the respective fields.
5. Click the "Predict" button to see the prediction results.

The application will display the predicted win probabilities for the batting team and the bowling team, as well as the predicted winner of the match.

## Models

The prediction is based on two machine learning models: Random Forest (rfmodel) and Logistic Regression (lrmodel). These models have been trained on historical IPL match data to make predictions based on the input parameters.

## Data

The input data is collected and organized into a Pandas DataFrame. The DataFrame includes features such as bowling team, batting team, city, runs left, balls left, wickets left, total runs, current run rate (CRR), and required run rate (RRR). These features are used to make predictions using the trained machine learning models.

## Installation

To run the application locally, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/ipl-win-predictor.git
   ```

2. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

3. Run the Streamlit application:

   ```shell
   streamlit run app.py
   ```

   This will start the application on a local server, and you can access it by opening the provided URL in your web browser.


## Credits

This project was developed by MD Zama (https://github.com/MZKhan18). It uses the Streamlit library for the web application interface and the scikit-learn library for machine learning.
