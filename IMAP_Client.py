import imaplib
import email


class EmailClient:
    def __init__(self, server, email, password):
        print("Initializing EmailClient")
        self.server = server
        self.email = email
        self.password = password
        self.imap_connection = None

    def connect_imap(self):
        print(f"Connecting to IMAP server: {self.server}")
        self.imap_connection = imaplib.IMAP4_SSL(self.server)
        print("Logging in to IMAP")
        self.imap_connection.login(self.email, self.password)
        print("IMAP login successful")

    def list_mailboxes(self):
        if self.imap_connection:
            print("Listing IMAP mailboxes")
            status, mailboxes = self.imap_connection.list()
            if status == "OK":
                mailbox_list = []
                for mailbox in mailboxes:
                    print(f"Mailbox: {mailbox.decode()}")
                    parts = mailbox.decode().split(' ')
                    flags = parts[0].strip('()').split()
                    mailbox_name = parts[-1].strip('"')

                    if "\\Noselect" not in flags:
                        mailbox_list.append(mailbox_name)
                return mailbox_list
        return []

    def select_mailbox(self, mailbox="inbox"):
        if self.imap_connection:
            print(f"Selecting IMAP mailbox: {mailbox}")
            try:
                status, _ = self.imap_connection.select(mailbox)
                if status != "OK":
                    print(f"Failed to select mailbox: {mailbox}")
                    return False
                return True
            except Exception as e:
                print(f"Error selecting mailbox {mailbox}: {e}")
                return False
        return False

    def fetch_imap_emails(self, search_criterion="ALL"):
        if self.imap_connection:
            print(f"Fetching IMAP emails with criterion: {search_criterion}")
            try:
                status, messages = self.imap_connection.search(None, search_criterion)
                print(f"IMAP Search status: {status}, Messages: {messages}")
                if status == "OK":
                    email_ids = messages[0].split()
                    print(f"IMAP Email IDs: {email_ids}")
                    return email_ids
            except Exception as e:
                print(f"Error fetching emails: {e}")
        return []

    def get_imap_email(self, email_id):
        if self.imap_connection:
            print(f"Fetching IMAP email ID: {email_id}")
            try:
                email_id_str = email_id.decode()  # Decode byte string to regular string
                status, msg_data = self.imap_connection.fetch(email_id_str, "(RFC822)")
                print(f"IMAP Fetch status: {status}")
                if status == "OK" and msg_data:
                    raw_email = msg_data[0][1]
                    email_message = raw_email.decode("utf-8").split("\r\n")
                    print("IMAP Email fetched successfully")
                    return email_message
            except Exception as e:
                print(f"Error fetching email ID {email_id}: {e}")
        return None

    def parse_email(self, email_message):
        print("Parsing email")
        subject = email_message[0]

        sender = email_message[2]

        receiver = email_message[1]

        body = "\n".join(email_message[3:len(email_message)-1])

        print("\n" + "=" * 50)
        print(sender)
        print(receiver)
        print(subject)
        print("Body:")
        print(body)
        print("=" * 50 + "\n")

        return subject, sender, body

    def close_imap(self):
        if self.imap_connection:
            print("Closing IMAP connection")
            self.imap_connection.logout()
            print("IMAP Logout successful")


# Usage example
if __name__ == "__main__":
    server = "10.129.234.87"
    email = "robin"
    password = "robin"

    print("Creating EmailClient instance")
    client = EmailClient(server, email, password)

    print("Connecting to the IMAP server")
    client.connect_imap()

    print("Listing IMAP mailboxes")
    mailboxes = client.list_mailboxes()

    for mailbox in mailboxes:
        print(f"Selecting IMAP mailbox: {mailbox}")
        try:
            if client.select_mailbox(mailbox):
                email_ids = client.fetch_imap_emails()
                for email_id in email_ids:
                    print(f"Processing IMAP email ID: {email_id}")
                    try:
                        email_message = client.get_imap_email(email_id)
                        if email_message:
                            client.parse_email(email_message)
                    except Exception as e:
                        print(f"Error processing email ID {email_id}: {e}")
                        continue
        except Exception as e:
            print(f"Error processing mailbox {mailbox}: {e}")
            continue

    client.close_imap()
