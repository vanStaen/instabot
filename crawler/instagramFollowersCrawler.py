# Get instance
# if needed : sudo pip3 install instaloader
# run it with : python3 instagramFollowersCrawler.py
import instaloader
from decouple import config

L = instaloader.Instaloader()

user = "paulsmith"

# Login or load session
L.login("clementvanstaen", config("CLEMENTVANSTAEN_PWD"))

# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, user)

# Save list of followers
file = open("insta_followers_of/" + user + ".txt", "a+")
for follower in profile.get_followers():
    username = follower.username
    file.write(username + "\n")
    print(username)
file.close()
