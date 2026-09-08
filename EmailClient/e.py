import smtplib #Needed to send the message
from email.message import EmailMessage# To import the email modules 
import imaplib,email#Needed to recieve mails

class EmailClient:
    def __init__(self,app_hash):
        self.app_hash = app_hash
        self.run()
        pass

    def ai_generation(self):
     pass


    def match_io(self):
       pass

    def read_variables(self):#Instead of using input(),a dictonary foe app_hash allows the CAISY to pass data automatically without us having to type i tin the terminal.
        app_hash = {
            "sender" : self.sender,
            "receiver" : self.receiver,
            "subject" : self.subject,
            "body" : self.body,
        }
        return app_hash
    pass
 

    def exit(self):
       pass

    def display(self):#To dispaly the content
       print(f"From:{self.sender}")
       print(f"To:{self.receiver}")
       print(f"Subject:{self.subject}")
       print(f"Body:{self.body}")
    pass

    def send(self):
         #It creates an SMTP server and establsihes a connection to the Gmail SMTP server
        smtpserver = smtplib.SMTP("smtp.gmail.com",587)
        #To identify yourself to an ESMTP server using EHLO
        smtpserver.ehlo()
        #Secure SMTP connection
        smtpserver.starttls()
        #Login to the server-Authenticaion
        smtpserver.login(self.username,self.password)
        #Sending an email
        self.From = self.sender
        self.To = self.receiver
        self.Subject = self.Subject
        self.Body = self.Body
        Content = f"Subject:{self.Subject}\n\nBody{self.Body}"  
        smtpserver.sendmail(self.From,self.To,Content)

        #Quits the smptp session
        smtpserver.quit()

    def receive(self,folder = "INBOX",criteria = "UNSEEN"):
         #Creates an imap object
         imapserver = imaplib.IMAP4_SSL("imap.gmail.com")#IMAP4_SSL  extends IMAP4 to use SSL for secure connections
         #Login:Authenticates with the server
         M = imapserver.login(self.username,self.password)
         #Use  "[Gmail]/All Mail"  for selecting mails from sent mail.
         imapserver.select(' "[Gmail]/All Mail" ',readonly=True)
         #Searches the mailbox for specific messages
         response,messages = imapserver.search(None,"UNSEEN")
         messages = messages[0].split()
         latest = int(messages[-1])#extract from last
         oldest = int(messages[0])#extract from start
         for i in range(latest,latest-20):#It displays only the top 20 unseen mails
         #Fetch
           res,msg =imapserver.fetch(str(i),"(RFC822)")
           for response in msg:
            if isinstance(response,tuple):
                #It converts raw server bytes into python object
                msg = email.message_from_bytes(response[1])
                #to print required information
                print(msg["From"])
                print(msg["Subject"])
                #Starts a loop to look inside every "part" of the email
                for part in msg.walk():
                    #An if condition to ignore html or images
                    if part.get_content_type() == "text/plain":
                        #To extract the raw text and convert it into readable string
                        Body = part.get_payload(decode = True)
                        print(f"Body:{Body.decode("UTF-8")}")
         M.close()
         M.logout()



   
    def run(self,task):
        self.read_variables()
        self.diaplay()
        if self.task == "send":
            self.send()
        elif self.task == "receive":
            self.receive()
    pass