# 💊 Pill Reminder & Monitoring System

A Streamlit-based application that helps users stay on track with their medication. The system ensures pill intake is validated through computer vision, identity is verified, and caregivers are notified via SMS and email.

---

## 📌 Features

- **Pill Detection:** Detects pills in uploaded images using YOLOv8.
- **Identity Verification:** Verifies the user via QR Code or Face Recognition.
- **Alert Notifications:** Sends SMS (via Twilio) and Email (via SMTP/Gmail) to caregivers upon successful intake.
- **History Logging:** Tracks and logs all pill intake events with timestamps.

---

## 🛠️ Technologies Used

- **Streamlit** – Web UI
- **YOLOv8** – Pill detection
- **OpenCV** – Image processing
- **face_recognition** – Face verification
- **pyzbar** – QR Code scanning
- **Twilio** – SMS notifications
- **smtplib** – Email notifications
- **Pandas** – Logging history

---

## 📁 Project Structure

pill_reminder/ ├── app.py # Main Streamlit app ├── utils/ │ ├── yolov_utils.py # YOLOv8 detection │ ├── qr_utils.py # QR code verification │ ├── face_utils.py # Face recognition │ └── logger.py # Logging functions ├── notifications.py # SMS & Email alerts ├── dataset/ │ └── pillsPicture/ # Pill image dataset ├── logs/ │ └── pill_log.csv # Log history └── requirements.txt # Python dependencies

yaml
Copy
Edit

---

## ⚙️ Installation

### Prerequisites

- Python 3.7+
- Twilio account for SMS
- Gmail account for email

### Setup Instructions

```bash
# Clone the repository
git clone https://github.com/your-username/pill-reminder.git
cd pill-reminder

# Create and activate a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install twilio smtplib opencv-python
YOLOv8 Model
Make sure the necessary YOLOv8 model files are downloaded and available in the appropriate folders (handled in yolov_utils.py).

🔐 Configuration
Twilio Setup
Update the following variables in app.py:

python
Copy
Edit
TWILIO_ACCOUNT_SID = "your_sid"
TWILIO_AUTH_TOKEN = "your_auth_token"
TWILIO_PHONE_NUMBER = "your_twilio_number"
Gmail Setup
Update the email configuration in app.py:

python
Copy
Edit
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_email_password"  # Consider using App Passwords
Note: If you use Gmail with 2-Step Verification, enable App Passwords.

🚀 Running the App
bash
Copy
Edit
streamlit run app.py
The app will launch in your default web browser.

🧪 How to Use
✅ Pill Validation
Upload an image of the pill.

Click "Validate Pill".

If detected, success message is shown and notifications are sent.

✅ Identity Verification
Choose QR Code or Face Recognition.

Upload a matching image.

Upon verification, notifications are sent.

📖 History
View past pill intake events with timestamps.

Check verification status and detection success.

🧯 Troubleshooting
❌ SMS or Email Not Sent?
Double-check Twilio and Gmail credentials.

Make sure Gmail allows third-party apps or use App Passwords.

❌ Detection/Verification Fails?
Ensure YOLO model files are in place.

Use clear, high-resolution images.
