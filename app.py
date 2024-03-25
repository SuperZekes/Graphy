import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config("Coke Vs Pepsi", page_icon="🥤", layout="wide")

# Generate random data for demonstration
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["This is not true info!", "Coke", "Pepsi"])

st.line_chart(
   chart_data, x="This is not true info!", y=["Coke", "Pepsi"], color=["#FF0000", "#0000FF"]
)