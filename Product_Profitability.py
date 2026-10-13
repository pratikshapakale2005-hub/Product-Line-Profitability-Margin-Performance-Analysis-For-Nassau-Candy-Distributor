import streamlit as st
import pandas as pd

# Load Dataset
df = pd.read_csv("Nassau Candy Distributor.csv")

st.title("💰 Product Profitability")

# Calculate Margin %
df["Margin %"] = (df["Gross Profit"] / df["Sales"]) * 100

# ==========================
# Profit Leaderboard
# ==========================

st.subheader("🏆 Profit Leaderboard")

profit_leaderboard = (
    df.groupby("Product Name")["Gross Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(profit_leaderboard)

# ==========================
# Margin Leaderboard
# ==========================

st.subheader("📈 Margin Leaderboard")

margin_leaderboard = (
    df.groupby("Product Name")["Margin %"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(margin_leaderboard)

# ==========================
# Product Performance Matrix
# ==========================

st.subheader("🎯 Product Performance Matrix")

product_matrix = (
    df.groupby("Product Name")
    .agg({
        "Sales": "sum",
        "Gross Profit": "sum",
        "Units": "sum"
    })
    .reset_index()
)

st.scatter_chart(
    product_matrix,
    x="Sales",
    y="Gross Profit",
    size="Units"
)

# ==========================
# Product Summary Table
# ==========================

st.subheader("📋 Product Summary")

summary = (
    df.groupby("Product Name")
    .agg({
        "Sales": "sum",
        "Gross Profit": "sum",
        "Units": "sum"
    })
    .sort_values("Gross Profit", ascending=False)
)

st.dataframe(summary)
