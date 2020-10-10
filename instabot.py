from InstagramAPI import InstagramAPI
from time import sleep
from random import randint
from postgreSQL.fetch import fetchFirst
from postgreSQL.delete import deleteUser
import time
import datetime
import json
import smtplib
import ssl
import sys
import logging

errors = 0
counterIterationsTotal = 0
appCounter = 0

# Get Data for emailing
with open('config.mail.json', 'r') as config:
    data = config.read()
emailData = json.loads(data)
for email in emailData['emailAccount']:
    smtp_server = email['smtp_server']
    port = email['port']
    sender_email = email['sender_email']
    receiver_email = email['receiver_email']
    password = email['password']

# Read file vonfig.json and parse data
with open('config.json', 'r') as config:
    data = config.read()
apps = json.loads(data)

# Setting up logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('log/insta_bot.log')
file_formatter = logging.Formatter(
    "{'time':'%(asctime)s', 'level': '%(levelname)s', 'message': '%(message)s'}"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def like_tag_feed(tag, max_likes):
    global likeCounter
    global counterIterationsTotal
    print('# Liking media with hashtag #{}'.format(tag))
    next_max = 1
    next_max_id = ''
    likes = 0
    for n in range(next_max):
        api.getHashtagFeed(tag, next_max_id)
        temp = api.LastJson
        for post in temp["items"]:
            if not post["has_liked"]:
                unformattedTimeStamp = time.time()
                formattedTimeStamp = time.strftime(
                    "%H:%M:%S",
                    time.gmtime(unformattedTimeStamp + 3600 + 3600))
                print('[{}] Running ... Liking {}'.format(
                    formattedTimeStamp, post["pk"]))
                api.like(post["pk"])
                likes += 1
                likeCounter += 1
                counterIterationsTotal += 1
                logging.info('#{} - Photo liked! ... ({})'.format(
                    tag, likeCounter))
                if likes >= max_likes:
                    break
                sleep(randint(3, 22))
        try:
            next_max_id = temp["next_max_id"]
        except Exception:
            pass
        if likes >= max_likes:
            break


def like_recent_media(target_user, max_likes):
    global likeCounter
    global counterIterationsTotal
    print('# Liking media from User {}'.format(target_user))

    def get_user_profile(target_user):
        api.searchUsername(target_user)
        return api.LastJson['user']

    user_profile = get_user_profile(target_user)
    user_id = user_profile['pk']
    user_posts = api.getUserFeed(user_id)
    info = api.LastJson

    likes = 0
    for recent_post in info['items']:
        if not recent_post["has_liked"]:
            unformattedTimeStamp = time.time()
            formattedTimeStamp = time.strftime(
                "%H:%M:%S", time.gmtime(unformattedTimeStamp + 3600 + 3600))
            print('[{}] Running ... Liking {} from {}'.format(
                formattedTimeStamp, recent_post["pk"], target_user))
            api.like(recent_post['pk'])
            likes += 1
            likeCounter += 1
            counterIterationsTotal += 1
            logging.info('{} - Photo #{} liked! ... ({})'.format(
                target_user, recent_post["pk"], likeCounter))
            if likes >= max_likes:
                break
            sleep(randint(3, 22))


def send_email(mailType, detail):

    unformattedDateStamp = datetime.datetime.now()
    formattedDateStamp = unformattedDateStamp.strftime("%d/%m %H:%M")

    if mailType == 0:
        message = f"""\
Subject: {formattedDateStamp}, Instabot ran successfully
Instabot ran successfully with {detail} iterations """
    elif mailType == 1:
        message = f"""\
Subject: Python Error report
There were too many erros when running the instabot script for the account {userAccount} ({formattedDateStamp}) """
    else:
        mailType = f"""\
Subject: All hands on deck! 
Something weird is going on in your python script ({formattedDateStamp})."""

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()


# Go Through al the apps in config.Json
for app in apps:

    if (appCounter == 0):

        # Go though all the accounts
        for account in app['accounts']:

            # Check account Active-status
            if account['active']:

                print('--------------------------------------')
                print('Connection to account {}'.format(account['username']))
                print('--------------------------------------')

                # Reset user Error
                errors = 0

                # For error handling
                userAccount = account['username']

                try:

                    api = InstagramAPI(account['username'],
                                       account['password'])
                    api.login()
                    logging.info('### Connection to account {}'.format(
                        account['username']))
                    sleep(5)

                    # Reset the like counter
                    likeCounter = 0

                    while likeCounter < account['iterations'] + 1:

                        iterationProUser = randint(3, 7)
                        iterationProHashtag = randint(7, 12)

                        targetUserFollower = fetchFirst(
                            account['username'].replace(".", ""))
                        logging.info(
                            'Fetched user {} from postgreSQL table {}'.format(
                                targetUserFollower, account['username']))
                        print('> Fetched user {} from postgreSQL table {}'.
                              format(targetUserFollower, account['username']))

                        try:
                            # Like media from user
                            like_recent_media(targetUserFollower,
                                              iterationProUser)
                            print('likeCounter: {}'.format(likeCounter))
                            # Delete user from list
                            deleteUser(account['username'], targetUserFollower)
                            logging.info(
                                'Deleted user {} from postgreSQL table {}'.
                                format(targetUserFollower,
                                       account['username']))
                            print(
                                '> Deleted user {} from postgreSQL table {}'.
                                format(targetUserFollower,
                                       account['username']))

                            # Like media from hastags array
                            like_tag_feed(
                                account['tags'][randint(
                                    0,
                                    len(account['tags']) - 1)],
                                iterationProHashtag)
                            print('likeCounter: {}'.format(likeCounter))

                            # Wait for few secondes
                            sleep(30)

                        except:

                            errors += 1
                            print('(!) ERROR {}'.format(errors))
                            logging.warning(
                                '(!) ERROR #{} on account {}'.format(
                                    errors, account['username']))

                            # Delete user from list
                            deleteUser(account['username'], targetUserFollower)
                            logging.info(
                                'Deleted user {} from postgreSQL table {}'.
                                format(targetUserFollower,
                                       account['username']))
                            print(
                                '> Deleted user {} from postgreSQL table {}'.
                                format(targetUserFollower,
                                       account['username']))

                            # Break process if too much User Errors at once
                            if errors >= 20:
                                send_email(1, userAccount)
                                logging.critical(
                                    '10 ERROR on account {}. Account will be dropped for now.'
                                    .format(account['username']))
                                break
                            else:
                                continue

                except:

                    print(
                        f'Some unhandled error happened for account {userAccount} !'
                    )
                    continue

    else:
        break

    appCounter = appCounter + 1

# Inform that the script ended.
send_email(0, counterIterationsTotal)
logging.info(
    'SCRIPT RAN SUCCESSFULLY ({} iterations)'.format(counterIterationsTotal))

print('------------------------')
print('SCRIPT RAN SUCCESSFULLY')
print('------------------------')
