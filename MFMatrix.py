import pandas as pd
import streamlit as st

SHEET_ID = '1tUmm4rh-BH53wd8d5xCug9OSYMxqd6CB'
SHEET_NAME = ['Rank','Data','Code']

url1 = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME[0]}'
Rank = pd.read_csv(url1)

url2 = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME[1]}'
Data = pd.read_csv(url2)

url3 = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME[2]}'
Code = pd.read_csv(url3)

st.title("Welcome to Azreal")

st.header("About the Mutual Fund Matrix")

st.markdown("Azreal is a Web based application created by Dhruv Suresh which helps users make better investment decisions in Mutual Funds using the power of Data Analytics.")
st.markdown("Mutual Funds are deemed to be one of the most safe investments based on popular opinion. A consistent monthly investment strategy devoting 10-20% of monthly income (varies from person to person) parked in a good performing mutual fund could yield very promising returns in the long run.")
st.markdown("However with the advent and advancement of the finance and technology domain, there is a huge influx of funds and a plethora to choose from which can be very daunting to the consumer. Azreal's Mutual Fund Matrix aims to tackle this issue and recommend the best funds based off of histoical performance.")
st.markdown("Azreal's Mutual Fund matrix pulls all existing historical data for every mutual fund listed by the The Association of Mutual Funds in India (AMFI). It then calculates various parameters such as the 3 and 5 year return, standard deviation of yearly returns etc. Now having these various parameters Azreal determines which fund has provided the most consistent returns with the least amount of risk.")
st.markdown("Since the data extraction process is very time consuming, I have saved the final findings as of September 2022 and is displayed as below in the Rank, Data and Code List Tabs respectively. The Rank sheet contains the final ranking having best to worst ranked top to down in that order. The Data contains all the details about the funds' historical performances. The Code List is a reference which can be used to see which Scheme Code corresponds to which Scheme Name. The files can also be downloaded as .csv by pressing the Download as csv button")
st.markdown("** Historical performance does not guarantee future performance. Please read all scheme related documents carefully before investing.")
st.markdown("** Please do your own due diligence before investing. This is not financial advice.")

tab1, tab2, tab3 = st.tabs(["Rank", "Data", "Code List"])

with tab1:
   st.header("Rank")
   st.download_button(label = "Download Rank as csv",data = Rank.to_csv(), file_name = "Rank.csv")
   st.dataframe(Rank,height = 10000)

with tab2:
   st.header("Data")
   st.download_button(label = "Download Data as csv",data = Data.to_csv(), file_name = "Data.csv")
   st.dataframe(Data,height = 10000)

with tab3:
   st.header("Code List")
   st.download_button(label = "Download Code List as csv",data = Code.to_csv(), file_name = "Code_List.csv")
   st.dataframe(Code,height = 10000)
