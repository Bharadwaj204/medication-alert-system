import smtplib
from twilio.rest import Client
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import streamlit as st
import cv2
from utils.yolov_utils import detect_pill
from utils.qr_utils import verify_qr
from utils.face_utils import verify_face
from notifications import send_alert
from utils.logger import log_pill_intake
import os
import datetime

# Twilio configuration for SMS alerts
TWILIO_ACCOUNT_SID = 'Twilio Account SID'  # Replace with your Twilio Account SID
TWILIO_AUTH_TOKEN = 'Twilio Auth Token'    # Replace with your Twilio Auth Token
TWILIO_PHONE_NUMBER = 'your Twilio number'  # Replace with your Twilio number

# Email configuration for SMTP alerts
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "Replace with your email address@gmail.com"  # Replace with your email address
EMAIL_PASSWORD = "your email password"  # Replace with your email password

def send_sms_alert(message, recipient_number):
    """
    Send an SMS alert using Twilio.
    """
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    try:
        message = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=recipient_number
        )
        print(f"SMS sent successfully: {message.sid}")
    except Exception as e:
        print(f"Error sending SMS: {e}")

def send_email_alert(message, recipient_email):
    """
    Send an email alert using SMTP.
    """
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient_email
        msg['Subject'] = 'Pill Reminder Alert'
        
        msg.attach(MIMEText(message, 'plain'))
        
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_ADDRESS, recipient_email, text)
        server.quit()
        
        print(f"Email sent successfully to {recipient_email}")
    except Exception as e:
        print(f"Error sending email: {e}")

def send_alert(message):
    """
    Send alert via SMS and email to the caretaker.
    """
    caretaker_phone = '+1234567890'  # Replace with the caretaker's phone number
    caretaker_email = 'caretaker_email@example.com'  # Replace with caretaker's email address
    
    # Send SMS alert
    send_sms_alert(message, caretaker_phone)
    
    # Send Email alert
    send_email_alert(message, caretaker_email)

# Constants
IMAGE_PATH = 'dataset/pillsPicture/'
LOG_PATH = 'logs/pill_log.csv'

# Streamlit Page Configuration
st.set_page_config(page_title="Pill Reminder", layout="wide")
st.title("Pill Reminder & Monitoring System")

# Sidebar for navigation
st.sidebar.header("Pill Intake Settings")
task = st.sidebar.radio("Choose Task", ("Pill Validation", "Identity Verification", "History"))

if task == "Pill Validation":
    st.header("Pill Detection")
    uploaded_image = st.file_uploader("Upload an image of the pill", type=["jpg", "jpeg", "png"])
    if uploaded_image:
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
        if st.button("Validate Pill"):
            # Call YOLOv8 pill detection function
            result = detect_pill(uploaded_image)
            if result:
                st.success("✅ Pill detected successfully!")
                # Log the pill intake and send alert
                log_pill_intake(LOG_PATH, 'Pill Detected')
                send_alert("Pill detected successfully! Time to take your medication.")
                st.info("📨 SMS Sent | 📧 Email Sent")
                st.write(f"🕓 Intake logged: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
            else:
                st.error("❌ Pill detection failed! Please try again or assist the user.")
                send_alert("Pill detection failed. Please assist the user in taking the pill.")

elif task == "Identity Verification":
    st.header("Identity Verification")
    verify_method = st.selectbox("Choose Verification Method", ("QR Code", "Face Recognition"))

    if verify_method == "QR Code":
        qr_image = st.file_uploader("Upload QR Code Image", type=["jpg", "jpeg", "png"])
        if qr_image:
            if verify_qr(qr_image):
                st.success("✅ QR Code Verified Successfully!")
                log_pill_intake(LOG_PATH, 'QR Verified')
                send_alert("QR Code verified. Proceeding with pill intake.")
                st.info("📨 SMS Sent | 📧 Email Sent")
                st.write(f"🕓 Intake logged: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
            else:
                st.error("❌ QR Code Verification Failed. Try Again.")
                send_alert("QR Code verification failed. Assistance required.")

    elif verify_method == "Face Recognition":
        face_image = st.file_uploader("Upload Face Image", type=["jpg", "jpeg", "png"])
        if face_image:
            if verify_face(face_image):
                st.success("✅ Face Verified Successfully!")
                log_pill_intake(LOG_PATH, 'Face Verified')
                send_alert("Face verified. Proceeding with pill intake.")
                st.info("📨 SMS Sent | 📧 Email Sent")
                st.write(f"🕓 Intake logged: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
            else:
                st.error("❌ Face Verification Failed. Try Again.")
                send_alert("Face verification failed. Assistance required.")

elif task == "History":
    st.header("Pill Intake History")
    if os.path.exists(LOG_PATH):
        import pandas as pd
        history = pd.read_csv(LOG_PATH)
        st.write(history)
    else:
        st.write("No pill intake history available.")
