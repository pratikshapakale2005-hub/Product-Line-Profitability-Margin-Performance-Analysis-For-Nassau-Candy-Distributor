import streamlit as st
import pandas as pd

df = pd.read_csv("Nassau Candy Distributor.csv")

st.title("🌍 Region Analytics")

# Region Revenue

st.subheader("Revenue by Region")

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(region_sales)

# Region Profit

st.subheader("Profit by Region")

region_profit = (
    df.groupby("Region")["Gross Profit"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(region_profit)

# Region Contribution

st.subheader("Regional Contribution")

contribution = (
    df.groupby("Region")["Sales"]
    .sum()
)

st.dataframe(contribution)
