import streamlit as st

st.title("🍽 Meal Planner")

diet = st.selectbox(
    "Select Diet Type",
    ["Vegetarian", "Non-Vegetarian", "Vegan"]
)

calories = st.number_input(
    "Daily Calorie Goal",
    min_value=1200,
    max_value=4000,
    value=2000
)

generate = st.button("Generate Meal Plan")

if generate:

    if diet == "Vegetarian":
        meals = [
            "🥣 Breakfast: Oatmeal with fruits",
            "🍚 Lunch: Vegetable rice bowl",
            "🥗 Dinner: Paneer salad"
        ]

    elif diet == "Non-Vegetarian":
        meals = [
            "🍳 Breakfast: Egg omelette",
            "🍗 Lunch: Chicken rice bowl",
            "🐟 Dinner: Grilled fish"
        ]

    else:
        meals = [
            "🍓 Breakfast: Fruit smoothie",
            "🥗 Lunch: Quinoa salad",
            "🍲 Dinner: Tofu stir fry"
        ]

    st.success("Meal plan generated!")

    for meal in meals:
        st.write(meal)

col1, col2 = st.columns(2)

with col1:
    if st.button("⬅ Back Home"):
        st.switch_page("app.py")

with col2:
    if st.button("Next ➜ Grocery List"):
        st.switch_page("pages/grocery_list.py")