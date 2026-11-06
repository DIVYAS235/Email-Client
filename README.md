Python Email Client
A simple command-line email client built with Python that uses Gmail's SMTP server to send emails. The application authenticates with a Gmail.
App Password, collects the sender and recipient details, and sends an
email with a subject and message body.
Features
- Connects to Gmail's SMTP server using an SMTP client.
- Authenticates using a Gmail App Password.
- Accepts the sender's Gmail address and credentials at runtime.
- Collects the recipient's email address, subject, and message.
- Sends an email and allows the user to verify delivery in the recipient's inbox.
How It Works
1. Run Email.py.
2. Enter the Gmail address that will send the email.
3. Enter the Gmail App Password when prompted.
4. Choose the send option (S) when prompted.
5. Enter the sender address, recipient address, subject, and message.
6. The application connects to Gmail's SMTP server, authenticates, and
   sends the email.
7. Check the recipient's inbox to confirm that the message was delivered.


Requirements
- Python 3
- A Gmail account
- Two-Step Verification enabled on the sending Google account
- A Gmail App Password

Gmail App Password Setup
1. Enable Two-Step Verification on your Google account.
2. Create an App Password in your Google Account security settings.
3. Use that App Password when the application prompts for the password.
Google may change the exact location or availability of App Password
settings. Use Google's official account security settings for the
current instructions.
Security Notice
- Never publish your Gmail password or App Password.
- Do not hard-code credentials in the source code or commit them to
  GitHub.
- If an App Password has appeared in a screenshot, terminal recording,
  source file, or public repository, revoke it immediately in your
  Google Account and generate a new one.
- For a production-ready version, load credentials securely from
  environment variables or a secrets manager, and avoid printing them
  in the terminal.
- Do not commit .env files. If you use one, add it to .gitignore
  and provide a .env.example containing placeholders only.
Technologies Used
- Python
- SMTP (Simple Mail Transfer Protocol)
- Gmail SMTP server

Test Result
The application was tested by sending an email from the configured Gmail
account to a second email account. The message was successfully received
in the recipient's inbox.