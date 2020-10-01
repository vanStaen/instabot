from InstagramAPI import InstagramAPI
from time import sleep
from random import randint
import time, datetime
import json
import smtplib
import ssl
import sys

userErrors = 0
iterationProUser = 5
iterationProHashtag = 10
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
message = """\
Subject: Python Error report
Error when running Python script"""

# Read file vonfig.json and parse data
with open('config.json', 'r') as config:
    data = config.read()
apps = json.loads(data)


def logAction(data):
    unformattedDateStamp = datetime.datetime.now()
    formattedDateStamp = unformattedDateStamp.strftime("%Y-%m-%d %H:%M:%S")
    file = open("log/log_instagram.txt", "a+")
    file.write("[" + formattedDateStamp + "] " + data + "\n")
    file.close()


def like_tag_feed(tag, max_likes):
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
                logAction('#{} - Photo liked! ... ({})'.format(
                    tag, likeCounter + likes))
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
            try:
                api.like(recent_post['pk'])
            except Exception as e:
                if (e.status_code == 400):
                    print(">>> This is an Error 400")
                    print(e)
                else:
                    print(">>> This is not an Error 400")
                    print(e)
                sys.exit("/!\ It came this far ... ")
                pass
            likes += 1
            logAction('{} - Photo #{} liked! ... ({})'.format(
                target_user, recent_post["pk"], likeCounter + likes))
            if likes >= max_likes:
                break
            sleep(randint(3, 22))


def send_email_on_error(errorType):
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

                try:
                    api = InstagramAPI(account['username'],
                                       account['password'])
                    api.login()
                    logAction('### Connection to account {}'.format(
                        account['username']))
                    sleep(5)

                    # Reset some variables
                    likeCounter = 0

                    # Go though TargetUsers
                    targetUserFollowers = open(
                        "userlist_instagram/username_{}.txt".format(
                            account['username']), "r")

                    with targetUserFollowers as file:

                        for profile in file:

                            if likeCounter >= account['iterations']:

                                #Break for statement, to switch insta account
                                break

                            try:
                                # Like media from user
                                like_recent_media(profile[:-1],
                                                  iterationProUser)
                                likeCounter += iterationProUser
                                print('likeCounter: {}'.format(likeCounter))
                                # Delete user from list
                                with open(
                                        "userlist_instagram/username_{}.txt".
                                        format(account['username']),
                                        "r") as file:
                                    lines = file.readlines()
                                with open(
                                        "userlist_instagram/username_{}.txt".
                                        format(account['username']),
                                        "w") as file:
                                    for line in lines:
                                        if line.strip("\n") != profile[:-1]:
                                            file.write(line)

                                #Reset user Error
                                userErrors = 0

                                # Like media from hastags array
                                like_tag_feed(
                                    account['tags'][randint(
                                        0,
                                        len(account['tags']) - 1)],
                                    iterationProHashtag)
                                likeCounter += iterationProHashtag
                                print('likeCounter: {}'.format(likeCounter))

                                # Wait for few secondes
                                sleep(30)

                            except:

                                userErrors += 1
                                print('USER ERROR {}'.format(userErrors))

                                # Delete user from list
                                with open(
                                        "userlist_instagram/username_{}.txt".
                                        format(account['username']),
                                        "r") as file:
                                    lines = file.readlines()
                                with open(
                                        "userlist_instagram/username_{}.txt".
                                        format(account['username']),
                                        "w") as file:
                                    for line in lines:
                                        if line.strip("\n") != profile[:-1]:
                                            file.write(line)

                                # Break process if too much User Errors at once
                                if userErrors >= 5:
                                    break
                                else:
                                    continue

                except:

                    print('LOGIN ERROR')
                    continue

    else:
        break

    appCounter = appCounter + 1

# Inform that the script ended.
print('------------------------')
print('SCRIPT RAN SUCCESSFULLY')
print('------------------------')