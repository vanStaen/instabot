import smtplib
import ssl
import json

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


def send_mail(errorType):

    message = """\
Subject: Hi there
This message is sent from Python."""

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
    except Exception as e:
        # Print any error messages to stdout
        print(e)


send_mail(0)