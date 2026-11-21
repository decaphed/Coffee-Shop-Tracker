import streamlit as st
import pandas as pd
from datetime import datetime
from utils.helpers import SALES_CSV, initialize_state

initialize_state()

# show the page title
st.title("Point of Sale")

# show the available drinks
st.subheader("Available Drinks")

# show the menu as a table
st.dataframe(st.session_state.menu)

st.session_state.sales = pd.read_csv(SALES_CSV)

if not st.session_state.menu.empty:
    # let the user choose a drink
    drink_index = st.selectbox(
        "Desired Drink",
        range(len(st.session_state.menu)),
        format_func=lambda index: (
            f"{st.session_state.menu.iloc[index]['Name']} "
            f"({st.session_state.menu.iloc[index]['Size']})"
        )
    )
    drink = st.session_state.menu.iloc[drink_index]
    desired_drink = drink["Name"]

    # set how many drinks to add
    quantity = st.number_input("Quantity", step=1, min_value=0)
    total = quantity * drink["Price"]

    # show the item total
    st.write(f"Total bill is: {round(total, 2)}")

    # add the drink when the button is clicked
    if st.button("Add to Order"):
        if quantity > 0:
            st.session_state.current_order.append({
                "Name": desired_drink,
                "Size": drink["Size"],
                "Quantity": quantity,
                "Price": drink["Price"],
                "Total": round(total, 2)
            })
else:
    # show a message when the menu is empty
    st.write("There are no items on the menu.")

# show the items in the order
st.subheader("Current Order")

for i, item in enumerate(st.session_state.current_order):
    # place the item and remove button in separate columns
    col1, col2 = st.columns([4, 1])
    col1.write(f"{item['Name']} x {item['Quantity']}")

    if col2.button("Remove", key=f"remove_{i}"):
        st.session_state.current_order.pop(i)
        # refresh the page after removing the item
        st.rerun()

# save payment only when the order has items
if st.button("Confirm Payment") and st.session_state.current_order:
    now = datetime.now()
    transaction_id = now.strftime("%Y%m%d%H%M%S%f")
    transaction_date = now.strftime("%Y-%m-%d %H:%M:%S")

    sale_rows = []
    for item in st.session_state.current_order:
        sale_rows.append({
            "Transaction Id": transaction_id,
            "Date": transaction_date,
            "Name": item["Name"],
            "Size": item["Size"],
            "Quantity": item["Quantity"],
            "Total": item["Total"]
        })

    log = pd.DataFrame(sale_rows)
    new_sales = pd.concat([st.session_state.sales, log], ignore_index=True)
    new_sales.to_csv(SALES_CSV, index=False)
    st.session_state.sales = new_sales
    st.session_state.receipt = {
        "Transaction Id": transaction_id,
        "Date": transaction_date,
        "Items": [item.copy() for item in st.session_state.current_order],
        "Total": round(sum(item["Total"] for item in st.session_state.current_order), 2)
    }
    st.session_state.current_order = []

if "receipt" in st.session_state:
    # show the receipt after payment
    st.subheader("Receipt")
    st.write(f"Transaction: {st.session_state.receipt['Transaction Id']}")
    st.write(f"Date: {st.session_state.receipt['Date']}")
    # show the receipt items
    st.dataframe(pd.DataFrame(st.session_state.receipt["Items"]))
    # show the amount paid
    st.write(f"Total paid: {st.session_state.receipt['Total']}")
