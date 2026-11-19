import streamlit as st
import pandas as pd
from datetime import datetime
from utils.helpers import SALES_CSV

st.title("Sales Log")

sales = pd.read_csv(SALES_CSV)
st.dataframe(sales)