# Nassau Candy Distributor Profitability Dashboard

## Project Overview
This project performs a **Product Line Profitability and Margin Performance Analysis** for Nassau Candy Distributor. The goal is to identify high-performing products, profitable divisions, and margin risks using data analytics and an interactive Streamlit dashboard.

The analysis transforms raw order data into meaningful business insights to support strategic decision-making.

---

## Business Problem
High sales volume does not always mean high profitability. Some products may sell frequently but produce low margins due to high manufacturing or operational costs.

Organizations need to identify:

- Which products generate the highest profit
- Which divisions perform efficiently
- Where pricing or cost optimization is required

This project addresses these challenges using exploratory data analysis and visualization.

---

## Dataset Description

The dataset includes order-level transactional data with the following key fields:

- Sales
- Units
- Cost
- Gross Profit
- Product Name
- Division
- Region
- Order Date

---

## Key Metrics

The following metrics were calculated during analysis:

**Gross Margin (%)**
Gross Margin = Gross Profit / Sales × 100


**Profit per Unit**


Profit per Unit = Gross Profit / Units


These metrics help evaluate profitability efficiency.

---

## Exploratory Data Analysis

The analysis includes:

- Division profitability analysis
- Regional profit analysis
- Monthly profit trends
- Cost vs margin relationship
- Top performing products
- Pareto (80/20) profit analysis

---

## Dashboard Features

The interactive Streamlit dashboard provides:

- KPI metrics (Total Sales, Profit, Margin, Units Sold)
- Division profitability charts
- Regional profit distribution
- Monthly profit trend visualization
- Profit contribution by division
- Cost vs margin diagnostics
- Pareto profit concentration analysis

The dashboard allows users to explore insights interactively.

---

## Technologies Used

- Python
- Pandas
- Plotly
- Streamlit
- Matplotlib
- Seaborn
- scikit-learn

---

## Requirements

Install the required libraries using:


pip install -r requirements.txt


---
## Machine Learning Implementation

A Linear Regression model was implemented to predict product profitability based on business variables such as sales, cost, units sold, division, and region.

The model was trained using scikit-learn and evaluated using performance metrics including Mean Absolute Error and R² Score. This demonstrates how machine learning can support profit forecasting and pricing optimization.

---

## Run the Dashboard

To start the dashboard, run:


streamlit run nassau_dashboard.py


---

## Project Structure


Nassau_Candy_Project
│
├── Nassau Candy Distributor.csv
├── analysis.ipynb
├── nassau_dashboard.py
├── requirements.txt
├── README.md
└── Research_Paper.pdf


---

## Conclusion

This project demonstrates how data analytics and visualization can help organizations better understand profitability patterns and improve business decision-making.
