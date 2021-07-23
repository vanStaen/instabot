import os

# Read a File in Python
fromDirectory = "followersOf"

for filename in os.listdir(fromDirectory):
    if filename.endswith(".txt"):
        targetUserFile = filename
        targetUserFollowers = open("followersOf/"+ targetUserFile,"r")
        with targetUserFollowers as file:
            for profile in file:
                print('{} is followed by {}'.format(targetUserFile, profile))
        targetUserFollowers.close()
        continue
    else:
        continue