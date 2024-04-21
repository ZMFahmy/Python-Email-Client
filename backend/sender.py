import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Sender:
    def __init__(self, email_address, password):
        self.server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        self.server.ehlo()

        self.email_address = email_address
        self.password = password

    def send_message(self, recipient_email, bcc, subject, message):
        self.server.login(self.email_address, self.password)
        msg = MIMEMultipart()
        msg["From"] = self.email_address
        msg["To"] = recipient_email
        msg["Bcc"] = bcc
        msg["Subject"] = subject

        msg.attach(MIMEText(message, 'plain'))

        text = msg.as_string()
        print(text)
        self.server.sendmail(self.email_address, recipient_email, text)
        print("Success")
