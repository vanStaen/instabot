from selenium import webdriver
from time import sleep

# Webdriver
chromedriver_path = 'chromedriver'
#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--incognito")
#driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=chrome_options)
driver = webdriver.Chrome(executable_path=chromedriver_path)
#driver.maximize_window()
sleep(2)

users = ["liegewiesemorgentau", "swsvn", "escapismmusique", "into-lala", "cotumo", "cosmovitali", "meeresrausch"]

# Go though all the accounts
for user in users:

    # Open profile user
    driver.get('https://www.soundcloud.com/' + user + '/followers')

    # in chromedriver scroll down
    SCROLL_PAUSE_TIME = 1
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    #  iterations of the Bot
    for x in range(1, 10000):

        try:
            follower = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/div/div/ul/li['+str(x+1)+']/div/div[2]')
            result_inner = (follower.get_attribute('innerHTML'))
            result_username = result_inner.split('"')[1][1:]
            # Save in list of followers
            file = open("ressources/soundcloud_followers_of/"+ user +".txt","a+")
            file.write(result_username + "\n")
            print(result_username)
            file.close()

        except:
            break