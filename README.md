# Email Client Script

This Python script provides a simple interface for interacting with an email server using IMAP. It allows users to:

- Connect to an IMAP server
- List available mailboxes
- Select a mailbox
- Fetch and display emails from a mailbox

The script is designed to handle common errors gracefully and display email content in a readable format.

---

## Features

1. **IMAP Connection**
   - Connect securely to an IMAP server using SSL.

2. **Mailbox Management**
   - List all mailboxes on the server.
   - Select specific mailboxes for email retrieval.

3. **Email Fetching**
   - Fetch emails using search criteria (default: `ALL`).
   - Display email subject, sender, and body.
   - Replace carriage returns (\r\n) with proper newlines for better readability.

4. **Error Handling**
   - Gracefully handle errors during mailbox selection and email fetching.
   - Continue processing other mailboxes or emails even if an error occurs.

---

## Requirements

- Python 3.8+
- Modules:
  - `imaplib`
  - `email`
  - `email.header`

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/email-client-script.git
   ```

2. Navigate to the project directory:
   ```bash
   cd IMAP-Mail-Dumper 
   ```

3. Run the script:
   ```bash
   python3 IMAP_Client.py
   ```

---

## Usage

### Configuring the Script

Update the following variables in the script to match your email server and credentials:

```python
server = "your.imap.server"
email = "your-email@example.com"
password = "your-password"
```

### Running the Script

Simply execute the script:

```bash
python IMAP_Client.py
```

The script will:
- Connect to the IMAP server.
- List available mailboxes.
- Retrieve emails from each mailbox.
- Display the subject, sender, and body of each email.

### Example Output

```plaintext
Creating EmailClient instance
Initializing EmailClient
Connecting to the IMAP server
Connecting to IMAP server: your.imap.server
Logging in to IMAP
IMAP login successful
Listing IMAP mailboxes
Mailbox: INBOX
Selecting IMAP mailbox: INBOX
Fetching IMAP emails with criterion: ALL
Processing IMAP email ID: 1
Subject: Test Email
From: sender@example.com
Body:
This is a test email.

--------------------------------------------------
```

---

## Known Issues

- Ensure the provided server, email, and password are correct.
- Only works with IMAP; POP3 is not supported.

---

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue to report bugs or suggest features.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

