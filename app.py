import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Sales Dashboard",
    layout="wide"
)

st.title("Sales & Profitability Dashboard")

df = pd.read_csv("Nassau Candy Distributor.csv")

st.write(df.head())

import streamlit as st

st.sidebar.header("Filters")

division = st.sidebar.multiselect(
    "Division",
    ["Consumer", "Industrial", "Healthcare"]
)

factory = st.sidebar.multiselect(
    "Factory",
    ["Factory A", "Factory B", "Factory C"]
)

margin = st.sidebar.slider(
    "Margin %",
    0,
    100,
    (10, 50)
)

product = st.sidebar.text_input(
    "Search Product"
)

st.set_page_config(
    page_title="Sales & Profitability Dashboard",
    page_icon="📊",
    layout="wide"
)