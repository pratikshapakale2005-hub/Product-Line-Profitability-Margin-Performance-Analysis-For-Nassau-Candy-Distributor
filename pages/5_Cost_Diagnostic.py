import streamlit as st
import pandas as pd

df = pd.read_csv("Nassau Candy Distributor.csv")

st.title("💵 Cost Diagnostics")

# Cost vs Sales

st.subheader("Cost vs Sales")

cost_sales = (
    df.groupby("Product Name")
    .agg({
        "Sales":"sum",
        "Cost":"sum"
    })
)

st.line_chart(cost_sales)

# Margin Risk

st.subheader("Margin Risk Analysis")

df["Margin %"] = (
    df["Gross Profit"]/df["Sales"]
)*100

risk_products = (
    df.groupby("Product Name")["Margin %"]
    .mean()
    .sort_values()
    .head(10)
)

st.bar_chart(risk_products)

# Cost Summary

st.subheader("Top Cost Products")

cost_summary = (
    df.groupby("Product Name")["Cost"]
    .sum()
    .sort_values(ascending=False)
    .head(20)
)

st.dataframe(cost_summary)
