
import streamlit as st
import pandas as pd
from datetime import datetime
from utils.helpers import initialize_state

initialize_state()
    
st.title("Daily Dashboard")

# get sales data
sales = st.session_state.sales

# calculate todays sales
today = datetime.now().strftime("%Y-%m-%d")
sales["Date"] = pd.to_datetime(sales["Date"], format="mixed")
daily_sales = sales[sales["Date"].dt.strftime("%Y-%m-%d") == today]

# display results
st.metric("Today's Revenue", round(daily_sales["Total"].sum(),2))

st.metric("Items Sold", daily_sales["Quantity"].sum())

# display sales
st.subheader("Today's Sales")
st.dataframe(daily_sales)

# let the user download today's sales
sales_csv = daily_sales.to_csv(index=False).encode("utf-8")
st.download_button(
    "Download today's sales",
    data=sales_csv,
    file_name=f"sales_{today}.csv",
    mime="text/csv"
)
