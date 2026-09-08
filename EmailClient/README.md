EMAIL CLIENT

A simple email app which uses Cient-Server architecture 
Frontend : a user interface with simple HTML,CSS,Javascript to display inboxes,read emails,and a composer

Backend : Handles secure communication,uses smtplib for sending emails and imaplib for receivind emails. ,email.mime to handle attachments and HTML formatting.

The MAP:
Sending email
Firstly,the app connects to the server(for eg:smtp.gmail.com)
Encryption:The app uses TLS(Transport Layer Security) for security to protect it from hackers.
Authentication:The app provides the username and password.
The envelope:Tells the server who the sender is and who the recipient is.
Payload:To hand over the actual subject and body of the email.
Handoff:Once the server says "ok",it takes the message from sender and tries to deliver it to the receiver.


Receiving Email
The Warehouse:When someone sends the email,it doesnt go to the computer,it sits on the server(Warehouse)
Logging in:The python app connects to the  IMAP server(for eg:imap.gmail.com) and logs in.
Selects the folder.
Searching "unread mails".
Fetching:The server send the data.
Warning:the data usualy looks like a giant block (including headers,timestamps,encoded attachments).
Parsing:The app has the parse or clean up that data to show only the "From" and "Body" text to the user.


State
1.Open the connection
2.Authenticate
3.Execute the command
4.Close the connection

