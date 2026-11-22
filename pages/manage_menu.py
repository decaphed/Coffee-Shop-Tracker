import pandas as pd
import streamlit as st
from utils.helpers import MENU_CSV, initialize_state

initialize_state()

st.header("Manage Your Menu")

# Upload and replace the menu CSV
st.subheader("Upload a new menu")
uploaded_menu = st.file_uploader(
    "Choose a CSV file",
    type=["csv"],
)

if uploaded_menu is not None:
    try:
        uploaded_menu_df = pd.read_csv(uploaded_menu)
        required_columns = ["Name", "Size", "Price", "Category"]

        if not all(column in uploaded_menu_df.columns for column in required_columns):
            st.error("CSV must contain: Name, Size, Price, Category")
        else:
            uploaded_menu_df = uploaded_menu_df[required_columns]
            st.write("CSV preview")
            st.dataframe(uploaded_menu_df, hide_index=True)

            if st.button("Replace menu with uploaded CSV", type="secondary"):
                uploaded_menu_df.to_csv(MENU_CSV, index=False)
                st.session_state.menu = uploaded_menu_df
                st.session_state.pop("menu_editor", None)
                st.success("Menu replaced with the uploaded CSV.")
    except (pd.errors.EmptyDataError, pd.errors.ParserError):
        st.error("Please upload a valid CSV file.")

# edit items and add or delete rows
edited_menu = st.data_editor(
    st.session_state.menu,
    num_rows="dynamic",
    hide_index=True,
    key="menu_editor",
)

# save menu changes
if st.button("Save menu", type="primary"):
    if edited_menu.isna().any().any():
        st.error("Fill in every field before saving.")
    elif edited_menu["Name"].astype(str).str.strip().eq("").any():
        st.error("Item names cannot be empty.")
    else:
        try:
            edited_menu.to_csv(MENU_CSV, index=False)
            st.session_state.menu = edited_menu
            st.write("Menu saved.")
            st.rerun()
        except OSError as error:
            st.error(f"Could not save the menu CSV: {error}")



