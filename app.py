#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import numpy as np
import joblib


# In[2]:


#loading the trained model
model=joblib.load("xgboost_model.pkl")
#title
st.title("ENERGY CONSUMPTION PREDICTION")
#different input fields 
Year=st.number_input("year",min_value=2005,max_value=2018,value=2005)
Month=st.number_input("month",min_value=1,max_value=12,value=1)
Weekday=st.number_input("weekday(0=Monday,6=Sunday)",min_value=0,max_value=6,value=0)
Hour=st.number_input("Hour(0-23)",min_value=0,max_value=23,value=0)
#prediction
if st.button("Predict"):
    X=np.array([[Year,Month,Weekday,Hour]])
    prediction=model.predict(X)
    st.success(f"Predicted Energy Consumption:{prediction[0]:.2f}MW")

