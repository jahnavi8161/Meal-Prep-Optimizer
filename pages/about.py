import streamlit as st

st.title("ℹ About This App")

st.write("""
Meal Prep Optimizer is a simple web application that helps users
generate meal plans based on dietary preferences and calorie goals.

Built with:

• Python  
• Streamlit  
""")

if st.button("⬅ Back Home"):
    st.switch_page("app.py")