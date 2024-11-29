import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
from pyzbar.pyzbar import decode
import cv2

class QRCodeScanner(VideoTransformerBase):
    def __init__(self):
        self.result = None

    def transform(self, frame):
        image = frame.to_ndarray(format="bgr24")
        for barcode in decode(image):
            self.result = barcode.data.decode("utf-8")
            # Draw a rectangle around the QR code
            rect = barcode.rect
            cv2.rectangle(image, (rect.left, rect.top), 
                          (rect.left + rect.width, rect.top + rect.height), 
                          (255, 0, 0), 2)
            break  # Stop after detecting one QR code
        return image

def scan_product():
    scanner = webrtc_streamer(key="qr-scanner", 
                              video_transformer_factory=QRCodeScanner)
    if scanner.video_transformer and scanner.video_transformer.result:
        return scanner.video_transformer.result
    return None

def main():
    st.title("Smart Shopping Cart")
    cart = []

    if st.button("Start Scanning"):
        barcode = scan_product()
        if barcode:
            st.success(f"Scanned Barcode: {barcode}")
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
