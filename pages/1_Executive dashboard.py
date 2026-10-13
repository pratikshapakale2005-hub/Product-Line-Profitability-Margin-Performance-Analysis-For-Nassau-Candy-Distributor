import streamlit as st
import pandas as pd

# Load Data
df = pd.read_csv(r"C:\Users\lenovo\OneDrive\Desktop\code\Nassau Candy Distributor.csv")

# Convert Date Column
df["Date"] = pd.to_datetime(df["Ship Date"])

st.title("📊 Executive Overview")

# KPI Calculations
total_sales = df["Sales"].sum()
total_profit = df["Gross Profit"].sum()
total_units = df["Units"].sum()
margin = (total_profit / total_sales) * 100

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Revenue", f"₹{total_sales:,.0f}")

with col2:
    st.metric("Profit", f"₹{total_profit:,.0f}")

with col3:
    st.metric("Margin %", f"{margin:.2f}%")

with col4:
    st.metric("Units Sold", f"{total_units:,.0f}")

st.divider()

# Revenue Trend Analysis
st.subheader("📈 Revenue Trend Analysis")

sales_trend = (
    df.groupby("Date")["Sales"]
    .sum()
    .reset_index()
)

st.line_chart(
    sales_trend.set_index("Date")
)

st.divider()

# Profit Trend Analysis
st.subheader("💰 Profit Trend Analysis")

profit_trend = (
    df.groupby("Date")["Gross Profit"]
    .sum()
    .reset_index()
)

st.line_chart(
    profit_trend.set_index("Date")
)
