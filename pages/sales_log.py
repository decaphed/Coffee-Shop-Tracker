
import streamlit as st
import pandas as pd
from datetime import datetime
from utils.helpers import SALES_CSV

st.title("Sales Log")

sales = pd.read_csv(SALES_CSV, dtype={"Transaction Id": str})

# summarize all-time quantities by item
all_time_sales = (
    sales.groupby("Name", as_index=False)["Quantity"]
    .sum()
    .sort_values("Quantity", ascending=False)
)

st.subheader("All-Time Sales by Item")
if all_time_sales.empty:
    st.write("No sales have been recorded.")
else:
    st.bar_chart(all_time_sales, x="Name", y="Quantity")

st.dataframe(sales)