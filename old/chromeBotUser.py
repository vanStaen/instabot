from selenium import webdriver
from time import sleep
from random import randint
import random
import time

def logAction(data):
    unformattedTimeStamp = time.time()
    formattedTimeStamp = time.strftime("%H:%M:%S", time.gmtime(unformattedTimeStamp + 3600))
    file = open("../log/log_instagram.txt", "a+")
    file.write("[" +formattedTimeStamp + "] " + data + "\n")
    file.close()

# How often the full script should run
iterationScript = 500
# How many Like pro User
iterationProUser = 5
# Extra time to connect
timeToConnect = 3

# Account, Password, Active
accounts = [["miralykkeofficial", "2mjett", False],
            ["clementvanstaen", "kftv2h4insta", False],
            ["deuxfrancs", "kftv2h4INSTA", True],
            ["vanstaenmusic", "kftv2h4insta", False],
            ["purzelbaumrecords", "kftv2h4insta", False]]


# 500 iterations of the Bot
for x in range(1, iterationScript):

    # Go though all the accounts
    for account in accounts:

        if account[2] == True :

            try:
                # Open Web Browser
                chromedriver_path = '../ressources/chromedriver'
                webdriver = webdriver.Chrome(executable_path=chromedriver_path)
                sleep(2)

                # Debugging: Print account name
                print('--------------------------------------')
                print('Connection to account {}'.format(account[0]))
                print('--------------------------------------')
                logAction('### Connection to account {}'.format(account[0]))

                try:

                    # Login
                    webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
                    sleep(3)
                    username = webdriver.find_element_by_name('username')
                    username.send_keys(account[0])
                    password = webdriver.find_element_by_name('password')
                    password.send_keys(account[1])
                    button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button')
                    button_login.click()
                    sleep(3)

                    # Give me extra time to connect
                    for y in range(1, timeToConnect + 1 ):
                        countdown = timeToConnect + 1 - y
                        print('>' * countdown + ' still {} sec to connect'.format(countdown))
                        sleep(1)

                    # Click the popup
                    notnow = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
                    notnow.click()

                    # Reset likeCounter
                    likeCounter = 0

                    # Go though TargetUsers
                    targetUserFollowers = open("username_{}.txt".format(account[0]),"r")

                    with targetUserFollowers as file:

                        for profile in file:

                            print('###########################')
                            print('User: {}'.format(profile[:-1]))
                            print('###########################')
                            sleep(3)

                            # If account has liked more than 50 time, go to next
                            if likeCounter >= 50 :

                                break

                            # Generate a list of random int (user post to be liked)
                            postToBeLiked = random.sample(range(17), iterationProUser)
                            print(postToBeLiked)
                            sleep(2)

                            # 5 Iterations pro followers
                            for x in range(0,iterationProUser):

                                #Track in Terminal
                                unformattedTimeStamp = time.time()
                                formattedTimeStamp = time.strftime("%H:%M:%S", time.gmtime(unformattedTimeStamp + 3600))
                                print('[{}] Running ... {}'.format(formattedTimeStamp,profile[:-1]))

                                try:

                                    # Open Instagram profile
                                    webdriver.get('https://www.instagram.com/' + profile[:-1] + '/')
                                    sleep(randint(1,2)) #12-22

                                    # Open thumbnail {n} to land in the "navigable" windows
                                    images = webdriver.find_elements_by_class_name("_bz0w")
                                    image_curr = images[postToBeLiked[x]].find_element_by_tag_name("a").get_attribute("href")
                                    webdriver.get(image_curr)
                                    sleep(randint(4,5)) #25-35

                                    # Like the picture
                                    button_like = webdriver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/article/div[2]/section[1]/span[1]/button/span')
                                    button_like.click()
                                    likeCounter += 1

                                    # Track in Terminal
                                    unformattedTimeStamp = time.time()
                                    formattedTimeStamp = time.strftime("%H:%M:%S", time.gmtime(unformattedTimeStamp + 3600))
                                    print('[{}] Running ... Photo #{} liked!'.format(formattedTimeStamp,postToBeLiked[x]))
                                    logAction('{} - Photo #{} liked! ... ({})'.format(profile[:-1],postToBeLiked[x],likeCounter))
                                    sleep(randint(2,3)) #28-38

                                # On Error, or if last pictures is reached.
                                # Or In case Account is private
                                except:

                                    print('ERROR: Liking picture failed')
                                    sleep(3)

                                    continue

                            # Delete the Profile from the txt list file
                            with open("username_{}.txt".format(account[0]),"r") as readFile:
                                lines = readFile.readlines()
                            with open("username_{}.txt".format(account[0]),"w") as writeFile:
                                for line in lines:
                                    if line.strip("\n") != profile[:-1]:
                                        writeFile.write(line)
                            logAction("{} deleted!".format(profile[:-1]))

                    # Close Username file
                    targetUserFollowers.close()

                # ERROR Connection to the profile
                except:

                    # Track error in Terminal
                    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
                    print('ERROR with profile {}'.format(account[0]))
                    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

                    # Deactivate Account
                    account[2] = False

                    # Resume Script
                    continue

                # Close the Browser window
                webdriver.close()

            except:

                # Track error in Terminal
                print('%%%%%%%%%%%%%%%%%%%%%%%%%%%')
                print('ERROR with Chrome WebDriver')
                print('%%%%%%%%%%%%%%%%%%%%%%%%%%%')

                break

    # between every iteration
    print('-------------------------------')
    print('ITERATION  {} OF {} FINISHED'.format(x-1, iterationScript))
    print('-------------------------------')
    # Sleep a little
    sleep(3600)

# Inform that the script ended.
# I am pretty sure that I will never see this.
print('------------------------')
print('SCRIPT RAN SUCCESSFULLY')
print('------------------------')