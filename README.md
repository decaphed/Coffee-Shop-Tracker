# Coffee Shop Tracker

A simple Streamlit app for managing a coffee shop menu and tracking sales.

## Features

- Add, edit, and delete menu items.
- Upload a CSV file to replace the saved menu.
- Record orders and show a receipt after payment.
- View the sales log and daily sales summary.
- Download today's sales as a CSV file.

## Run the app

From the project folder, install the packages and start the app:

```bash
pip install streamlit pandas
streamlit run app.py
```

Menu items and sales are saved in `data/menu.csv` and `data/sales.csv`.
