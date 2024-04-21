# Documentation

## Receiver Script

This script defines a `Receiver` class that provides functionality for receiving and processing new emails from an IMAP email server (specifically configured for Gmail). It uses Plyer to provide desktop notifications when new emails are received.

### Modules Imported

- `imaplib`: Used to interact with IMAP email servers.
- `email`: Used to handle email messages.
- `time`: Used for controlling delays in the script.
- `threading`: Used for running the email checking process in a separate thread.
- `plyer`: Used for sending desktop notifications.

### Functions

#### `send_notification(sender, subject)`

- Sends a desktop notification using Plyer when a new email is received.
- Parameters:
    - `sender` (`str`): The sender's email address.
    - `subject` (`str`): The subject line of the email.
- Behavior:
    - Uses Plyer to send a notification with the sender and subject details.
    - The notification is displayed for 15 seconds.

### Class `Receiver`

#### Constructor: `__init__(self, email_address, password)`

- Initializes a `Receiver` instance.
- Parameters:
    - `email_address` (`str`): The email address to connect to.
    - `password` (`str`): The password for the email account.
- Behavior:
    - Establishes a connection to the IMAP server (`imap.gmail.com`).
    - Retrieves existing messages from the inbox and stores their numbers.
    - Starts a separate thread for checking for new emails using the `check_new_emails()` method.

#### Method: `establish_connection(self)`

- Establishes a connection to the IMAP server and selects the inbox.
- Behavior:
    - Logs in to the IMAP server using the provided email and password.
    - Selects the inbox and prints the status.

#### Method: `check_new_emails(self)`

- Checks for new emails in the inbox periodically and sends notifications for new emails.
- Behavior:
    - Continuously logs in to the IMAP server and checks for new emails.
    - If new emails are detected, fetches the latest email and sends a notification using the `send_notification()` function.
    - Sleeps for 10 seconds between checks.

#### Method: `list_messages(self)`

- Returns a list of messages in the inbox with metadata.
- Behavior:
    - Iterates through messages in the inbox.
    - For each message, fetches and parses its content, storing metadata such as sender, recipient, subject, date, and BCC.
    - Returns a list of dictionaries containing message metadata.

#### Method: `get_specific_message(self, message_number)`

- Retrieves and returns the content of a specific message.
- Parameters:
    - `message_number` (`str`): The unique identifier of the message to retrieve.
- Behavior:
    - Fetches and parses the specified message.
    - Collects metadata (e.g., sender, recipient, date, subject) and content (`text/plain`) of the message.
    - Returns a dictionary with message metadata and content.

#### Method: `get_last_message(self)`

- Retrieves and returns the content of the last (most recent) message.
- Behavior:
    - Uses the `get_specific_message()` method to retrieve and return the most recent message in the inbox.

## Sender Script

This script defines a `Sender` class that provides functionality for sending emails using an SMTP email server (configured for Gmail).

### Modules Imported

- `smtplib`: Used to interact with SMTP email servers.
- `email.mime.text`: Provides the MIMEText class to represent the email message content.
- `email.mime.multipart`: Provides the MIMEMultipart class to represent the email structure.

### Class `Sender`

#### Constructor: `__init__(self, email_address, password)`

- Initializes a `Sender` instance and establishes a connection to the SMTP server.
- Parameters:
    - `email_address` (`str`): The sender's email address (account from which the email will be sent).
    - `password` (`str`): The password for the sender's email account.
- Behavior:
    - Creates a connection to the SMTP server (`smtp.gmail.com`) on port 465 using SSL encryption.
    - Initializes the connection and stores the sender's email address and password.

#### Method: `send_message(self, recipient_email, bcc, subject, message)`

- Sends an email message to the specified recipient.
- Parameters:
    - `recipient_email` (`str`): The recipient's email address.
    - `bcc` (`str`): The BCC (blind carbon copy) email address, if any.
    - `subject` (`str`): The subject line of the email.
    - `message` (`str`): The body of the email (plain text).
- Behavior:
    - Logs in to the SMTP server using the sender's email address and password.
    - Creates a MIMEMultipart message object and sets the "From," "To," "Bcc," and "Subject" fields.
    - Attaches the plain text message body to the MIMEMultipart object.
    - Converts the MIMEMultipart object to a string and sends the email.
    - Prints the content of the email and a success message to the console.

## GUI Script

This script defines a `GUI` class that provides a graphical user interface (GUI) for sending and receiving emails. It integrates with the `Receiver` and `Sender` classes from the backend package.

### Modules Imported

- `tkinter`: Used for creating the graphical user interface.
- `backend.receiver`: Imports the `Receiver` class from the backend package for handling email reception.
- `backend.sender`: Imports the `Sender` class from the backend package for handling email sending.

### Class `GUI`

The `GUI` class is responsible for managing the user interface and providing functionality for sending and receiving emails.

#### Constructor: `__init__(self, email, password)`

- Initializes a `GUI` instance.
- Parameters:
    - `email` (`str`): The email address of the user.
    - `password` (`str`): The password for the user's email account.
- Behavior:
    - Creates a `tkinter.Tk` window.
    - Initializes a `Sender` instance for sending emails and a `Receiver` instance for receiving emails.
    - Sets the initial state to "receiver" and displays the receiver screen.

#### Method: `clear_screen(self)`

- Clears all widgets from the main window.
- Behavior:
    - Iterates through all child widgets of the main window and destroys them.

#### Method: `send_pressed(self)`

- Handles the event when the "Send" button is pressed.
- Behavior:
    - If the current state is not "sender," clears the screen and displays the sender screen.

#### Method: `inbox_pressed(self)`

- Handles the event when the "Inbox" button is pressed.
- Behavior:
    - Establishes a connection to the email inbox using the `Receiver` instance.
    - Clears the screen and displays the receiver screen.

#### Method: `send_message_pressed(self, to, bcc, subject, message, to_entry, bcc_entry, subject_entry, text_widget)`

- Handles the event when the "Send Message" button is pressed.
- Parameters:
    - `to` (`str`): The recipient's email address.
    - `bcc` (`str`): The BCC (blind carbon copy) email address, if any.
    - `subject` (`str`): The subject line of the email.
    - `message` (`str`): The body of the email (plain text).
    - `to_entry`, `bcc_entry`, `subject_entry` (`tkinter.Entry`): Entry widgets for the recipient, BCC, and subject fields.
    - `text_widget` (`tkinter.Text`): The text widget containing the email body.
- Behavior:
    - Sends the email using the `Sender` instance.
    - Clears the content of the entry and text widgets.

#### Method: `show_sender_screen(self)`

- Displays the sender screen in the GUI.
- Behavior:
    - Sets the current state to "sender."
    - Configures the GUI for sending emails, including buttons, labels, and text widgets.

#### Method: `show_receiver_screen(self)`

- Displays the receiver screen in the GUI.
- Behavior:
    - Sets the current state to "receiver."
    - Configures the GUI for receiving emails, including buttons, labels, and text widgets.
    - Retrieves the last received message using the `Receiver` instance and displays its details in the GUI.

## How to Run the Application

1. Open the terminal and navigate to the directory that contains the project files.
2. example credentials to show running of commands:
    - Email: `example@gmail.com`
    - Password: `kdjg lajf oytr mqal`
3. Run the following command:

    ```bash
    python main.py example@gmail.com kdjg lajf oytr mqal
    ```
