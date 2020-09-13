from selenium import webdriver
from time import sleep
import datetime
from selenium.webdriver.common.by import By
import random

unformattedDateStamp = datetime.datetime.now()
formattedDateStamp = unformattedDateStamp.strftime("%Y-%m-%d")

# Account, eMail, Password, Active, Iteration
accounts = [
    ["purzelbaumrecords", "info@purzelbaumrecords.com", "", True, 50],
    ["vanstaenmusic", "clement.vanstaen@gmail.com", "", True, 50],
    ["miralykke", "info@miralykke.com", "", True, 30]
]

chromedriver_path = 'ressources/chromedriver'


def logAction(data):

    file = open("log/log_soundcloud.txt", "a+")
    file.write("[" + formattedDateStamp + "] " + data + "\n")
    file.close()


def login(login, pwd):
    # Open Soundcloud Community
    driver.get('https://community.soundcloud.com/')
    sleep(random.randint(3, 4))
    # Open Login form
    button_login = driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/nav/div/section[2]/ul/li[2]/a')
    button_login.click()
    sleep(1)
    # Add mail to form
    access_form = driver.find_element_by_id('username')
    access_form.send_keys(login)
    sleep(0.5)
    # Add Password
    password_form = driver.find_element_by_id('password')
    password_form.send_keys(pwd)
    sleep(0.5)
    # Waiting until Captcha are manually done
    msg = 'Did you fix the capcha for {}?'.format(login)
    shall = input("%s (y/N) " % msg).lower() == 'y'
    # Click Continue
    button_signin = driver.find_element_by_id('submit_signin')
    button_signin.click()
    sleep(0.5)


def login2(login, pwd):
    # Open Soundcloud
    driver.get('https://www.soundcloud.com/')
    sleep(random.randint(3, 5))
    # Open Login form
    button_login = driver.find_element_by_xpath(
        '//*[@id="content"]/div/div/div[1]/div/div[2]/button[1]')
    button_login.click()
    sleep(random.randint(1, 5))
    # Select Frame
    login_frame = driver.find_elements(By.TAG_NAME, "iframe")
    driver.switch_to.frame(login_frame[0])
    # Add mail to form
    access_form = driver.find_element_by_id('sign_in_up_email')
    access_form.send_keys(login)
    sleep(random.randint(1, 5))
    # Click Continue
    button_signin = driver.find_element_by_id('sign_in_up_submit')
    button_signin.click()
    sleep(random.randint(1, 5))
    # Add Password
    password_form = driver.find_element_by_id('enter_password_field')
    password_form.send_keys(pwd)
    sleep(random.randint(1, 5))
    # Click Continue
    button_signin = driver.find_element_by_id('enter_password_submit')
    button_signin.click()


def follow(account, user, followCounter):
    driver.get('https://www.soundcloud.com/' + user)
    sleep(2)
    # click follow
    button_follow = driver.find_element_by_xpath(
        '//*[@id="content"]/div/div[3]/div/div[2]/div/button[1]')
    button_follow_text = (button_follow.get_attribute('innerHTML'))
    if button_follow_text == 'Folgen' or button_follow_text == 'Follow':
        button_follow.click()
    # Login
    logAction('{} followed! ... ({})'.format(user, followCounter))
    # Add to Unfollow list
    file = open("userlist_soundcloud/followed_" + account + ".txt", "a+")
    file.write("[" + formattedDateStamp + "] " + user + "\n")
    file.close()


def unfollow(account, user, unfollowCounter):
    driver.get('https://www.soundcloud.com/' + user)
    sleep(2)
    # click follow
    button_unfollow = driver.find_element_by_xpath(
        '//*[@id="content"]/div/div[3]/div/div[2]/div/button[1]')
    button_unfollow_text = (button_unfollow.get_attribute('innerHTML'))
    if button_unfollow_text == 'Folge ich' or button_unfollow_text == 'Following':
        button_unfollow.click()
    # Login
    logAction('{} unfollowed! ... ({})'.format(user, unfollowCounter))
    # Delete from unfollow list
    #file = open("userlist_soundcloud/followed_"+ account +".txt","a+")
    #file.write("[" + formattedDateStamp + "] " + user + "\n")
    # file.close()


# Go though all the accounts
for account in accounts:

    # Check account Active-status
    if account[3]:

        print('--------------------------------------')
        print('Connection to account {}'.format(account[0]))
        print('--------------------------------------')

        # Open WebDriver
        driver = webdriver.Chrome(executable_path=chromedriver_path)
        sleep(1)

        # Login to account
        login(account[0], account[2])
        logAction('### Connection to account {}'.format(account[0]))
        sleep(1)

        # Reset some variables
        followCounter = 1

        # Go though TargetUsers
        targetUserFollowers = open(
            "userlist_soundcloud/username_{}.txt".format(account[0]), "r")

        with targetUserFollowers as file:

            for profile in file:

                if followCounter >= account[4]:

                    # Break for statement, to switch account
                    driver.quit()
                    break

                try:

                    # Follow User
                    follow(account[0], profile[:-1], followCounter)
                    print('{} followed ... ({})'.format(
                        profile[:-1], followCounter))
                    followCounter = followCounter+1

                    # Delete user from list
                    with open("userlist_soundcloud/username_{}.txt".format(account[0]), "r") as file:
                        lines = file.readlines()
                    with open("userlist_soundcloud/username_{}.txt".format(account[0]), "w") as file:
                        for line in lines:
                            if line.strip("\n") != profile[:-1]:
                                file.write(line)

                    # Reset user Error
                    userErrors = 0

                    # Wait for few secondes
                    sleep(random.randint(0, 4))

                except:

                    userErrors += 1

                    # Break process if too much User Errors at once
                    if userErrors >= 3:
                        break
                    else:
                        continue


# Inform that the script ended.
# I am pretty sure that I will never see this.
print('------------------------')
print('SCRIPT RAN SUCCESSFULLY')
print('------------------------')
