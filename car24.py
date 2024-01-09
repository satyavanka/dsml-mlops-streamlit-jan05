import streamlit as st
import pandas as pd
import pickle

st.title("Car Price Preciction from User")

# 4 inputs from user 

#fuel type, Transimission type, engine power, seats 

col1,col2 = st.columns(2)

with col1:
    fuel_type = st.radio("Fuel Type", ["Petrol","Diesel","CNG","Electric"])

with col2:
    transmission_type = st.selectbox("Transmission Type",["Manual","Automatic"])

col3,col4 = st.columns(2)

with col3:
    engine_power = st.slider("Enmgine Power", 500,5000,step=100)

with col4:
    seats = st.selectbox("Seats",[2,4,5,7])

model = pickle.load(open("car_pred", "rb"))
# model = pickle.load(open("car_pred","rb"))

encode_dict = {"fuel_type":{"Petrol":2,"Deisel":1,"CNG":3,"LPG":4,"Electric":5},
               "transmission":{"Manual":1,"Automatic":2}
               }

def model_pred(fuel_type,transmission_type,engine_power,seats):
    transmission_type = encode_dict["transmission"][transmission_type]
    fuel_type = encode_dict["fuel_type"][fuel_type]


    data = [[2018.0,1,40000,fuel_type,transmission_type,18.0,engine_power,85,seats]]

    return round(model.predict(data)[0], 2)

if st.button("Predict"):
    st.write(model_pred(fuel_type,transmission_type,engine_power,seats))
else:
    st.write("Click on Predict, once you are done with the data")