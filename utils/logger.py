import csv
from datetime import datetime

def log_pill_intake(log_path, event):
    """
    Logs pill intake events to a CSV file with a timestamp.
    
    Args:
        log_path (str): Path to the log file.
        event (str): Event to log (e.g., 'Pill Detected', 'QR Verified').
    """
    # Check if the log file exists, and create it if it doesn't
    file_exists = False
    try:
        with open(log_path, mode='r', newline='', encoding='utf-8') as file:
            file_exists = True
    except FileNotFoundError:
        pass

    # Open the log file and append the event with a timestamp
    with open(log_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # If file is empty, write headers
        if not file_exists:
            writer.writerow(['Timestamp', 'Event'])
        
        # Write the current timestamp and event
        writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), event])
