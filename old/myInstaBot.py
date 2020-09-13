from selenium import webdriver
from time import sleep
from random import randint
import time

likes = 0
fromDirectory = "followersOf"

#Account, Password, Active
accounts = [["miralykkeofficial", "2mjett", False], \
            ["clementvanstaen", "kftv2h4CVS", True], \
            ["deuxfrancs", "kftv2h4insta", False], \
            ["vanstaenmusic", "kftv2h4insta", True], \
            ["purzelbaumrecords", "kftv2h4insta", True]]

#Hastags and Users
#hashtag_list = ['kitkatclub', 'berlintechno', 'deephouseberlin', 'katerblau', 'watergaterecords']#
hashtag_list = []
user_list = ['rauschhausmusic', 'berlinhousemusic', 'cerclemusic', 'lovra']

#Webdriver
chromedriver_path = '/chromedriver'
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)

#Go though all the accounts

for account in accounts:

    if account[2] == True :

        #Debugging: Print account name
        print('--------------------------------------')
        print('Connection to account {}'.format(account[0]))
        print('--------------------------------------')

        #Login
        webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        sleep(3)
        username = webdriver.find_element_by_name('username')
        username.send_keys(account[0])
        password = webdriver.find_element_by_name('password')
        password.send_keys(account[1])
        button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button')
        button_login.click()
        sleep(3)

        #Click the popup
        notnow = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
        notnow.click()

        #Go though hashtag
        tag = -1

        for hashtag in hashtag_list:

            print('###########################')
            print('Hashtag: {}'.format(hashtag))
            print('###########################')

            tag += 1
            webdriver.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')
            sleep(5)

            # Click the first thumbnail to land in the "navigable" windows
            first_thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
            first_thumbnail.click()
            sleep(randint(1,2))

            try:

                # 500 iterations pro Hashtag
                for x in range(1,500):

                    #Track in Terminal
                    unformattedTimeStamp = time.time()
                    formattedTimeStamp = time.strftime("%H:%M:%S", time.gmtime(unformattedTimeStamp + 3600))
                    print('[{}] Running ... {}'.format(formattedTimeStamp, x))

                    try:
                        # Liking the picture
                        button_like = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button/span')
                        button_like.click()
                        likes += 1
                        sleep(randint(22,32))

                        # Next picture (careful, here in german)
                        webdriver.find_element_by_link_text('Weiter').click()
                        sleep(randint(25,32))

                    except:

                        # Next picture (careful, german)
                        webdriver.find_element_by_link_text('Weiter').click()
                        sleep(randint(25,32))

                        # In case liking throw an error
                        # it continues to the next pictures
                        continue


            # In case hashtag stops refreshing photos
            # Or if reached the last picture, it continues to the next hastag
            except:

                continue

        #Go though TargetUsers
        for user in user_list:

            print('###########################')
            print('User: {}'.format(user))
            print('###########################')

            try:

                targetUserFollowers = open("followersOf/"+ user + ".txt","r")

                with targetUserFollowers as file:

                    for profile in file:

                        try:
                            webdriver.get('https://www.instagram.com/' + profile + '/')
                            sleep(5)

                            # Click the first thumbnail to land in the "navigable" windows
                            first_thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
                            first_thumbnail.click()
                            sleep(randint(1,2))

                            # 5 Iterations pro followers
                            for x in range(1,5):

                                #Track in Terminal
                                unformattedTimeStamp = time.time()
                                formattedTimeStamp = time.strftime("%H:%M:%S", time.gmtime(unformattedTimeStamp + 3600))
                                print('[{}] Running ... {} from {}, like {}'.format(formattedTimeStamp,profile,user,x))

                                try:

                                    for randNext in range(1, randint(1, 5)):

                                        # Liking the picture
                                        button_like = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button/span')
                                        button_like.click()
                                        likes += 1
                                        sleep(randint(22,32))

                                    # Next picture (careful, here in german)
                                    webdriver.find_element_by_link_text('Weiter').click()
                                    sleep(randint(25,32))

                                # On Error, or if last pictures is reached.
                                except:

                                    continue

                        # In case Account is private
                        except:

                            continue

                targetUserFollowers.close()

            # On Error
            except:

                continue

        #Print results
        print('Liked {} photos.'.format(likes))
