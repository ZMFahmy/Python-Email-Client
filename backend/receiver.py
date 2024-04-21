import imaplib
import email
import time
import threading
from plyer import notification


def send_notification(sender, subject):
    notification.notify(
        title='New email received',
        message=f'From: {sender}\nSubject: {subject}',
        timeout=15
    )


class Receiver:
    def __init__(self, email_address, password):
        self.imap = None
        self.imap_server = "imap.gmail.com"
        self.email_address = email_address
        self.password = password

        self.establish_connection()

        _, messages_numbers = self.imap.search(None, "ALL")
        self.messages_numbers_split = messages_numbers[0].split()

        email_thread = threading.Thread(target=self.check_new_emails)
        email_thread.start()

    def establish_connection(self):
        self.imap = imaplib.IMAP4_SSL(host=self.imap_server, port=993)
        self.imap.login(self.email_address, self.password)

        status, messages = self.imap.select('INBOX')
        print("Inbox mailbox status:", status)

    def check_new_emails(self):
        while True:
            self.imap = imaplib.IMAP4_SSL(host=self.imap_server, port=993)
            self.imap.login(self.email_address, self.password)
            status, messages = self.imap.select('INBOX')
            _, new_messages_numbers = self.imap.search(None, "ALL")
            if len(new_messages_numbers[0].split()) > len(self.messages_numbers_split):
                self.messages_numbers_split = new_messages_numbers[0].split()
                _, data = self.imap.fetch(self.messages_numbers_split[-1], "(RFC822)")
                message = email.message_from_bytes(data[0][1])
                send_notification(message["From"], message["Subject"])
            time.sleep(10)

    def list_messages(self):
        messages = []
        for i in range(len(self.messages_numbers_split) - 1, -1, -1):
            _, data = self.imap.fetch(self.messages_numbers_split[i], "(RFC822)")

            message = email.message_from_bytes(data[0][1])
            message_data = {"Message Number": self.messages_numbers_split[i],
                            "From": message.get('From'),
                            "To": message.get('To'),
                            "BCC": message.get('BCC'),
                            "Date": message.get('Date'),
                            "Subject": message.get('Subject')
                            }
            messages.append(message_data)
        return messages

    def get_specific_message(self, message_number):
        _, data = self.imap.fetch(message_number, "(RFC822)")

        message = email.message_from_bytes(data[0][1])
        message_data = {"Message Number": message_number,
                        "From": message.get('From'),
                        "To": message.get('To'),
                        "BCC": message.get('BCC'),
                        "Date": message.get('Date'),
                        "Subject": message.get('Subject'),
                        "Content": ""
                        }
        for part in message.walk():
            if part.get_content_type() == "text/plain":
                message_data["Content"] += part.get_payload()

        return message_data

    def get_last_message(self):
        return self.get_specific_message(self.messages_numbers_split[-1])
