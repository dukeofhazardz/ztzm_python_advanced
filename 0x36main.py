import smtplib
from email.message import EmailMessage
import re
import dotenv
import os

dotenv.load_dotenv()
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASS")

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def send_welcome_email(email):
    msg = EmailMessage()
    msg['Subject'] = "Welcome to Moviebox!"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = email
    msg.set_content(f"""Hi there, {email}

Thanks for signing up to Moviebox - your new home for movies, series and entertainment on demand!

Cheers,
The Moviebox Team.
""")
    
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print(f"\nWelcome email sent to {email}")
    except Exception as e:
        print(f"\nFailed to send email: {e}")

def main():
    print("Welcome to MovieBox Sign up CLI")
    
    user_email = input("Enter your email address to sign up: ").strip()
    if not is_valid_email(user_email):
        print("Invalid email format. Please try again")
        return
    
    print("\nSigning you up and sending you welcome email...")
    send_welcome_email(user_email)

if __name__ == '__main__':
    main()