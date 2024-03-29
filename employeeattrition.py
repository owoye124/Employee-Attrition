import pandas as pd
import streamlit as st
import warnings
warnings.filterwarnings('ignore')
import joblib
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('employee_attrition.csv')
model = joblib.load('employeeattrition.pkl')

st.markdown("<h1 style = 'color: #0C2D57; text-align: center; font-family: Arial'>EMPLOYEE ATTRITION </h1>", unsafe_allow_html = True)
st.markdown("<h4 style = 'margin: -30px; color: #F11A7B; text-align: center; font-family: cursive '>Built By AKPOVI ROSEMARY OWOMARE</h4>", unsafe_allow_html = True)
st.markdown("<br>", unsafe_allow_html=True)
st.image('png Workers 1.png')

st.markdown("<h4 style = 'margin: -30px; color: green; text-align: center; font-family: helvetica '>Project Overview</h4>", unsafe_allow_html = True) #centralize heading

st.write("The objective of this machine learning project is to construct a dependable predictive model capable of accurately predicting employee attrition within our organization. By analyzing historical employee data, our aim is to uncover patterns and essential factors associated with attrition. The resulting model will enable our company to preemptively tackle attrition risks, execute tailored retention initiatives, and ultimately improve employee satisfaction and loyalty.")
st.markdown("<br>", unsafe_allow_html=True) # create space before the next line

st.dataframe(data, use_container_width= True)

st.sidebar.image('png employee attrition.png')

mnth_hr = st.sidebar.number_input('Average Monthly Hours Worked', data['average_montly_hours'].min(), data['average_montly_hours'].max())
sati_lv = st.sidebar.number_input('Satisfaction Level', data['satisfaction_level'].min(), data['satisfaction_level'].max())
last_ev = st.sidebar.number_input('Last Evaluation', data['last_evaluation'].min(), data['last_evaluation'].max())
numb_pr = st.sidebar.number_input('Number Of Project Done', data['number_project'].min(), data['number_project'].max())
time_sp = st.sidebar.number_input('Time Spent In Company', data['time_spend_company'].min(), data['time_spend_company'].max())
dept__  = st.sidebar.selectbox('Department Worked', data['department'].unique())
salary  = st.sidebar.selectbox('Salary Received', data['salary'].unique())

st.markdown("<br>", unsafe_allow_html=True) 
st.markdown("<br>", unsafe_allow_html=True) 
st.markdown("<br>", unsafe_allow_html=True) 

st.markdown("<h4 style = 'margin: -30px; color: green; text-align: center; font-family: helvetica '>Input Variable</h4>", unsafe_allow_html = True)



vars = pd.DataFrame()
vars['average_montly_hours'] = [mnth_hr]
vars['satisfaction_level'] = [sati_lv]
vars['last_evaluation'] = [last_ev]
vars['number_project'] = [numb_pr]
vars['time_spend_company'] = [time_sp]
vars['department'] = [dept__]
vars['salary'] = [salary]

st.subheader('Input variables', divider = True)
st.dataframe(vars)

dep_encoder = joblib.load('department_encoder.pkl')
sal_encoder = joblib.load('salary_encoder.pkl')

#transform the user inputs 
vars['department'] = dep_encoder.transform(vars[['department']])
vars['salary'] = sal_encoder.transform(vars[['salary']])


#predict the user input
if st.button('Predict Attrition'):
    predicted = model.predict(vars)
    if predicted[0] == 0:
        st.success('Not Attrited Employee')
    else:
        st.error('Attrited Employee')
