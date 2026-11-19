
from pathlib import Path

import streamlit as st
import pandas as pd

MENU_CSV = Path("data/menu.csv")
SALES_CSV = Path("data/sales.csv")


def initialize_state():

    if "menu" not in st.session_state:
        st.session_state.menu = pd.DataFrame(
            columns=["Name", "Size", "Price", "Category"]
        )

        if MENU_CSV.exists():
            try:
                st.session_state.menu = pd.read_csv(MENU_CSV)
            except pd.errors.EmptyDataError:
                pass

    if "sales" not in st.session_state:
        st.session_state.sales = pd.DataFrame(
            columns=[
                "Transaction Id",
                "Date",
                "Name",
                "Size",
                "Quantity",
                "Total"
            ]
        )

        if SALES_CSV.exists():
            try:
                st.session_state.sales = pd.read_csv(SALES_CSV)
            except pd.errors.EmptyDataError:
                pass

    if "current_order" not in st.session_state:
        st.session_state.current_order = []
