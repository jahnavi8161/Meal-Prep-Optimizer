import streamlit as st

st.title("🛒 Grocery List")

st.write("Items you may need for meal preparation:")

st.write("• Vegetables")
st.write("• Fruits")
st.write("• Protein sources")
st.write("• Grains")
st.write("• Spices")

col1, col2 = st.columns(2)

with col1:
    if st.button("⬅ Back to Meal Planner"):
        st.switch_page("pages/1_Meal_Planner.py")

with col2:
    if st.button("Next ➜ About"):
        st.switch_page("pages/about.py")