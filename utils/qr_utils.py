import cv2

# Function to verify QR Code
def verify_qr(image_file):
    # Read the uploaded QR code image
    img = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
    
    # Initialize the QRCode detector
    detector = cv2.QRCodeDetector()

    # Detect and decode the QR code from the image
    value, pts, qr_code = detector(img)

    # If QR code is detected, value will be non-empty
    if value:
        return True
    return False
