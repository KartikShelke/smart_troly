import streamlit as st
import cv2
from pyzbar.pyzbar import decode
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
        # Decode the frame to check for QR codes
        image = frame.to_ndarray(format="bgr24")
        for barcode in decode(image):
            self.result = barcode.data.decode("utf-8")
            rect = barcode.rect
            # Draw a rectangle around the detected QR code
            cv2.rectangle(
                image,
                (rect.left, rect.top),
                (rect.left + rect.width, rect.top + rect.height),
                (0, 255, 0),
                2,
            )
            break
        return image

# Function to start the scan and check for QR code
def scan_product():
    scanner = webrtc_streamer(
        key="qr-scanner",
        video_transformer_factory=QRCodeScanner,
        async_processing=True,
        media_stream_constraints={
            "video": True,  # Enable video
            "audio": False,  # Disable audio
        },
    )

    # Give the camera a moment to initialize (added delay)
    time.sleep(2)  # Let the camera stabilize before checking

    # Return the scanned result if available
    if scanner.video_transformer and scanner.video_transformer.result:
        return scanner.video_transformer.result
    return None

# Main function for the Streamlit app
def main():
    st.info("Click the 'Start Scan' button to activate the camera and scan QR codes.")

    # Add a button to start the scan
    if st.button("Start Scan"):
        scanned_code = scan_product()
        if scanned_code:
            st.success(f"QR Code Scanned: {scanned_code}")
        else:
            st.warning("No QR code detected. Please try again.")

if __name__ == "__main__":
    main()
