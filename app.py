import streamlit as st
from streamlit_animated import animated
from PIL import Image

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
st.markdown("<h1 style='text-align: center; color: #FFA07A;'>Smart Trolley - Dummy Interface</h1>", unsafe_allow_html=True)

# Input for barcode
barcode = st.text_input("Enter Product Barcode (e.g., 1234567890123):")

# Button to add product to cart
if st.button("Add Product to Cart"):
    if barcode in products:
        product = products[barcode]
        st.session_state.cart.append(product)
        st.session_state.total_cost += product["price"]
        animated.bounce(st.success(f"Added {product['name']} to the cart!"))

# View Cart
if st.button("View Cart"):
    if len(st.session_state.cart) == 0:
        animated.flash(st.info("Your cart is empty!"))
    else:
        cart_details = ""
        for product in st.session_state.cart:
            cart_details += f"{product['name']} - ${product['price']} \n"
        
        st.markdown("<div style='background-color: #F0F8FF; padding: 10px; border-radius: 5px;'>"
                    f"<pre>{cart_details}</pre></div>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='color: #32CD32;'>Total Cost: ${st.session_state.total_cost}</h3>", unsafe_allow_html=True)

# Checkout button
if st.button("Checkout"):
    if len(st.session_state.cart) == 0:
        animated.shake(st.warning("Your cart is empty!"))
    else:
        image = Image.open('image.jpg')
        st.image(image, caption="Scan to Pay", width=200)
        animated.pulse(st.success("Proceed to Payment!"))
