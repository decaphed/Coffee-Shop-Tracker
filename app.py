import streamlit as st
from utils.helpers import initialize_state

st.set_page_config(
    page_title="Coffee Shop Tracker",
    layout="wide"
)

initialize_state()

st.title("Coffee Shop Tracker")

st.write("Welcome to the Coffee Shop Management System!")
st.write("Select a page from the sidebar to get started.")