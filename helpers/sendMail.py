import smtplib
import ssl
import json
import datetime
from decouple import config
from email.mime.text import MIMEText
from helpers.getDateTime import getDateTime


def sendMail(mailType, detail, iteration, runTime):

    formattedDateStamp = getDateTime()

    if mailType == 0:
        messageSubject = f"{formattedDateStamp}, Instabot ran successfully."
        messageBody = f"Instabot ran successfully with {iteration} iterations.<br/> Runtime of the script : {runTime}<br/>"
        messageBody = messageBody + "<ol>"
        for data in detail:
            if detail[data]['connectionError']:
                messageBody = messageBody + \
                    f"<li>Error on connection with account <b>'{detail[data]['name']}'</b>.</li>"
            elif not detail[data]['active']:
                messageBody = messageBody + \
                    f"<li>Account <b>'{detail[data]['name']}'</b> is deactivated.</li>"
            elif not detail[data]['run']:
                messageBody = messageBody + \
                    f"<li>Account <b>'{detail[data]['name']}'</b> did not run.</li>"
            else:
                messageBody = messageBody + \
                    f"<li>Account <b>{detail[data]['name']}</b><ul><li>ran {detail[data]['iterations']} iterations of {detail[data]['iterationMax']} max.</li><li>generated {detail[data]['errors']} errors.</li><li>{detail[data]['databaseUser']} username remaining.</li></li>"
        messageBody = messageBody + "</ol>"
    elif mailType == 1:
        messageSubject = "Python Error report."
        messageBody = f"There were too many errors when running the instabot script for the account <b>{detail}</b>. The account will be deactivated."
    elif mailType == 2:
        messageSubject = f"{formattedDateStamp}, Instabot script started."
        messageBody = "Instabot started running"
    elif mailType == 3:
        messageSubject = f"All accounts have been updated!"
        messageBody = f"The Weekly account update was <b>successfull</b>.<br/> Run time of the script : {runTime}.<br/>"
        messageBody = messageBody + "<ol>"
        for data in detail:
            if detail[data]['alive']:
                messageBody = messageBody + \
                    f"<li><b>{detail[data]['name']}</b> active with :<ul><li>Iterations max pro run: {detail[data]['iterationMax']}</li><li>Hashtags: {str(detail[data]['tags'])[1:-1]}.</li><li>{detail[data]['usernameLeft']} users remaining.</li></li>"
            else:
                messageBody = messageBody + \
                    f"<li><b>Deactivated!</b> {detail[data]['name']}<ul><li>Iterations max pro run: {detail[data]['iterationMax']}</li><li>Hashtags: {str(detail[data]['tags'])[1:-1]}.</li><li>{detail[data]['usernameLeft']} users remaining.</li></li>"
        messageBody = messageBody + "</ol>"
    elif mailType == 4:
        messageSubject = f"[Warning] Add some more user to account {detail}"
        messageBody = f"Accout {detail} has less than {iteration} usernames left in the date base. You may want to add some more."
    else:
        messageSubject = "Subject: All hands on deck!"
        messageBody = f"Something weird is going on in your python script ({formattedDateStamp})."

    smtp_server = config('SENDINBLUE_SMTP')
    port = config('SENDINBLUE_PORT')
    sender_email = config('EMAIL_GMAIL')
    receiver_email = 'info@clementvanstaen.com'
    password = config('SENDINBLUE_PWD')

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:

        msg = MIMEText(messageBody, 'html')
        msg['Subject'] = messageSubject
        msg['From'] = "Instabot <info@clementvanstaen.com>"
        msg['To'] = receiver_email
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)  # Secure the connection
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        return f"Message sent to {receiver_email}!"

    except Exception as e:

        # Print any error messages to stdout
        return e

    finally:

        server.quit()

    # Create a secure SSL context
    context = ssl.create_default_context()
