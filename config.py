import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration settings
SENDER_EMAIL = os.getenv("SENDER_EMAIL", "mediastardeveloper4831@gmail.com")

# File paths
CREDENTIALS_FILE = 'credentials.json'
TOKEN_FILE = 'token.json'
LOG_FILE = 'logs/email_logs.txt'
TEMPLATE_FILE = 'templates/email_template.html'

# Scopes required for Gmail API
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
