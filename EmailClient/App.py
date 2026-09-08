
import smtplib
from email.message import EmailMessage
import hashlib
import sys

class EmailClient:
    def __init__(self,sender,receiver,subject,body )-> None:
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.body_hash = hashlib.sha256(body.encode()).hexdigest()
        self.run()


    def ai_generation(self,task,input,lang = "English"):
       response = 
       if task == "compose":
           prompt = f"Write a professional email based on this:{input}"
       elif task == "summarize":
           prompt = f"Summarize this email body concisely:{input}"
       elif task == "translate":
           prompt = f"Translate this email into{lang}:{input}"
       self.body = response
       self.body_hash = hashlib.sha256(body.encode()).hexdigest()
       return self.body
    pass
       
    def match_io(self,signal):
       if signal == "mic":
           return "compose"
       elif signal == "touch sensor of single tap":
           return "summarize"
       elif signal == "touch sensor of double tap":
           return "translate"
    pass

    def read_variables(self):
        app_hash = {
            "sender" : self.sender,
            "receiver" : self.receiver,
            "subject" : self.subject,
            "body" : self.body,
            "body_hash" : self.body_hash
        }
        return app_hash
    pass
    
    def exit(self):
        if hasattr(self,'app_hash'):
            self.app_hash.clear()
        sys.exit(0)
        pass

    def display(self):
       print(f"From:{self.sender}")
       print(f"To:{self.receiver}")
       print(f"Subject:{self.subject}")
       print(f"Body:{self.body}")
    pass
       
    
    def run(self,signal):
       task = self.match_io(signal)
       self.ai_generation(task,signal)
       state = self.read_variables()
       self.diaplay(state)
    pass

if __name__ == "main":

 app = EmailClient()
app.run()


