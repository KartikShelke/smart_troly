import streamlit as st
import cv2
from pyzbar.pyzbar import decode
import requests

def scan_product():
    # This function will be a placeholder as Streamlit doesn't support direct webcam access
    return st.text_input("Enter barcode manually for testing")

def fetch_product(barcode):
    response = requests.post("http://127.0.0.1:5000/get-product", json={"barcode": barcode})
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Product not found!")
        return None

def display_cart(cart):
    total = 0
    for item in cart:
        st.write(f"{item['name']} - {item['quantity']} x {item['price']} = {item['quantity'] * item['price']}")
        total += item['quantity'] * item['price']
    st.write(f"Total: {total}")
    return total

def main():
    st.title("Smart Cart")
    cart = []
    
    if st.button("Scan Product"):
        barcode = scan_product()
        if barcode:
            product = fetch_product(barcode)
            if product:
                cart.append(product)
                st.success(f"Added {product['name']} to cart!")

    if st.button("View Cart"):
        display_cart(cart)

    if st.button("Checkout"):
        total = display_cart(cart)
        st.write("Redirecting to payment...")
        st.success("Payment Successful! Thank you for shopping.")

if __name__ == "__main__":
    main()