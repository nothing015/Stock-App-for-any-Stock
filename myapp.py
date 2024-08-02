import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price APP

Shown here are the stock closing price and volume of Apple
""")

tickerSymbol = 'AAPL'

# Try fetching the data and display it
try:
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period='1d', start='2015-5-31', end='2024-5-31')
    
    if not tickerDf.empty:
        st.write("### Data for APPLE INC.")
        st.write(tickerDf)  # Display the dataframe
        st.line_chart(tickerDf['Close'], width=0, height=0, use_container_width=True)
        st.line_chart(tickerDf['Volume'], width=0, height=0, use_container_width=True)
    else:
        st.write(f"No data found for {tickerSymbol}.")
except Exception as e:
    st.write(f"Failed to get data for {tickerSymbol}. Reason: {e}")
