import smtplib
import ssl
import json
import datetime
from decouple import config
from email.mime.text import MIMEText
from helpers.getDateTime import getDateTime


def sendMail(mailType, detail, counterIterationsTotal):

    formattedDateStamp = getDateTime()

    if mailType == 0:
        messageSubject = f"{formattedDateStamp}, Instabot ran successfully."
        messageBody = f"Instabot ran successfully with {counterIterationsTotal} iterations.<br/>"
        messageBody = messageBody + "<ol>"
        for data in detail:
            if detail[data]['connectionError']:
                messageBody = messageBody + \
                    f"<li>Error on connection with account <b>'{detail[data]['name']}'</b>.</li>"
            elif detail[data]['active']:
                messageBody = messageBody + \
                    f"<li><b>{detail[data]['name']}</b><ul><li>ran {detail[data]['iterations']} iterations</li><li>generated {detail[data]['errors']} errors.</li><li>{detail[data]['databaseUser']} username remaining.</li></li>"
            else:
                messageBody = messageBody + \
                    f"<li>Account <b>'{detail[data]['name']}'</b> is deactivated.</li>"
        messageBody = messageBody + "</ol>"
    elif mailType == 1:
        messageSubject = "Python Error report."
        messageBody = f"There were too many errors when running the instabot script for the account <b>{detail}</b>. The account will be deactivated."
    elif mailType == 2:
        messageSubject = f"{formattedDateStamp}, Instabot script started."
        messageBody = "Instabot started running"
    elif mailType == 3:
        messageSubject = f"[Weekly Account update]"
        messageBody = f"The Weekly account update was successfull."
    else:
        messageSubject = "Subject: All hands on deck!"
        messageBody = f"Something weird is going on in your python script ({formattedDateStamp})."

    smtp_server = config('SMTP_SERVER_GMAIL')
    port = config('PORT_GMAIL')
    sender_email = config('EMAIL_GMAIL')
    receiver_email = config('EMAIL_GMAIL')
    password = config('PWD_GMAIL')

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:

        msg = MIMEText(messageBody, 'html')
        msg['Subject'] = messageSubject
        msg['From'] = "Instabot <clement.vanstaen@gmail.com>"
        msg['To'] = receiver_email
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)  # Secure the connection
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        return f"Message sent!"

    except Exception as e:

        # Print any error messages to stdout
        return e

    finally:

        server.quit()

    # Create a secure SSL context
    context = ssl.create_default_context()
