import streamlit as st
import pandas as pd

df = pd.read_csv("Nassau Candy Distributor.csv")

st.title("🏢 Division Performance")

# Revenue by Division
st.subheader("Revenue by Division")

revenue_division = (
    df.groupby("Division")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(revenue_division)

# Profit by Division
st.subheader("Profit by Division")

profit_division = (
    df.groupby("Division")["Gross Profit"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(profit_division)

# Margin Comparison
st.subheader("Margin Comparison")

df["Margin %"] = (
    df["Gross Profit"] / df["Sales"]
) * 100

margin_division = (
    df.groupby("Division")["Margin %"]
    .mean()
    .sort_values(ascending=False)
)

st.bar_chart(margin_division)
