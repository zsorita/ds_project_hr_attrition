import pandas as pd
import streamlit as st

st.set_page_config(page_title='HR Attrition')

def load_data():
  attrition_data = pd.read_csv("IBM_HR-Attrition.csv")
  return data



def load_data():
    data = pd.read_csv(
        "./data/ph_data.csv",
        encoding='ISO-8859-1'
    )
    return data
