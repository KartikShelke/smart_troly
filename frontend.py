import cv2
import requests
from pyzbar.pyzbar import decode

# Store cart details
cart = []

# Scan QR code/barcode using camera
def scan_product():
    cap = cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()
        for barcode in decode(frame):
            barcode_data = barcode.data.decode('utf-8')
            cap.release()
            cv2.destroyAllWindows()
            return barcode_data
        cv2.imshow("Scan Product", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# Fetch product details
def fetch_product(barcode):
    response = requests.post("http://127.0.0.1:5000/get-product", json={"barcode": barcode})
    if response.status_code == 200:
        return response.json()
    else:
        print("Product not found!")
        return None

# Display cart and total cost
def display_cart():
    print("\nYour Cart:")
    total = 0
    for item in cart:
        print(f"{item['name']} - {item['quantity']} x {item['price']} = {item['quantity'] * item['price']}")
        total += item['quantity'] * item['price']
    print(f"Total: {total}\n")
    return total

# Main Function
def main():
    while True:
        print("\n1. Scan Product")
        print("2. View Cart")
        print("3. Checkout")
        choice = input("Enter your choice: ")

        if choice == "1":
            barcode = scan_product()
            product = fetch_product(barcode)
            if product:
                cart.append(product)
                print(f"Added {product['name']} to cart!")

        elif choice == "2":
            display_cart()

        elif choice == "3":
            total = display_cart()
            print("Redirecting to payment...")
            # UPI payment integration can be added here
            print("Payment Successful! Thank you for shopping.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()