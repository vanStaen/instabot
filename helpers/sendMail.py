import requests
import json
from email.mime.text import MIMEText
from decouple import config
from helpers.getDateTime import getDateTime


def sendMail(mailType, detail, iteration, runTime):

    formattedDateStamp = getDateTime()

    if mailType == 0:
        messageSubject = f"{formattedDateStamp}, Instabot ran successfully."
        messageBody = f"Instabot ran successfully with {iteration} iterations.<br/> Runtime of the script : {runTime}<br/>"
        messageBody = messageBody + "<ol>"
        for data in detail:
            if detail[data]["connectionError"]:
                messageBody = (
                    messageBody
                    + f"<li>Error on connection with account <b>'{detail[data]['name']}'</b>.</li>"
                )
            elif not detail[data]["active"]:
                messageBody = (
                    messageBody
                    + f"<li>Account <b>{detail[data]['name']}</b><ul><li>is deactivated.</li></ul></li>"
                )
            elif not detail[data]["run"]:
                messageBody = (
                    messageBody
                    + f"<li>Account <b>{detail[data]['name']}</b><ul><li>did not run.</li></ul></li>"
                )
            else:
                messageBody = (
                    messageBody
                    + f"<li>Account <b>{detail[data]['name']}</b><ul><li>ran {detail[data]['iterations']} iterations of {detail[data]['iterationMax']} max.</li><li>generated {detail[data]['errors']} errors.</li><li>{detail[data]['databaseUser']} username remaining.</li></ul></li>"
                )
        messageBody = messageBody + "</ol>"
    elif mailType == 1:
        messageSubject = f"Account '{detail}' is now deactivated"
        messageBody = f"There were too many errors when running the instabot script for the account <b>{detail}</b>. The account will be deactivated."
    elif mailType == 2:
        messageSubject = f"{formattedDateStamp}, Instabot script started."
        messageBody = "Instabot started running"
    elif mailType == 3:
        messageSubject = f"All accounts have been updated!"
        messageBody = f"The Weekly account update was <b>successful</b>.<br/> Run time of the script : {runTime}.<br/>"
        messageBody = messageBody + "<ol>"
        for data in detail:
            if detail[data]["alive"]:
                messageBody = (
                    messageBody
                    + f"<li><b>{detail[data]['name']}</b> active with :<ul><li>Iterations max pro run: {detail[data]['iterationMax']}</li><li>Hashtags: {str(detail[data]['tags'])[1:-1]}.</li><li>{detail[data]['usernameLeft']} users remaining.</li></li>"
                )
            else:
                messageBody = (
                    messageBody
                    + f"<li>Deactivated! <b>{detail[data]['name']}</b><ul><li>Iterations max pro run: {detail[data]['iterationMax']}</li><li>Hashtags: {str(detail[data]['tags'])[1:-1]}.</li><li>{detail[data]['usernameLeft']} users remaining.</li></li>"
                )
        messageBody = messageBody + "</ol>"
    elif mailType == 4:
        messageSubject = f"[Warning] Add some more user to account {detail}"
        messageBody = f"Accout {detail} has less than {iteration} usernames left in the date base. You may want to add some more."
    elif mailType == 5:
        messageSubject = f"Not running today!"
        messageBody = f"The bot is not running today!"
    else:
        messageSubject = "Subject: All hands on deck!"
        messageBody = (
            f"Something weird is going on in your python script ({formattedDateStamp})."
        )

    # Make http resquest to Mailman service
    try:
        receiver_email = config("EMAIL_GMAIL")
        url = "https://mailman-cvs.herokuapp.com/api/instabot"
        data = {
            "from": "instabot <info@clementvanstaen.com>",
            "to": receiver_email,
            "subject": messageSubject,
            "body": messageBody,
            "key": config("MAILMAN_KEY"),
        }

        headers = {"Content-type": "application/json", "Accept": "text/plain"}
        request = requests.post(url, data=json.dumps(data), headers=headers)
        # print(request.text)

        return f"Message sent to {receiver_email}!"

    except Exception as e:

        # Print any error messages to stdout
        return e
