import smtplib
import json
from email.mime.text import MIMEText

# Get Data for emailing
with open('../../config.mail.json', 'r') as config:
    data = config.read()
emailData = json.loads(data)
for email in emailData['emailAccount']:
    smtp_server = email['smtp_server']
    port = email['port']
    sender_email = email['sender_email']
    receiver_email = email['receiver_email']
    password = email['password']


def send_email(message='content message'):
    smtpserver = smtplib.SMTP(smtp_server, port)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(sender_email, password)
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'My custom Subject'
    msg['From'] = "Your name <Your email>"
    msg['To'] = receiver_email
    smtpserver.sendmail(sender_email, receiver_email, msg.as_string())
    smtpserver.close()
    print('Mail is sent successfully!!')


cont = """\
<html>
 <head></head>
 <body>
   <p>Hi!<br>
      How are you?<br>
      Here is the <a href="http://www.google.com">link</a> you wanted.
   </p>
 </body>
</html>
"""
try:
    send_email(message=cont)
except:
    print('Mail could not be sent')