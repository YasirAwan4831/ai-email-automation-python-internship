import sys
from email_service import send_email
from scheduler import schedule_email, run_scheduler
from utils.helpers import read_template
from config import TEMPLATE_FILE

def display_menu():
    print("\n" + "="*30)
    print("   Email Automation System")
    print("="*30)
    print("1. Send an email immediately")
    print("2. Schedule an email")
    print("3. Start scheduler loop")
    print("4. Exit")
    print("="*30)
    return input("Select an option (1-4): ")

def get_email_details(is_scheduling=False):
    to_email = input("Recipient email: ")
    subject = input("Subject: ")
    
    use_template = input("Use HTML template? (y/n): ").strip().lower() == 'y'
    if use_template:
        body = read_template(TEMPLATE_FILE)
        if not body:
            print("Template is empty or missing. Falling back to simple text.")
            body = input("Message body: ")
            use_template = False
        else:
            print(f"Loaded template from {TEMPLATE_FILE}")
    else:
        body = input("Message body: ")
        
    return to_email, subject, body, use_template

def main():
    while True:
        choice = display_menu()
        
        if choice == '1':
            print("\n--- Send Email ---")
            to_email, subject, body, is_html = get_email_details()
            print("\nSending email...")
            send_email(to_email, subject, body, is_html)
            
        elif choice == '2':
            print("\n--- Schedule Email ---")
            to_email, subject, body, is_html = get_email_details(is_scheduling=True)
            time_str = input("Enter schedule time (HH:MM in 24-hour format, e.g., 14:30): ")
            schedule_email(to_email, subject, body, time_str, is_html)
            print("\nNOTE: You must select 'Start scheduler loop' (Option 3) to actually run scheduled jobs.")
            
        elif choice == '3':
            run_scheduler()
            
        elif choice == '4':
            print("Exiting Email Automation System. Goodbye!")
            sys.exit(0)
            
        else:
            print("Invalid option. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting Email Automation System. Goodbye!")
        sys.exit(0)
