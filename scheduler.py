import schedule
import time
from email_service import send_email

def job(to_email, subject, body, is_html=False):
    print(f"\n[Scheduler] Executing scheduled job: Sending email to {to_email}...")
    send_email(to_email, subject, body, is_html)

def schedule_email(to_email, subject, body, time_str, is_html=False):
    """
    Schedules an email to be sent at a specific time daily.
    
    Args:
        to_email (str): Recipient email address.
        subject (str): Email subject.
        body (str): Email body text or HTML.
        time_str (str): Time in "HH:MM" format (24-hour).
        is_html (bool): Whether the body is HTML.
    """
    schedule.every().day.at(time_str).do(job, to_email, subject, body, is_html)
    print(f"[Scheduler] Email scheduled for {to_email} at {time_str} every day.")

def run_scheduler():
    """
    Starts the scheduler loop. This function blocks.
    """
    print("\n[Scheduler] Started. Waiting for scheduled tasks...")
    print("Press Ctrl+C to stop the scheduler and return to menu (or exit).")
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[Scheduler] Stopped by user.")
