from selenium import webdriver
from time import sleep

# Webdriver
chromedriver_path = '../ressources/chromedriver'
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)

webdriver.get('https://www.instagram.com/clementvanstaen/')

images = webdriver.find_elements_by_class_name("_bz0w")
image_curr = images[0].find_element_by_tag_name("a").get_attribute("href")
webdriver.get(image_curr)