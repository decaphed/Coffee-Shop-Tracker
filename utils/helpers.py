
from pathlib import Path

import streamlit as st
import pandas as pd

MENU_CSV = Path("data/menu.csv")
SALES_CSV = Path("data/sales.csv")


# keep app data between page changes
def initialize_state():

    # load menu data once per session
    if "menu" not in st.session_state:
        # start with an empty menu table
        st.session_state.menu = pd.DataFrame(
            columns=["Name", "Size", "Price", "Category"]
        )

        if MENU_CSV.exists():
            try:
                # read saved menu items
                st.session_state.menu = pd.read_csv(MENU_CSV)
            except pd.errors.EmptyDataError:
                # keep the empty table when the file has no rows
                pass
        else:
            # create the data folder and menu file
            MENU_CSV.parent.mkdir(parents=True, exist_ok=True)
            st.session_state.menu.to_csv(MENU_CSV, index=False)

    # load sales data once per session
    if "sales" not in st.session_state:
        # start with an empty sales table
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
                # read saved sales rows
                st.session_state.sales = pd.read_csv(SALES_CSV)
            except pd.errors.EmptyDataError:
                # keep the empty table when the file has no rows
                pass
        else:
            # create the data folder and sales file
            SALES_CSV.parent.mkdir(parents=True, exist_ok=True)
            st.session_state.sales.to_csv(SALES_CSV, index=False)

    # start with an empty order
    if "current_order" not in st.session_state:
        st.session_state.current_order = []
