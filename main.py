import streamlit as st
import pandas as pd

def load_data(dataset_name):
    if dataset_name == "Synthetic":
        return pd.read_csv("synthetic.csv")
    elif dataset_name == "Organic":
        return pd.read_csv("organic.csv") 

st.title("Data Visualization for Fast Fashion!")

dataset_option = st.selectbox(
    "Choose a dataset to view:",
    ("Synthetic", "Organic")
)

df = load_data(dataset_option)

st.line_chart(df, x="x_value", y="y_value")
st.dataframe(df)


