import streamlit as st
import pandas as pd

st.title("Data Visualization for Fast Fashion!")

df_syn = pd.read_csv("synthetic.csv")
df_org = pd.read_csv("organic.csv")

st.subheader("Combined Dataset Comparison")

df_combined = pd.merge(
    df_syn[['x_value', 'y_value']], 
    df_org[['x_value', 'y_value']], 
    on='x_value', 
    suffixes=('_synthetic', '_organic')
)

st.line_chart(df_combined, x='x_value', y=['y_value_synthetic', 'y_value_organic'])

col1, col2 = st.columns(2)

def show_data(name, df):
    with (col1 if name == "Synthetic" else col2):
        st.subheader(f"{name} Dataset")
        st.line_chart(df, x='x_value', y='y_value')
        st.dataframe(df)

show_data("Synthetic", df_syn)
show_data("Organic", df_org)
