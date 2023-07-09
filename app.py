import streamlit as st
import pickle
import numpy as np
import pandas as pd

st.title('IPL Win Predictor')

rfmodel = pickle.load(open('rfModel.pkl','rb'))
lrmodel = pickle.load(open('lrModel.pkl','rb'))

col1 , col2 = st.columns(2)
team = {'Royal Challengers Bangalore','Mumbai Indians','Chennai Super Kings','Kolkata Knight Riders','Rajasthan Royals',
        'Sunrisers Hyderabad','Delhi Capitals','Punjab Kings','Lucknow Super Giants','Gujarat Titans'}
with col1:
    bowling_team = st.selectbox('Select Bowling Team',team)
with col2:
    team.remove(bowling_team)
    batting_team = st.selectbox('Select Batting Team', team)

col1 , col2 = st.columns(2)
with col1:
    allCity = {'Ahmedabad', 'Kolkata', 'Mumbai', 'Navi Mumbai', 'Pune', 'Dubai',
       'Sharjah', 'Abu Dhabi', 'Delhi', 'Chennai', 'Hyderabad',
       'Visakhapatnam', 'Chandigarh', 'Bengaluru', 'Jaipur', 'Indore',
       'Bangalore', 'Raipur', 'Ranchi', 'Cuttack', 'Dharamsala', 'Nagpur',
       'Johannesburg', 'Centurion', 'Durban', 'Bloemfontein',
       'Port Elizabeth', 'Kimberley', 'East London', 'Cape Town'}
    city = st.selectbox("Select City",allCity)
with col2:
    target = st.number_input("Enter first innings total")

col1, col2= st.columns(2)
with col1:
    runsScored = st.number_input("Enter Runs Scored")
with col2:
    wickets = st.number_input("Enter wickets out")

col1,col2 = st.columns(2)
with col1:
    OversCompleted = st.number_input("Enter Over number")
with col2:
    ball = st.number_input("Enter ball number")



if st.button('Predict'):
    runs_left = target - runsScored
    balls_left = 120 - (OversCompleted * 6 + ball)
    wicket_left = 10 - wickets
    crr = (runsScored * 6) / (120 - balls_left)
    rrr = (runs_left * 6) / balls_left

    input_df = pd.DataFrame({'bowling_team':[bowling_team],'batting_team':[batting_team],'city':[city],
                             'runs_left':runs_left,'balls_left':[balls_left],'wickets_left':[wicket_left],
                             'total_run_x':[target],'crr':[crr],'rrr':[rrr]})
    prob = lrmodel.predict_proba(input_df)
    win = prob[0][1]
    loss = prob[0][0]
    st.header(batting_team + " : " + str(round(win*100,2)) + "%")
    st.header(bowling_team + " : " + str(round(loss * 100,2)) + "%")

    result = rfmodel.predict(input_df)
    if result ==1:
        winner = batting_team
    else:
        winner = bowling_team
    st.header("Winner : "+winner)
