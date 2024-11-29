import streamlit as st
import cv2
from pyzbar.pyzbar import decode
import requests
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    barcode = db.Column(db.String(100), unique=True, nullable=False)

# Initialize Database
def init_db():
    with app.app_context():
        db.create_all()

# Default Route
@app.route('/')
def index():
    return "Welcome to the Smart Cart API! Use the /get-product endpoint to fetch product details."

# API to get product details by barcode
@app.route('/get-product', methods=['POST'])
def get_product():
    data = request.json
    barcode = data.get('barcode')
    product = Product.query.filter_by(barcode=barcode).first()
    if product:
        return jsonify({
            'name': product.name,
            'quantity': product.quantity,
            'price': product.price
        }), 200
    return jsonify({'error': 'Product not found'}), 404

# Streamlit App
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
    init_db()  # Initialize the database before running the app
    main()
