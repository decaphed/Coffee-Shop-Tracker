import pandas as pd
import streamlit as st
from utils.helpers import MENU_CSV

# load the menu from its csv file
st.session_state.menu = pd.read_csv(MENU_CSV)
# show the page title and section heading
st.title("Ground Assembly Specialty Coffee")
st.header("Manage Your Menu")

categories = [
    "Refreshers",
    "Frappes",
    "Matcha",
    "Tea",
    "Iced Coffee",
    "Espresso",
    "Cold Brew",
    "Hot Coffee",
    "Hot Chocolate",
    "Other"
]
sizes = ["L", "M", "S"]

if not st.session_state.menu.empty:
    menu = st.session_state.menu
    # let the user choose a menu item
    item_index = st.selectbox(
        "Menu item",
        range(len(menu)),
        format_func=lambda index: (
            f"{menu.iloc[index]['Name']} ({menu.iloc[index]['Size']})"
        )
    )
    item = menu.iloc[item_index]
    item_category = item["Category"]
    if item_category not in categories:
        categories.append(item_category)

    if item["Size"] not in sizes:
        sizes.append(item["Size"])

    # group the edit fields until the user saves
    with st.form("edit_menu_item"):
        # let the user change the item details
        name = st.text_input("Name", value=str(item["Name"]))
        size = st.selectbox("Size", sizes, index=sizes.index(item["Size"]))
        category = st.selectbox(
            "Category",
            categories,
            index=categories.index(item_category)
        )
        price = st.number_input(
            "Price",
            min_value=0.0,
            step=0.1,
            value=float(item["Price"])
        )
        save_item = st.form_submit_button("Save changes")

    if save_item:
        if not name.strip():
            # show an error when the name is empty
            st.error("Enter a name for the item.")
        else:
            st.session_state.menu.loc[item_index] = [
                name.strip(),
                size,
                price,
                category
            ]
            st.session_state.menu.to_csv(MENU_CSV, index=False)
            # confirm the change and refresh the page
            st.success("Menu item updated.")
            st.rerun()

    # remove the selected item when clicked
    if st.button("Delete item"):
        st.session_state.menu = menu.drop(menu.index[item_index]).reset_index(drop=True)
        st.session_state.menu.to_csv(MENU_CSV, index=False)
        # confirm the deletion and refresh the page
        st.success("Menu item deleted.")
        st.rerun()
else:
    # explain why there are no edit controls
    st.write("There are no items to edit.")

# show the form for adding a menu item
st.subheader("Add a Menu Item")
with st.form("add_menu_item"):
    # collect details for the new item
    new_name = st.text_input("New item name")
    new_size = st.selectbox("New item size", sizes)
    new_category = st.selectbox("New item category", categories)
    new_price = st.number_input("New item price", min_value=0.0, step=0.1)
    add_item = st.form_submit_button("Add to Menu")

if add_item:
    if not new_name.strip():
        # show an error when the name is empty
        st.error("Enter a name for the item.")
    else:
        new_row = pd.DataFrame([{
            "Name": new_name.strip(),
            "Size": new_size,
            "Price": new_price,
            "Category": new_category
        }])
        st.session_state.menu = pd.concat(
            [st.session_state.menu, new_row],
            ignore_index=True
        )
        st.session_state.menu.to_csv(MENU_CSV, index=False)
        # confirm the addition and refresh the page
        st.success("Menu item added.")
        st.rerun()
