import streamlit as st
import pandas as pd
from utils.helpers import MENU_CSV

st.session_state.menu = pd.read_csv(MENU_CSV)
st.title("Ground Assembly Specialty Coffee")
st.header("Manage Your Menu")

item = st.text_input("What is The New Addition to The Menu: ")
size = st.selectbox("Size: ", ('L','M','S'))
category = st.selectbox('Category of Item: ', ("Refreshers","Frappes","Matcha","Tea","Iced Coffee"))
price = st.number_input('Planned Price: ', placeholder="How much would it be?", step=0.1)

if st.button('Add to Menu', type='primary'):
    st.write("Item Successfully addded to the menu!")

    menu = pd.DataFrame({'Name':[item],'Size':[size],"Category":[category],"Price":[price]})

    og_menu = st.session_state.menu

    new_menu = pd.concat([og_menu, menu], ignore_index=True) # appends inserted values to the csv file
    new_menu.to_csv(MENU_CSV, index=False)
st.session_state.menu