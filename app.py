import streamlit as st
from PIL import Image
from streamlit import caching

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

# Title of the app with animation
st.markdown("<h1 style='text-align: center; color: blue;'>Smart Trolley - Dummy Interface</h1>", unsafe_allow_html=True)

# Add some animations and styles to the app
st.write("""
<style>
@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}
.loader {
    border: 16px solid #f3f3f3;
    border-top: 16px solid blue;
    border-radius: 50%;
    width: 120px;
    height: 120px;
    animation: spin 2s linear infinite;
}
</style>
<div class="loader" style="display: none;"></div>
""", unsafe_allow_html=True)

# Input for barcode with placeholder
barcode = st.text_input("Scan or Enter Product Barcode (e.g., 1234567890123)", placeholder="e.g. 1234567890123")

# Button to add product to cart with animation
col1, col2 = st.columns([3, 1])
with col1:
    if st.button("Add Product to Cart"):
        if barcode in products:
            product = products[barcode]
            st.session_state.cart.append(product)
            st.session_state.total_cost += product["price"]
            st.success(f"Added {product['name']} to the cart!")

# View Cart with animation
with col2:
    if st.button("View Cart"):
        if len(st.session_state.cart) == 0:
            st.info("Your cart is empty!")
        else:
            cart_details = ""
            for product in st.session_state.cart:
                cart_details += f"{product['name']} - ${product['price']} \n"
            st.text(cart_details)
            st.write(f"Total Cost: ${st.session_state.total_cost}")

# Checkout button with animation
if st.button("Checkout"):
    if len(st.session_state.cart) == 0:
        st.warning("Your cart is empty!")
    else:
        # Show QR code or image for payment
        image = Image.open('image.jpg')
        st.image(image, caption="Scan to Pay", width=200)  # Adjust width as needed
        st.success("Proceed to Payment!")
