import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf

#history = msft.history(period="1mo")


st.title("Stock Market App")
st.write("This is the day where I have decide to rock")

ticker_input  = st.text_input('Please enter ticker symbol', 'AAPL')


ticker_data = yf.Ticker(ticker_input)

start_date = st.date_input("Enter Starting date:",value=pd.to_datetime("2021-01-01"))
End_date = st.date_input("Enter Ending date:",value=pd.to_datetime("today"))

hist = ticker_data.history(start=start_date,end=End_date)

st.write("APPLE stock data")

# st.write(hist)
st.dataframe(hist)

# st.write("This plot is volume of the stock")
# st.line_chart(hist.Volume)


# st.write("This plot is closing price  of the stock")
# st.line_chart(hist.Close)

# import streamlit as st

# col1, col2, col3 = st.columns(3)

# with col1:
#    st.header("A cat")
#    st.image("https://static.streamlit.io/examples/cat.jpg")

# with col2:
#    st.header("A dog")
#    st.image("https://static.streamlit.io/examples/dog.jpg")

# with col3:
#    st.header("An owl")
#    st.image("https://static.streamlit.io/examples/owl.jpg")

# st.image('sunrise.jpg', caption='Sunrise by the mountains')

col1,col2 = st.columns(2)

with col1:
    st.write("This plot is volume of the stock")
    st.line_chart(hist.Volume)

with col2:
    st.write("This plot is closing price  of the stock")
    st.line_chart(hist.Close)

import pickle

# with open("lr.pkl","wb") as f:
#     pickle.dump(lr,f)

# with open("lr.pkl","wb") as f:
#     lr = pickle.load(f)


from xgboost import XGBClassifier

xgb = XGBClassifier()

xgb.fit(x_train,y_train) #if it is huge file, it will take lot of space


# with open("xgb.pkl","wb") as f:
#     pickle.dump(xgb,f)

with open("xgb.pkl","wb") as f:
    xgb = pickle.load(f)

xgb.predict(prediction_data)