from InstagramAPI import InstagramAPI
from time import sleep
from random import randint
from decouple import config
from helpers.getDateTime import getDateTime
from helpers.getDateTime import getHourTime
from helpers.getDateTime import diffTime
import datetime as datetime
import logging
import sys


# When the script started
startTime = getHourTime()

# Setting up logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("log/insta_bot.log")
file_formatter = logging.Formatter(
    "{'time':'%(asctime)s', 'level': '%(levelname)s', 'message': '%(message)s'},"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def like_tag_feed(tag, max_likes):
    global likeCounter
    global counterIterationsTotal
    global fourHundredCounter

    print("> Liking media with hashtag #{}".format(tag))
    logging.info("> Liking media with hashtag #{}".format(tag))

    next_max = 1
    next_max_id = ""
    likes = 0

    for n in range(next_max):
        api.getHashtagFeed(tag, next_max_id)
        temp = api.LastJson
        for post in temp["items"]:
            if not post["has_liked"]:
                # Get a TimeStamp
                formattedTimeStamp = getDateTime()
                print(
                    "[{}] Running ... Liking {}".format(formattedTimeStamp, post["pk"])
                )
                result = api.like(post["pk"])
                counterIterationsTotal += 1
                if result == False:
                    logging.critical(f"Api return error 400 for tag {tag}")
                    print(f"Api return error 400 for tag {tag}")
                    return False
                if result == True:
                    fourHundredCounter = 0
                likes += 1
                likeCounter += 1
                logging.info("#{} - Photo liked! ... ({})".format(tag, likeCounter))
                if likes >= max_likes:
                    return True
                sleep(randint(3, 17))
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

    print("> Liking media from User {}".format(target_user))
    logging.info("> Liking media from User {}".format(target_user))

    def get_user_profile(target_user):
        api.searchUsername(target_user)
        return api.LastJson["user"]

    user_profile = get_user_profile(target_user)
    user_id = user_profile["pk"]
    user_posts = api.getUserFeed(user_id)
    info = api.LastJson
    likes = 0

    for recent_post in info["items"]:
        if not recent_post["has_liked"]:
            # Get a TimeStamp
            formattedTimeStamp = getDateTime()
            print(
                "[{}] Running ... Liking {} from {}".format(
                    formattedTimeStamp, recent_post["pk"], target_user
                )
            )
            result = api.like(recent_post["pk"])
            counterIterationsTotal += 1

            if result == False:
                logging.critical(f"Api return error 400 for user {target_user}")
                print(f"Api return error 400 for user {target_user}")
                return False
            if result == True:
                fourHundredCounter = 0
            likes += 1
            likeCounter += 1
            logging.info(
                "{} - Photo #{} liked! ... ({})".format(
                    target_user, recent_post["pk"], likeCounter
                )
            )
            if likes >= max_likes:
                return True
            sleep(randint(3, 17))


# Data User
userList = "localBot_users.txt"
accountName = "vinticiousberlin"
accountPassword = config("VINTICIOUSBERLIN_PWD")
counterIterationsTotal = 0
maxIterations = 300
likeCounter = 0
errors = 0

# Start
print("--------------------------------------")
print("Connection to account {}".format(accountName))
print("--------------------------------------")

try:

    api = InstagramAPI(accountName, accountPassword)
    resultLogin = api.login()
    # Error when connecting
    if not resultLogin:
        print("###  Connection Error")
    logging.info("### Connection to account {}".format(accountName))

    sleep(5)

    while likeCounter < maxIterations + 1:

        iterationProUser = randint(2, 4)
        iterationProHashtag = randint(7, 12)

        file = open(userList)
        targetUserFollower = file.readline().rstrip()
        file.close()

        try:
            # Like media from user
            result = like_recent_media(targetUserFollower, iterationProUser)
            print("likeCounter: {}".format(likeCounter))

            if result == False:
                errors += 1

            # check if we already maxed up the iteration threshold
            if likeCounter > maxIterations - 1:
                break

            # Delete user from list
            with open(userList,'r') as readFile:
                lines = readFile.readlines()

            # delete matching content
            with open(userList, 'w') as writefile:
                for line in lines:
                    # readlines() includes a newline character
                    if line.strip("\n") != targetUserFollower:
                        writefile.write(line)

        except Exception as e:

            print("E: {}".format(e))

            if e is "'items'":
                # Not authorized to view user
                print("Not authorized to view user")
            else :
                print("something else")
                print(e)
                #sys.exit()

            # if e == 'item':
                # 
            # if e == "user":
                # You've Been Logged Out
            # if e == "Not logged in!":
                # You are obvioulsy not log in

        
        # Delete user from list
        with open(userList, "r") as readFile:
            lines = readFile.readlines()

        # delete matching content
        with open(userList, "w") as writefile:
            for line in lines:
                # readlines() includes a newline character
                if line.strip("\n") != targetUserFollower:
                    writefile.write(line)

        # Wait for few secondes
        sleep(randint(5, 45))

except:

    print(f"Some error happened for account {accountName} !")

# Inform that the script ended.
logging.info("Script ran with ({} iterations)".format(counterIterationsTotal))

print("------------------------")
print("SCRIPT ENDED")
print("------------------------")
