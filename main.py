import streamlit as st
import pandas as pd

st.set_page_config(page_title="Fast Fashion Fiber Degradation", layout="wide")

st.title("Data Visualization for Fast Fashion")
st.write(
    "This dashboard compares how much different textile fibers biodegraded after "
    "181 days under aerobic industrial composting conditions."
)

# Here is the data from Table 2 in the paper
df = pd.DataFrame({
    "Fiber": [
        "Viscose rayon",
        "Machine-washable wool",
        "Untreated wool",
        "Polyester",
        "Polyamide (nylon)",
        "Polypropylene"
    ],
    "Fiber category": [
        "Natural/regenerated",
        "Natural/regenerated",
        "Natural/regenerated",
        "Synthetic",
        "Synthetic",
        "Synthetic"
    ],
    "Biodegradation after 181 days (%)": [
        83.2,
        67.6,
        48.4,
        -0.6,
        2.1,
        1.5
    ],
    "95% confidence interval": [
        3.0,
        6.5,
        2.0,
        1.5,
        2.8,
        1.0
    ]
})

st.subheader("Graph 1: Biodegradation by Fiber Type")

st.write(
    "This graph shows the measured biodegradation percentage for each fiber after 181 days. "
    "Higher values mean more of the material biodegraded."
)

st.bar_chart(
    df,
    x="Fiber",
    y="Biodegradation after 181 days (%)"
)

st.dataframe(df, use_container_width=True)

# This is the second graph with the average results for the two fiber categories
category_df = (
    df.groupby("Fiber category", as_index=False)["Biodegradation after 181 days (%)"]
    .mean()
)

st.subheader("Graph 2: Average Biodegradation by Fiber Category")

st.write(
    "This graph compares the average biodegradation of natural/regenerated fibers "
    "against synthetic fibers."
)

st.bar_chart(
    category_df,
    x="Fiber category",
    y="Biodegradation after 181 days (%)"
)

st.dataframe(category_df, use_container_width=True)

st.subheader("Conclusion")

natural_avg = category_df.loc[
    category_df["Fiber category"] == "Natural/regenerated",
    "Biodegradation after 181 days (%)"
].values[0]

synthetic_avg = category_df.loc[
    category_df["Fiber category"] == "Synthetic",
    "Biodegradation after 181 days (%)"
].values[0]

st.write(
    f"Natural/regenerated fibers had an average biodegradation of about "
    f"{natural_avg:.1f}% after 181 days, while synthetic fibers had an average "
    f"biodegradation of about {synthetic_avg:.1f}%."
)

st.write(
    "This supports the conclusion that natural and regenerated fibers biodegrade "
    "much more than synthetic fibers under these composting conditions."
)

st.subheader("Data Source")


st.write("https://www.wool.com/globalassets/wool/attachments/biodegradation-behavior-of-wool-and-other-textile-fibers-in-aerobic-composting-conditions.pdf")

