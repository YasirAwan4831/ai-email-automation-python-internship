# Email Automation System

This is a lightweight, professional Python-based Email Automation System designed for scheduling and sending emails using the Gmail API. It maintains email history logs and provides a clean terminal-based interface.

## Prerequisites

1.  **Python Installed**: Ensure you have Python 3.7+ installed. You can check by running `python --version` in your terminal.
2.  **Google Account**: A standard Google/Gmail account to send emails from.

## Step 1: Install Dependencies

Open your terminal or command prompt, navigate to the project directory, and run:

```bash
pip install -r requirements.txt
```

## Step 2: Configure Environment Variables

1. Open the `.env` file in the root of the project.
2. Replace `your_email@gmail.com` with the Gmail address you will use to send the emails.
   ```env
   SENDER_EMAIL=your_actual_email@gmail.com
   ```

## Step 3: Set up Gmail API Credentials

This is the most important step to allow your script to send emails securely.

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. **Create a new Project**: Click the project dropdown at the top and select "New Project". Name it something like "Email Automation".
3. **Enable Gmail API**:
   - Go to "APIs & Services" -> "Library".
   - Search for "Gmail API" and click "Enable".
4. **Configure OAuth Consent Screen**:
   - Go to "APIs & Services" -> "OAuth consent screen".
   - Choose "External" and click "Create".
   - Fill in the required fields (App name, User support email, Developer contact information). You can use your own email for these.
   - Click "Save and Continue" through the Scopes and Test users screens (you can add your own email as a Test user).
5. **Create Credentials**:
   - Go to "APIs & Services" -> "Credentials".
   - Click "Create Credentials" -> "OAuth client ID".
   - Select "Desktop app" as the Application type.
   - Name it (e.g., "Python Email App") and click "Create".
6. **Download Credentials**:
   - After creation, you will see your Client ID and Client Secret. Click the "Download JSON" button.
   - Rename the downloaded file to `credentials.json`.
   - **Move `credentials.json` into the root folder of this project** (`email-automation-system/`).

## Step 4: Run the Application

Now you are ready to run the system!

1. In your terminal, run:
   ```bash
   python main.py
   ```
2. **First-time Authentication**:
   - The first time you send an email or start the app, a browser window will open asking you to log in to your Google account.
   - It will warn you that "Google hasn't verified this app". This is normal since you just created it. Click "Advanced" -> "Go to [Your App Name] (unsafe)".
   - Click "Continue" to grant the app permission to "Send email on your behalf".
   - After allowing access, you can close the browser. A `token.json` file will be created in your project folder, which keeps you logged in for future runs.

## Features & Usage

When you run `python main.py`, you will see a terminal menu:
- **Option 1**: Sends an email immediately. You can choose to use the HTML template (`templates/email_template.html`) or write plain text.
- **Option 2**: Schedules an email. Enter the time in 24-hour format (e.g., `14:30` for 2:30 PM). 
- **Option 3**: Starts the scheduler loop. **You must run this for scheduled emails to actually send!** It will run in the background until you press `Ctrl+C`.
- **Logs**: All sent emails (successes and failures) are recorded in `logs/email_logs.txt`.
