import pandas as pd
import streamlit as st
from utils.helpers import MENU_CSV


st.title("Ground Assembly Specialty Coffee")
st.header("Manage Your Menu")

# edit items and add or delete rows
edited_menu = st.data_editor(
    st.session_state.menu,
    num_rows="dynamic",
    hide_index=True
)

# save menu changes
if st.button("Save menu", type="primary"):
    if edited_menu.isna().any().any():
        st.error("Fill in every field before saving.")
    elif edited_menu["Name"].astype(str).str.strip().eq("").any():
        st.error("Item names cannot be empty.")
    else:
        edited_menu.to_csv(MENU_CSV, index=False)
        st.session_state.menu = edited_menu
        st.success("Menu saved.")
        st.rerun()
