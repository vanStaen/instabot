from InstagramAPI import InstagramAPI
from time import sleep
from random import randint
from decouple import config
from postgreSQL.fetch import fetchFirst
from postgreSQL.fetch import fetchAllAccount
from postgreSQL.delete import deleteUser
from postgreSQL.deactivate import deactivate
from helpers.sendMail import sendMail
import time
import json
import smtplib
import ssl
import sys
import logging

errors = 0
counterIterationsTotal = 0
appCounter = 0
fourHundredCounter = 0

# Setting up logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('log/insta_bot.log')
file_formatter = logging.Formatter(
    "{'time':'%(asctime)s', 'level': '%(levelname)s', 'message': '%(message)s'}"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

# Loading Accounts infos
accounts = fetchAllAccount()
password = {}
for account in accounts:
    password[account[3]] = config(account[3].upper()+'_PWD')


def like_tag_feed(tag, max_likes):
    global likeCounter
    global counterIterationsTotal
    global fourHundredCounter

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
                result = api.like(post['pk'])
                counterIterationsTotal += 1
                if result == False:
                    logging.critical(f"Api return error 400 for tag {tag}")
                    return False
                if result == True:
                    fourHundredCounter = 0
                likes += 1
                likeCounter += 1
                logging.info(
                    '#{} - Photo liked! ... ({})'.format(tag, likeCounter))
                if likes >= max_likes:
                    return True
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
    global fourHundredCounter

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
            result = api.like(recent_post['pk'])
            counterIterationsTotal += 1
            if result == False:
                logging.critical(
                    f"Api return error 400 for user {target_user}")
                return False
            if result == True:
                fourHundredCounter = 0
            likes += 1
            likeCounter += 1
            logging.info(
                '{} - Photo #{} liked! ... ({})'.format(target_user, recent_post["pk"], likeCounter))
            if likes >= max_likes:
                return True
            sleep(randint(3, 22))


# Info mail on script start
print(sendMail(2, ''))

# Go though all the accounts
for account in accounts:

    # Check account Active-status
    if account[0]:

        print('--------------------------------------')
        print('Connection to account {}'.format(account[3]))
        print('--------------------------------------')

        # Reset user Error
        errors = 0
        fourHundredCounter = 0

        # For error handling
        userAccount = account[3]

        try:

            api = InstagramAPI(account[3],
                               password[account[3]])
            api.login()
            logging.info('### Connection to account {}'.format(
                account[3]))
            sleep(5)

            # Reset the like counter
            likeCounter = 0

            while likeCounter < account[1] + 1:

                iterationProUser = randint(3, 7)
                iterationProHashtag = randint(7, 12)

                targetUserFollower = fetchFirst(
                    account[3].replace(".", ""))

                try:
                    # Like media from user
                    result = like_recent_media(targetUserFollower,
                                               iterationProUser)
                    print('likeCounter: {}'.format(likeCounter))

                    if result == False:
                        fourHundredCounter += 1

                    if fourHundredCounter >= 5:
                        deactivate(account[3])
                        print(sendMail(1, userAccount))
                        logging.critical(
                            'Too many 400 Error on account {}. Account will be dropped for now.'.format(account[3]))
                        break

                    # Delete user from list
                    deleteUser(account[3].replace(
                        ".", ""), targetUserFollower)

                    # Like media from hastags array
                    result = like_tag_feed(
                        account[2][randint(
                            0,
                            len(account[2]) - 1)],
                        iterationProHashtag)
                    print('likeCounter: {}'.format(likeCounter))

                    if result == False:
                        fourHundredCounter += 1

                    if fourHundredCounter >= 5:
                        deactivate(account[3])
                        print(sendMail(1, userAccount))
                        logging.critical(
                            'Too many 400 Error on account {}. Account will be dropped for now.'.format(account[3]))
                        break

                    # Wait for few secondes
                    sleep(30)

                except Exception as e:

                    errors += 1
                    print('Error #{} on account {}'.format(
                        errors, account[3]))
                    logging.warning('Error #{} on account {}'.format(
                        errors, account[3]))

                    # Delete user from list
                    deleteUser(account[3].replace(
                        ".", ""), targetUserFollower)

        except:

            print(
                f'Some unhandled error happened for account {userAccount} !'
            )
            continue

        # return numbers of errors
        if errors >= 1:
            logging.critical('{} ERROR on account {}. Account will NOT be dropped.'.format(
                errors, account[3]))


# Inform that the script ended.
print(sendMail(0, counterIterationsTotal))
logging.info(
    'SCRIPT RAN SUCCESSFULLY ({} iterations)'.format(counterIterationsTotal))

print('------------------------')
print('SCRIPT RAN SUCCESSFULLY')
print('------------------------')
