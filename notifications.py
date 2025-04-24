import smtplib
from twilio.rest import Client
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
