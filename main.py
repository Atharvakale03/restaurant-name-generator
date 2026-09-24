import streamlit as st
import random

st.set_page_config(
    page_title="Restaurant Name Generator",
    page_icon="🍽️",
    layout="centered"
)

restaurant_words = {
    "Indian": {
        "prefix": ["Spice", "Royal", "Tandoori", "Masala", "Curry", "Saffron"],
        "suffix": ["House", "Kitchen", "Palace", "Bistro", "Flavours", "Corner"]
    },
    "Italian": {
        "prefix": ["Bella", "La", "Roma", "Pasta", "Casa", "Viva"],
        "suffix": ["Kitchen", "Oven", "Bistro", "Trattoria", "Table", "Cucina"]
    },
    "American": {
        "prefix": ["Urban", "Classic", "Downtown", "Big", "Grill", "Golden"],
        "suffix": ["Diner", "Grill", "Kitchen", "House", "Cafe", "Bistro"]
    },
    "Mexican": {
        "prefix": ["Fiesta", "Casa", "El", "Taco", "Amigo", "Sol"],
        "suffix": ["Cantina", "Kitchen", "Grill", "House", "Cafe", "Bistro"]
    },
    "Chinese": {
        "prefix": ["Dragon", "Golden", "Jade", "Lucky", "Imperial", "Red"],
        "suffix": ["Wok", "Garden", "Kitchen", "House", "Palace", "Bistro"]
    }
}

signature_dishes = {
    "Indian": ["Butter Chicken", "Paneer Tikka", "Biryani", "Masala Dosa", "Dal Makhani"],
    "Italian": ["Margherita Pizza", "Pasta Alfredo", "Lasagna", "Risotto", "Bruschetta"],
    "American": ["Classic Cheeseburger", "BBQ Ribs", "Loaded Fries", "Grilled Steak", "Chicken Wings"],
    "Mexican": ["Tacos", "Burritos", "Nachos", "Quesadillas", "Enchiladas"],
    "Chinese": ["Hakka Noodles", "Manchurian", "Fried Rice", "Dim Sum", "Kung Pao Chicken"]
}

taglines = [
    "Where every bite tells a story.",
    "Good food. Great memories.",
    "Taste the difference.",
    "Made with passion, served with love.",
    "Your table, your experience.",
    "A place for food lovers.",
    "Fresh flavors, unforgettable moments."
]


def generate_restaurant_name(cuisine):
    data = restaurant_words[cuisine]
    prefix = random.choice(data["prefix"])
    suffix = random.choice(data["suffix"])
    return f"{prefix} {suffix}"


def generate_rating():
    return round(random.uniform(4.1, 5.0), 1)


def generate_price(price_range):
    prices = {
        "Budget": "₹200 - ₹500",
        "Moderate": "₹500 - ₹1,000",
        "Premium": "₹1,000 - ₹2,000",
        "Luxury": "₹2,000+"
    }

    return prices[price_range]


st.title("🍽️ Restaurant Name Generator")

st.write(
    "Create a unique restaurant concept based on your "
    "cuisine, location, ambience and dining preferences."
)

st.divider()

st.sidebar.header("⚙️ Restaurant Preferences")

cuisine = st.sidebar.selectbox(
    "🍴 Pick a cuisine",
    ["Indian", "Italian", "American", "Mexican", "Chinese"]
)

restaurant_type = st.sidebar.selectbox(
    "🏪 Restaurant Type",
    [
        "Fine Dining",
        "Casual Dining",
        "Cafe",
        "Food Truck",
        "Family Restaurant",
        "Fast Food"
    ]
)

location = st.sidebar.text_input(
    "📍 City / Location",
    placeholder="e.g. Pune"
)

food_preference = st.sidebar.selectbox(
    "🥗 Food Preference",
    ["Vegetarian", "Non-Vegetarian", "Both"]
)

ambience = st.sidebar.selectbox(
    "✨ Ambience",
    ["Modern", "Traditional", "Luxury", "Cozy", "Rustic", "Casual"]
)

price_range = st.sidebar.selectbox(
    "💰 Price Range",
    ["Budget", "Moderate", "Premium", "Luxury"]
)

st.subheader("🎨 Create Your Restaurant")

generate = st.button(
    "✨ Generate Restaurant",
    use_container_width=True
)

if generate:

    restaurant_name = generate_restaurant_name(cuisine)
    dish = random.choice(signature_dishes[cuisine])
    tagline = random.choice(taglines)
    rating = generate_rating()
    price = generate_price(price_range)

    st.success("Your restaurant has been generated! 🎉")

    st.markdown(f"## 🍽️ {restaurant_name}")
    st.markdown(f'**"{tagline}"**')

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.info(f"### 🍴 Cuisine\n{cuisine}")
        st.info(f"### 🏪 Type\n{restaurant_type}")
        st.info(
            f"### 📍 Location\n"
            f"{location if location else 'Not specified'}"
        )

    with col2:
        st.info(f"### ✨ Ambience\n{ambience}")
        st.info(f"### 🥗 Food\n{food_preference}")
        st.info(f"### 💰 Price\n{price}")

    st.divider()

    st.subheader("⭐ Signature Dish")
    st.success(f"Try our famous **{dish}**!")

    st.subheader("⭐ Customer Rating")
    st.write(f"⭐⭐⭐⭐⭐ **{rating}/5.0**")
    st.progress(rating / 5)

    st.subheader("💡 Restaurant Concept")

    st.write(
        f"""
        **{restaurant_name}** is a {ambience.lower()}
        {restaurant_type.lower()} specializing in
        {cuisine.lower()} cuisine.

        The restaurant focuses on providing a memorable
        dining experience for customers looking for
        {food_preference.lower()} food.
        """
    )

else:
    st.info(
        "👈 Select your preferences from the sidebar "
        "and click **Generate Restaurant**."
    )

st.divider()

st.caption(
    "🍽️ Restaurant Name Generator | Built with Python & Streamlit"
)
