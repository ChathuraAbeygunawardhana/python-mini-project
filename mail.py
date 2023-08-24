import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_emails():
    """
    Sends personalized emails to recipients listed in a CSV file.

    This function reads email addresses and names from a CSV file, and sends
    personalized emails to each recipient using the provided Gmail account.

    Note:
        - Make sure to enable "Less secure apps" in your Gmail settings.
        - Use an app-specific password if you have two-factor authentication enabled.

    Returns:
        None
    """
    from_addr = 'YOUR_SENDERS_EMAIL@gmail.com'  # Sender's Gmail address
    email = 'YOUR_EMAIL@gmail.com'  # Your Gmail address
    password = 'YOUR_APP_PASSWORD'  # Your Gmail app-specific password

    # Read recipient information from CSV
    data = pd.read_csv("recipient_list.csv")
    to_addr = data['email'].tolist()
    names = data['name'].tolist()

    # Sending emails
    for to_email, name in zip(to_addr, names):
        msg = MIMEMultipart()
        msg['From'] = from_addr
        msg['To'] = to_email
        msg['Subject'] = 'Subject of Your Email'

        body = f"Hello {name},\n\nEnter your email content here."  # Replace with your email content

        msg.attach(MIMEText(body, 'plain'))

        # Sending the email using SMTP
        with smtplib.SMTP('smtp.gmail.com', 587) as mail:
            mail.ehlo()
            mail.starttls()
            mail.login(email, password)
            text = msg.as_string()
            mail.sendmail(from_addr, to_email, text)


if __name__ == "__main__":
    send_emails()
