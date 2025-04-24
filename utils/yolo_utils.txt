from ultralytics import YOLO
import tempfile
from PIL import Image

# Load YOLOv8 model once globally
model = YOLO("models/yolov8n.pt")

def detect_pill(image_file):
    """
    Detects pills in the uploaded image using YOLOv8 model.
    
    Args:
        image_file: The uploaded image file (e.g., from Streamlit's file_uploader).
    
    Returns:
        bool: True if any object is detected (assuming it's a pill), False otherwise.
    """
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_img:
        temp_img.write(image_file.read())
        temp_img_path = temp_img.name

    # Run detection using YOLOv8 model
    results = model(temp_img_path)

    # Check if any objects (pills) are detected
    for r in results:
        if r.boxes is not None and len(r.boxes) > 0:
            return True
    return False
