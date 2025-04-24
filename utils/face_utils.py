import cv2
import numpy as np  # <-- Add this line
import face_recognition

def verify_face(image_file):
    """
    Verifies if the uploaded image contains a valid face.
    
    Args:
        image_file: The uploaded image containing a face.
    
    Returns:
        bool: True if face is detected, False otherwise.
    """
    # Decode image
    img = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
    
    # Convert image to RGB (face_recognition expects RGB format)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Detect faces in the image
    face_locations = face_recognition.face_locations(img_rgb)
    
    # Return True if a face is found, otherwise False
    if len(face_locations) > 0:
        return True
    else:
        return False
