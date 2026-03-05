import streamlit as st

st.set_page_config(page_title="Meal Prep Optimizer", page_icon="🍽️", layout="wide")

# Dark / Light toggle
dark_mode = st.sidebar.toggle("🌙 Dark Mode")

if dark_mode:
    bg = "#0E1117"
    text = "#FFFFFF"
else:
    bg = "#F7F9FC"
    text = "#000000"

st.markdown(f"""
<style>
.main {{
background-color: {bg};
color: {text};
}}
</style>
""", unsafe_allow_html=True)

st.title("🍽️ Meal Prep Optimizer")

st.markdown("""
### Plan your meals smarter

Generate personalized meal plans based on diet preferences,
calorie goals and lifestyle.
""")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🥗 Smart Meal Plans")
    st.write("Generate diet-based meal plans instantly.")

with col2:
    st.subheader("🛒 Grocery Lists")
    st.write("Automatically create grocery lists.")

with col3:
    st.subheader("⏱ Save Time")
    st.write("Reduce cooking stress with planning.")

st.divider()

if st.button("Start Meal Planning ➜"):
    st.switch_page("pages/meal_planner.py")