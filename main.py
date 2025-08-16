import streamlit as st

# Title with image
st.title("🛒 Simple Grocery Store")

# Add grocery image from internet
st.image("https://cdn.pixabay.com/photo/2016/03/05/19/02/vegetables-1238252_1280.jpg", 
         caption="Fresh Groceries", use_container_width=True)

# Add exciting music
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", autoplay=True)

# Sidebar for navigation
menu = ["Home", "Add Items", "Cart", "Checkout"]
choice = st.sidebar.selectbox("Navigation", menu)

# Grocery stock (sample)
grocery_items = {
    "Rice (1kg)": 60,
    "Wheat Flour (1kg)": 45,
    "Sugar (1kg)": 50,
    "Milk (1L)": 30,
    "Eggs (6 pcs)": 40,
    "Oil (1L)": 120
}

# Session state for cart
if "cart" not in st.session_state:
    st.session_state.cart = {}

# Home Page
if choice == "Home":
    st.subheader("Welcome to the Grocery Store App 🛍️")
    st.write("Use the sidebar to add items, view your cart, and checkout.")

# Add Items Page
elif choice == "Add Items":
    st.subheader("Add Grocery Items to Cart")
    for item, price in grocery_items.items():
        qty = st.number_input(f"{item} - ₹{price}", min_value=0, max_value=10, step=1, key=item)
        if qty > 0:
            st.session_state.cart[item] = qty

# Cart Page
elif choice == "Cart":
    st.subheader("🛒 Your Shopping Cart")
    if st.session_state.cart:
        total = 0
        for item, qty in st.session_state.cart.items():
            price = grocery_items[item]
            cost = price * qty
            total += cost
            st.write(f"{item} x {qty} = ₹{cost}")
        st.write(f"### Total = ₹{total}")
    else:
        st.info("Your cart is empty.")

# Checkout Page
elif choice == "Checkout":
    st.subheader("✅ Checkout")
    if st.session_state.cart:
        total = 0
        for item, qty in st.session_state.cart.items():
            price = grocery_items[item]
            cost = price * qty
            total += cost
        st.success(f"Thank you for shopping! Your total bill is ₹{total}.")
        if st.button("Clear Cart"):
            st.session_state.cart = {}
    else:
        st.info("No items to checkout.")
