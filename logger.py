import os
import datetime

from config import LOG_FILE

def log_email_status(recipient, status, message=""):
    """
    Logs the status of an email sent.
    
    Args:
        recipient (str): The email address of the recipient.
        status (str): "Success" or "Failure".
        message (str): Optional error message or details.
    """
    # Ensure logs directory exists
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] Recipient: {recipient} | Status: {status} | Details: {message}\n"
    
    try:
        with open(LOG_FILE, "a") as file:
            file.write(log_entry)
        # We don't print here to keep terminal clean unless requested
    except Exception as e:
        print(f"Failed to write to log file: {e}")
