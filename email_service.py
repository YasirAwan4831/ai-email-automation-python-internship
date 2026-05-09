import os
import base64
from email.message import EmailMessage

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from config import SCOPES, CREDENTIALS_FILE, TOKEN_FILE, SENDER_EMAIL
from logger import log_email_status

def authenticate_gmail():
    """
    Authenticates the user and returns the Gmail API service.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
        
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CREDENTIALS_FILE):
                raise FileNotFoundError(f"Missing '{CREDENTIALS_FILE}'. Please download it from Google Cloud Console.")
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            # Run local server for auth
            creds = flow.run_local_server(port=0)
            
        # Save the credentials for the next run
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
            
    try:
        service = build('gmail', 'v1', credentials=creds)
        return service
    except HttpError as error:
        print(f"An error occurred during Gmail API build: {error}")
        return None

def create_message(to_email, subject, message_text, is_html=False):
    """
    Creates an EmailMessage object encoded in base64url format.
    """
    message = EmailMessage()
    if is_html:
        message.set_content(message_text, subtype='html')
    else:
        message.set_content(message_text)

    message['To'] = to_email
    message['From'] = SENDER_EMAIL
    message['Subject'] = subject

    # encoded message
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {
        'raw': encoded_message
    }

def send_email(to_email, subject, body, is_html=False):
    """
    Sends an email using the Gmail API.
    """
    try:
        service = authenticate_gmail()
    except FileNotFoundError as e:
        print(f"Authentication Error: {e}")
        log_email_status(to_email, "Failure", str(e))
        return False
        
    if not service:
        print("Failed to obtain Gmail service.")
        log_email_status(to_email, "Failure", "Authentication failed.")
        return False
        
    try:
        message = create_message(to_email, subject, body, is_html)
        send_message = service.users().messages().send(userId="me", body=message).execute()
        
        print(f"Email sent successfully to {to_email}. Message Id: {send_message['id']}")
        log_email_status(to_email, "Success", f"Message Id: {send_message['id']}")
        return True
    except HttpError as error:
        error_msg = f"An error occurred: {error}"
        print(error_msg)
        log_email_status(to_email, "Failure", error_msg)
        return False
    except Exception as e:
        error_msg = f"An unexpected error occurred: {e}"
        print(error_msg)
        log_email_status(to_email, "Failure", error_msg)
        return False
