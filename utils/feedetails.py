import email
import smtplib
import ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from datetime import date, datetime, timedelta


def sendemail(receiver_email, filename):
    """
    send receipt to learners email
    """

    subject = "learningdhara payment receipt"
    body = "This is an auto-generated email with payment receipt attachment"
    sender_email = "nishant@learningdhara.com"
    password = "xxxxxxxxx"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = "py.nishant@gmail.com"  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    # filename = "document.pdf"  # In same directory as script

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)


def get_first_date_of_current_month(year, month):
    """Return the first date of the month.

    Args:
        year (int): Year
        month (int): Month

    Returns:
        date (datetime): First date of the current month
    """

    first_date = datetime(year, month, 1)
    return first_date.strftime("%Y-%m-%d")


def get_last_date_of_month(year, month):
    """Return the last date of the month.

    Args:
        year (int): Year, i.e. 2022
        month (int): Month, i.e. 1 for January

    Returns:
        date (datetime): Last date of the current month
    """

    if month == 12:
        last_date = datetime(year, month, 31)
    else:
        last_date = datetime(year, month + 1, 1) + timedelta(days=-1)

    return last_date.strftime("%Y-%m-%d")
