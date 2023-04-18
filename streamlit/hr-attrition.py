import pandas as pd
import streamlit as st

st.set_page_config(page_title='HR Attrition')

def load_data():
    data = pd.read_csv(
        "IBM_HR-Attrition.csv"
    )
    return data

def introduction():
    data = load_data()
    with st.expander("View Data"):
        st.dataframe(data)
        st.caption("*Source: IBM HR Analytics Employee Attrition & Performance*")