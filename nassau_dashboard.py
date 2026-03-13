import streamlit as st
import pandas as pd
import plotly.express as px

# ------------------------------------------------
# PAGE SETTINGS
# ------------------------------------------------

st.set_page_config(
    page_title="Nassau Candy Analytics Dashboard",
    layout="wide"
)

# ------------------------------------------------
# STYLE (UNCHANGED)
# ------------------------------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right,#0f2027,#203a43,#2c5364);
}

h1 {
    color:#FFD700;
    text-align:center;
}

h2, h3 {
    color:#00FFFF;
}

p, span, label, div {
    color:white !important;
}

section[data-testid="stSidebar"] * {
    color:black !important;
}

[data-testid="stMetric"] {
    background-color:#1c3b57;
    padding:15px;
    border-radius:12px;
    text-align:center;
}

[data-testid="stMetricLabel"] {
    color:white !important;
}

[data-testid="stMetricValue"] {
    color:#FFD700 !important;
    font-size:26px;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------------
# LOAD DATA
# ------------------------------------------------

df = pd.read_csv("Nassau Candy Distributor.csv")

df["Gross Margin %"] = (df["Gross Profit"] / df["Sales"]) * 100
df["Profit per Unit"] = df["Gross Profit"] / df["Units"]

df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True, errors="coerce")

# ------------------------------------------------
# SIDEBAR FILTERS
# ------------------------------------------------

st.sidebar.title("Dashboard Filters")

division_filter = st.sidebar.multiselect(
    "Select Division",
    df["Division"].unique(),
    default=df["Division"].unique()
)

region_filter = st.sidebar.multiselect(
    "Select Region",
    df["Region"].unique(),
    default=df["Region"].unique()
)

df = df[
    (df["Division"].isin(division_filter)) &
    (df["Region"].isin(region_filter))
]

# ------------------------------------------------
# TITLE
# ------------------------------------------------

st.title("🍬 Nassau Candy Distributor Profitability Dashboard")

# ------------------------------------------------
# KPI METRICS
# ------------------------------------------------

col1,col2,col3,col4 = st.columns(4)

col1.metric("Total Sales",f"₹{df['Sales'].sum():,.0f}")
col2.metric("Total Profit",f"₹{df['Gross Profit'].sum():,.0f}")
col3.metric("Average Margin",f"{df['Gross Margin %'].mean():.2f}%")
col4.metric("Total Units Sold",f"{df['Units'].sum():,.0f}")

st.markdown("---")

# =================================================
# ROW 1
# =================================================

col1,col2 = st.columns(2)

with col1:

    st.subheader("Division Profitability")

    division_summary = df.groupby("Division").agg({
        "Sales":"sum",
        "Gross Profit":"sum"
    }).reset_index()

    division_summary["Gross Margin %"] = (
        division_summary["Gross Profit"] /
        division_summary["Sales"]
    )*100

    fig = px.bar(
        division_summary,
        x="Division",
        y="Gross Margin %",
        color="Division",
        text_auto=True,
        title="Division Margin Analysis"
    )

    st.plotly_chart(fig,use_container_width=True)

with col2:

    st.subheader("Regional Profitability")

    region_summary = df.groupby("Region")["Gross Profit"].sum().reset_index()

    fig = px.bar(
        region_summary,
        x="Region",
        y="Gross Profit",
        color="Region",
        text_auto=True,
        title="Profit by Region"
    )

    st.plotly_chart(fig,use_container_width=True)

st.markdown("---")

# =================================================
# ROW 2
# =================================================

col3,col4 = st.columns(2)

with col3:

    st.subheader("Monthly Profit Trend")

    monthly_profit = df.groupby(
        df["Order Date"].dt.to_period("M")
    )["Gross Profit"].sum().reset_index()

    monthly_profit["Order Date"] = monthly_profit["Order Date"].astype(str)

    fig = px.line(
        monthly_profit,
        x="Order Date",
        y="Gross Profit",
        markers=True,
        title="Monthly Profit Trend"
    )

    st.plotly_chart(fig,use_container_width=True)

with col4:

    st.subheader("Profit Contribution by Division")

    profit_share = df.groupby("Division")["Gross Profit"].sum().reset_index()

    fig = px.pie(
        profit_share,
        names="Division",
        values="Gross Profit",
        hole=0.4,
        title="Division Profit Share"
    )

    st.plotly_chart(fig,use_container_width=True)

st.markdown("---")

# =================================================
# ROW 3
# =================================================

col5,col6 = st.columns(2)

with col5:

    st.subheader("Top 10 Profitable Products")

    product_summary = df.groupby("Product Name").agg({
        "Sales":"sum",
        "Gross Profit":"sum"
    }).reset_index()

    top_products = product_summary.sort_values(
        by="Gross Profit",
        ascending=False
    ).head(10)

    st.dataframe(top_products,use_container_width=True)

with col6:

    st.subheader("Cost vs Margin Analysis")

    fig = px.scatter(
        df,
        x="Cost",
        y="Gross Margin %",
        color="Division",
        size="Units",
        hover_data=["Product Name","Sales"],
        title="Cost vs Margin Diagnostics"
    )

    st.plotly_chart(fig,use_container_width=True)

st.markdown("---")

# =================================================
# ROW 4
# =================================================

st.subheader("Pareto Profit Analysis")

product_summary = product_summary.sort_values(
    by="Gross Profit",
    ascending=False
)

product_summary["Cumulative Profit %"] = (
    product_summary["Gross Profit"].cumsum() /
    product_summary["Gross Profit"].sum()
)*100

fig = px.line(
    product_summary,
    y="Cumulative Profit %",
    markers=True,
    title="Pareto 80/20 Profit Analysis"
)

fig.add_hline(y=80,line_dash="dash",line_color="red")

st.plotly_chart(fig,use_container_width=True)