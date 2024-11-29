import streamlit as st
import cv2
from pyzbar.pyzbar import decode
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

# Streamlit title and layout
st.title("Smart Shopping Trolley - QR Code Scanner")
st.write("Use your camera to scan the QR codes of products.")

# QR Code Scanner
def scan_product():
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

    # Initialize webrtc_streamer
    scanner = webrtc_streamer(
        key="qr-scanner",
        video_transformer_factory=QRCodeScanner,
        async_processing=True,
        media_stream_constraints={
            "video": True,  # Ensure video stream is enabled
            "audio": False,  # Disable audio
        },
    )

    # Return scanned result if available
    if scanner.video_transformer and scanner.video_transformer.result:
        return scanner.video_transformer.result
    return None

# Main function
def main():
    st.info("Click the 'Start Scan' button to activate the camera and scan QR codes.")

    # Create a button to start scanning
    if st.button("Start Scan"):
        scanned_code = scan_product()
        if scanned_code:
            st.success(f"QR Code Scanned: {scanned_code}")
        else:
            st.warning("No QR code detected. Try again.")

if __name__ == "__main__":
    main()
