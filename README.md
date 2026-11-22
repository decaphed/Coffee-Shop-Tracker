# Coffee Shop Tracker

Coffee Shop Tracker is a Streamlit-based point-of-sale and management application for a specialty coffee shop. It gives staff a simple interface for maintaining the menu, building orders, recording payments, reviewing sales, and monitoring today's performance.

## Live App

[Open the Coffee Shop Tracker](https://coffee-shop-tracker-hasan-b53pytn9iwbcorjnwrhy7c.streamlit.app/)

## Video Demonstration

[Watch the project demonstration](https://drive.google.com/file/d/1r9X7Urwq9XHVbLdY0hYKUCfbnhCddcJ2/view?usp=sharing)

## Project Features

### Menu Management
- View all available menu items.
- Add, edit, and delete drinks using an editable table.
- Upload a CSV file to replace the complete menu.
- Save menu changes to persistent CSV storage.

### Point of Sale
- Select drinks and sizes from the current menu.
- Choose a quantity and calculate the order total.
- Add and remove items before payment.
- Confirm payment and generate a transaction receipt.
- Record each paid transaction in the sales log.

### Daily Dashboard
- View today's total revenue and items sold.
- See which items were sold most often today.
- Review today's sales in a table.
- Download today's sales as a CSV file.

### Sales Log
- View all completed sales transactions.
- Review all-time sales quantity by item in a bar chart.
- Track transaction IDs, dates, products, quantities, and totals.

## Built With

- **Python**
- **Streamlit** for the web interface
- **Pandas** for data processing and CSV storage

## Getting Started

From the project directory, install the required packages:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
streamlit run app.py
```

The application will open locally in your browser.

## Data Storage

The application stores data in the `data` folder:

- `data/menu.csv` - Coffee shop menu items
- `data/sales.csv` - Completed sales transactions
