Pill Reminder & Monitoring System
Overview
The Pill Reminder & Monitoring System is a Streamlit-based application designed to assist users in tracking their pill intake. The system allows for pill detection, identity verification, and alerts (SMS and email) to caregivers, ensuring the user takes their medication on time. The application leverages YOLOv8 for pill detection, QR code and face recognition for identity verification, and integrates with Twilio and SMTP for SMS and email notifications.

Features
Pill Validation: Upload a picture of a pill, and the app will use YOLOv8 to detect the pill.

Identity Verification: Users can choose between QR code verification or face recognition to ensure the correct person is taking the medication.

Alert Notifications: Sends SMS and email alerts to caregivers upon successful pill detection or identity verification.

History Logging: Tracks and logs pill intake events.

Technologies Used
Streamlit: For building the web interface.

YOLOv8: For pill detection.

QR Code & Face Recognition: For identity verification.

Twilio: For SMS alerts.

SMTP (Gmail): For email notifications.

OpenCV: For image processing and detection.

Pandas: For logging and displaying history.

Project Structure
graphql
Copy
Edit
pill_reminder/
├── app.py              # Main Streamlit app
├── utils/
│   ├── yolov_utils.py  # YOLOv8 model and pill detection functions
│   ├── qr_utils.py     # QR code verification functions
│   ├── face_utils.py   # Face recognition functions
│   ├── logger.py       # Logging functions for pill intake
├── notifications.py    # Contains functions to send SMS and email alerts
├── dataset/
│   └── pillsPicture/   # Folder for storing images of pills
├── logs/
│   └── pill_log.csv    # Log file for pill intake history
└── requirements.txt    # Python dependencies
Installation
Prerequisites
Make sure you have Python 3.7+ installed. You will also need an active Twilio account for SMS notifications and a Gmail account for email notifications.

Install Dependencies
Create a virtual environment and install the required dependencies by running the following commands:

Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/pill-reminder.git
cd pill-reminder
Create a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
Install the required Python packages:

bash
Copy
Edit
pip install -r requirements.txt
Install additional dependencies for Twilio and email:

bash
Copy
Edit
pip install twilio smtplib opencv-python
Ensure you have the necessary models for YOLOv8 and any other model files. These should be placed in the appropriate folders (yolov_utils.py handles YOLOv8).

Twilio & Email Configuration
Twilio: Set up your Twilio account and get your Account SID, Auth Token, and Phone Number from Twilio Console.

Replace TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, and TWILIO_PHONE_NUMBER in app.py with your own credentials.

Email: Use your Gmail account for email notifications.

Replace EMAIL_ADDRESS and EMAIL_PASSWORD in app.py with your Gmail credentials.

If using Gmail, you may need to enable Less Secure Apps or create an App Password if 2-Step Verification is enabled. More details: Google's App Passwords.

Running the Application
To run the application, execute the following command:

bash
Copy
Edit
streamlit run app.py
This will launch the Streamlit app in your default browser.

How to Use the App
Pill Validation:

Upload an image of the pill.

Click "Validate Pill" to let the app detect the pill using YOLOv8.

If the pill is detected, you will see a success message, and a notification will be sent to the caregiver (SMS and email).

Identity Verification:

Choose either QR Code or Face Recognition for verifying the identity of the person taking the pill.

Upload the respective image.

If verification is successful, a notification will be sent to the caregiver.

History:

View a log of past pill intake events, which includes timestamps and whether the pill was successfully detected and verified.

Dependencies
streamlit: For the app interface.

opencv-python: For image processing and detection.

twilio: For sending SMS alerts.

smtplib: For sending email alerts.

pandas: For logging and displaying the pill intake history.

yolov8: For YOLO-based pill detection.

face_recognition: For face recognition.

pyzbar: For QR code scanning.

Troubleshooting
No SMS or Email Sent:

Check if your Twilio account SID, Auth Token, and phone number are correctly configured.

Ensure the Gmail account is properly set up for sending emails.

Verify that the images uploaded for pill detection or identity verification are clear and properly formatted.

Image Detection Fails:

Ensure you have the necessary YOLOv8 model files.

Check if the image quality is sufficient for detection