import smtplib
import ssl
import json
from decouple import config


smtp_server = config('SMTP_SERVER_GMAIL')
port = config('PORT_GMAIL')
sender_email = config('EMAIL_GMAIL')
receiver_email = config('EMAIL_GMAIL')
password = config('PWD_GMAIL')

message = """\
Subject: Hi there
This message is sent from Python."""

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server, port)
    server.starttls(context=context)  # Secure the connection
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()
