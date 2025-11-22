import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Акции компаний", page_icon="📈", layout="wide", initial_sidebar_state="expanded")
st.sidebar.header("Выберите компанию и посмотрите графики цены и объёма торгов")
company = st.sidebar.selectbox("Компания", ["Apple", "Tesla", "Microsoft", "Google"])
st.title("Рынок акций реального времени")

if company == "Apple":
    st.title("Акции компании Apple")
    data = yf.Ticker("AAPL").history(period="max")
    st.subheader("График цены на закрытии торгов")
    st.line_chart(data.Close)
    st.subheader("График объёма торговли")
    st.line_chart(data.Volume)

elif company == "Tesla":
    st.title("Акции компании Tesla")
    data = yf.Ticker("TSLA").history(period="max")
    st.subheader("График цены на закрытии торгов")
    st.line_chart(data.Close)
    st.subheader("График объёма торговли")
    st.line_chart(data.Volume)

elif company == "Microsoft":
    st.title("Акции компании Microsoft")
    data = yf.Ticker("MSFT").history(period="max")
    st.subheader("График цены на закрытии торгов")
    st.line_chart(data.Close)
    st.subheader("График объёма торговли")
    st.line_chart(data.Volume)

elif company == "Google":
    st.title("Акции компании Google")
    data = yf.Ticker("GOOGL").history(period="max")
    st.subheader("График цены на закрытии торгов")
    st.line_chart(data.Close)
    st.subheader("График объёма торговли")
    st.line_chart(data.Volume)

else:
    st.stop