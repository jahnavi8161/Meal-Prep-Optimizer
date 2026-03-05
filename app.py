import streamlit as st

st.set_page_config(
    page_title="Meal Prep Optimizer",
    page_icon="🍽️",
    layout="wide"
)

st.title("🍽️ Meal Prep Optimizer")

st.write("""
Plan your weekly meals based on your diet preferences, calorie goals,
and lifestyle. This app helps you quickly generate meal ideas and
organize your grocery list.
""")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🥗 Meal Planning")
    st.write("Generate meal plans based on diet preferences.")

with col2:
    st.subheader("🛒 Grocery Lists")
    st.write("Get a ready-to-use grocery list for your meals.")

with col3:
    st.subheader("⏱ Save Time")
    st.write("Reduce daily cooking stress with organized planning.")

