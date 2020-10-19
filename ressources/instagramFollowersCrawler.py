# Get instance
# if needed : sudo pip3 install instaloader
import instaloader
L = instaloader.Instaloader()

user = "real_missbanana1"

# Login or load session
L.login("clementvanstaen", "kftv2h4insta")

# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, user)

# Save list of followers
file = open("insta_followers_of/" + user + ".txt", "a+")
for follower in profile.get_followers():
    username = follower.username
    file.write(username + "\n")
    print(username)
file.close()
