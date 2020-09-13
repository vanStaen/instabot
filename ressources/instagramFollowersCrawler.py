# Get instance
import instaloader
L = instaloader.Instaloader()

user = "touwe"

# Login or load session
L.login("clementvanstaen", "kftv2h4insta")

# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, user)

# Save list of followers
file = open("insta_followers_of/"+ user +".txt","a+")
for follower in profile.get_followers():
    username = follower.username
    file.write(username + "\n")
    print(username)
file.close()