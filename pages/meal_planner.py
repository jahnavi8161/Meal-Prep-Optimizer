import streamlit as st

st.title("Meal Planner")

diet = st.selectbox(
    "Select your diet type",
    ["Vegetarian", "Non-Vegetarian", "Vegan"]
)

calories = st.number_input(
    "Daily calorie goal",
    min_value=1200,
    max_value=4000,
    value=2000
)

if st.button("Generate Meal Plan"):

    st.success("Meal plan generated!")

    if diet == "Vegetarian":
        st.write("Breakfast: Oatmeal with fruits")
        st.write("Lunch: Vegetable rice bowl")
        st.write("Dinner: Paneer salad")

    elif diet == "Non-Vegetarian":
        st.write("Breakfast: Egg omelette")
        st.write("Lunch: Chicken rice bowl")
        st.write("Dinner: Grilled fish")

    else:
        st.write("Breakfast: Fruit smoothie")
        st.write("Lunch: Quinoa salad")
        st.write("Dinner: Tofu stir fry")