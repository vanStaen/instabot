from InstagramAPI import InstagramAPI
from time import sleep
from random import randint

instauser = 'clementvanstaen'
instapass = 'kftv2h4insta'

api = InstagramAPI(instauser, instapass)
api.login()

sleep(30)