import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import time

# Streamlit title and layout
st.title("Smart Shopping Trolley - QR Code Scanner")
st.write("Use your camera to scan the QR codes of products.")

# QR Code Scanner class for processing video
class QRCodeScanner(VideoTransformerBase):
    def __init__(self):
        self.result = None

    def transform(self, frame):
        # Process frame (QR code detection code would go here)
        image = frame.to_ndarray(format="bgr24")
        # Assuming that QR code detection logic will be added here
        # Example: If a QR code is detected, store the result
        # For now, you can simulate a barcode for testing purposes
        self.result = "1234567890123"  # Example result (barcode)
        return image

# Function to start the scan and check for QR code
def scan_product():
    # Creating an instance of webrtc_streamer with async_processing
    scanner = webrtc_streamer(
        key="qr-scanner",
        video_transformer_factory=QRCodeScanner,
        async_processing=True,
        media_stream_constraints={
            "video": True,  # Enable video
            "audio": False,  # Disable audio
        },
    )
    
    # Allow camera to initialize properly and get QR code results
    time.sleep(1)  # Short sleep to allow initialization
    return scanner

# Main function for the Streamlit app
def main():
    st.info("Click the 'Start Scan' button to activate the camera and scan QR codes.")
    
    # Initialize scan button
    if st.button("Start Scan"):
        scanner = scan_product()  # Start scanning when button is clicked
        if scanner.video_transformer and scanner.video_transformer.result:
            scanned_code = scanner.video_transformer.result
            st.success(f"QR Code Scanned: {scanned_code}")
        else:
            st.warning("No QR code detected. Please try again.")

if __name__ == "__main__":
    main()
