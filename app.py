import streamlit as st
import os
import sys
import numpy as np
from src.components.model_prediction import ModelPrediction
import time

st.title('Customer Churn Analysis')

st.markdown('Churn Prediction using Machine Learning')

# ['Tenure', 'CC_Contacted_LY', 'rev_growth_yoy', 'rev_per_month', 'CC_Agent_Score', 'Account_user_count', 'City_Tier', 'Churn']
tenure = st.number_input(label='Tenure', min_value=0, max_value=100)

cc_contacted_ly = st.number_input(label='CC_Contacted_LY', min_value=0, max_value=100)

rev_growth_yoy = st.number_input(label='rev_growth_yoy', min_value=0, max_value=100)

rev_per_month = st.number_input(label='rev_per_month', min_value=0, max_value=100)

cc_agent_score = st.number_input(label='CC_Agent_Score', min_value=0, max_value=100)

no_of_user = st.number_input(label='Account_user_count', min_value=0, max_value=100)

city = st.number_input(label='City_Tier', min_value=0, max_value=3)

if all([tenure, cc_contacted_ly, rev_growth_yoy, rev_per_month, cc_agent_score, no_of_user, city]):


    progress = st.progress(value=0,text='Predicting Churn')

    for i in range(100):
        time.sleep(0.01)
        progress.progress(i+1)

    if st.button('Predict Churn'): 

        inputs = [tenure, cc_contacted_ly, rev_growth_yoy, rev_per_month, cc_agent_score, no_of_user, city]

        inputs = np.array(inputs).reshape(1, -1)

        model_prediction = ModelPrediction(config=None)

        output = model_prediction.make_prediction(inputs)


        if output[0] == 1:
            st.warning('The customer may Churn')
        else:
            st.success('The customer may not Churn')

        
        


