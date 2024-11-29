import streamlit as st

# Initialize session state for cart if it doesn't exist
if 'cart' not in st.session_state:
    st.session_state.cart = []
    st.session_state.total_cost = 0

# Sample product details (barcode, name, price)
products = {
    "1": {"name": "Milk", "price": 25},
    "2": {"name": "Bread", "price": 15},
    "3": {"name": "Butter", "price": 30},
}

# Title of the app
st.title("Smart Trolley - Dummy Interface")

# Input for barcode
barcode = st.text_input("Enter Product Barcode (e.g., 1 or 2 or 3........):")

# Button to add product to cart
if st.button("Add Product to Cart"):
    if barcode in products:
        product = products[barcode]
        st.session_state.cart.append(product)
        st.session_state.total_cost += product["price"]
        st.success(f"Added {product['name']} to the cart!")

# View Cart
if st.button("View Cart"):
    if len(st.session_state.cart) == 0:
        st.info("Your cart is empty!")
    else:
        cart_details = ""
        for product in st.session_state.cart:
            cart_details += f"{product['name']} - ${product['price']} \n"
        st.text(cart_details)
        st.write(f"Total Cost: ${st.session_state.total_cost}")

# Checkout button
if st.button("Checkout"):
    if len(st.session_state.cart) == 0:
        st.warning("Your cart is empty!")
    else:
        # Show QR code or image for payment
        st.image('image.jpg', caption="Scan to Pay", use_column_width=100)
        st.success("Proceed to Payment!")
