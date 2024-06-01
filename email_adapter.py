import smtplib
from email.message import EmailMessage
import ssl


# Adapters
class EmailAdapter:
    def __init__(self, sender_email, sender_password):
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, receiver_email, subject, body):
        message = EmailMessage()
        message["From"] = self.sender_email
        message["To"] = ', '.join(receiver_email) if isinstance(receiver_email, list) else receiver_email
        message["Subject"] = subject
        message.set_content(body)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.sender_email, self.sender_password)
            smtp.sendmail(self.sender_email, receiver_email, message.as_string())
