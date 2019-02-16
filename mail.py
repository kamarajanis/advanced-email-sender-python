# Python code to Sending mail from your Gmail account

# libraries 
import smtplib
import sys
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

fromaddr = "YOUR_GMAIL_ID"
#get the address to sent from command line arguments
toaddr = sys.argv[1]
#get the subject to sent from command line arguments
subject = sys.argv[2]
#get the body mail to sent from command line arguments
bodymail = sys.argv[3] 
   
# instance of MIMEMultipart 
msg = MIMEMultipart() 
  
# storing the senders email address   
msg['From'] = fromaddr 
  
# storing the receivers email address  
msg['To'] = toaddr 
  
# storing the subject  
msg['Subject'] = subject
  
# string to store the body of the mail 
body = bodymail
  
# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login(fromaddr, "YOUR_GMAIL_PASSWORD") 
  
# Converts the Multipart msg into a string 
text = msg.as_string() 
  
# sending the mail 
s.sendmail(fromaddr, toaddr, text) 
  
# terminating the session 
s.quit()
