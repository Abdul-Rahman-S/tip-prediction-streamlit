import pickle
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

st.title("Tip Prediction")
with open('tip.pkl','rb') as file:
    loaded_model=pickle.load(file)
    
total_bill=st.number_input("total_bill",0,100000,1)
time=st.selectbox("time",['Lunch','Dinner'])
size=st.number_input("size",0,100,1)

new={
    "total_bill":total_bill,
    "time":time,
    "size":size
}

df1=pd.DataFrame(new,index=[0])

df1['time']=df1['time'].map({'Lunch':0,'Dinner':1})

prediction = loaded_model.predict(df1)

if st.button("Predict"):
    st.success(f"Prediction Tip: {prediction[0]}")
# else:
#     st.error("No Tip")