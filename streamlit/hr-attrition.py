import streamlit as st
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
import pickle

st.set_page_config(page_title='HR Attrition')

def load_data():
  attrition_data = pd.read_csv("IBM_HR-Attrition.csv")
  return data
  

