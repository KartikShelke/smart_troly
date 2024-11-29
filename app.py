import streamlit as st

# Dummy product data
products_db = {
    "1": {"name": "Milk", "quantity": 50, "price": 50.0},
    "2": {"name": "Bread", "quantity": 30, "price": 30.0},
    "3": {"name": "Eggs", "quantity": 100, "price": 5.0},
    "4": {"name": "Juice", "quantity": 20, "price": 40.0},
}

# Cart to store selected products
cart = []

# Function to add product to the cart
def add_to_cart(barcode):
    if barcode in products_db:
        product = products_db[barcode]
        cart.append(product)
        st.success(f"Added {product['name']} to the cart!")
    else:
        st.error("Product not found!")

# Function to display cart and total cost
def display_cart():
    if not cart:
        st.info("Your cart is empty!")
        return 0
    total = 0
    st.write("Your Cart:")
    for item in cart:
        st.write(f"{item['name']} - {item['quantity']} x {item['price']} = {item['quantity'] * item['price']}")
        total += item['quantity'] * item['price']
    st.write(f"Total: {total}")
    return total

# Main function to display the interface
def main():
    st.title("Smart Trolley - Dummy Interface")
    st.write("Welcome to the Smart Trolley. Scan products and manage your cart.")

    # Simulate product scanning by manually entering barcode
    barcode = st.text_input("Enter Product Barcode (e.g., 1234567890123):")

    if st.button("Add Product to Cart"):
        if barcode:
            add_to_cart(barcode)
        else:
            st.error("Please enter a valid barcode!")

    # View Cart
    if st.button("View Cart"):
        total = display_cart()
        st.write(f"Total Cost: {total}")

    # Checkout
    if st.button("Checkout"):
        total = display_cart()
        if total > 0:
            st.write("Proceeding to payment...")
            st.success("Payment Successful! Thank you for shopping.")
        else:
            st.warning("Your cart is empty. Add products before checking out.")

# Run the app
if __name__ == "__main__":
    main()
