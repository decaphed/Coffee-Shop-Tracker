import streamlit as st
import pandas as pd
from datetime import datetime
from utils.helpers import SALES_CSV

st.title("Point of Sale")

st.subheader("Available Drinks")

st.dataframe(st.session_state.menu)

st.session_state.sales = pd.read_csv(SALES_CSV)

desired_drink = st.selectbox("Desired Drink: ", st.session_state.menu['Name']) # creates a dropdown menu of the available drinks in the menu

drink = st.session_state.menu[st.session_state.menu['Name'] == desired_drink] # retrieves drink information

quantity = st.number_input("Quantity", step=1, min_value=0) # user will decide how many of the items they want 

total = quantity * drink['Price'].iloc[0] # will only take the price of the selected drink and multiplies it with the quantity

st.write(f'Total bill is: {round(total,2)}')

if st.button('Confirm Payment'):
    transaction_id = datetime.now().strftime("%Y%m%d%H%M%S")

    transaction_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log = pd.DataFrame({
        "Transaction Id":[transaction_id],
        "Date":[transaction_date],
        "Name":[desired_drink],
        "Size":[drink['Size'].iloc[0]],
        "Quantity":[quantity],
        "Total":[total]
    })
    
    og_log = st.session_state.sales

    new_sales = pd.concat([og_log, log], ignore_index=True) # appends inserted values to the csv file
    new_sales.to_csv(SALES_CSV, index=False)
