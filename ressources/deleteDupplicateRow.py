lines_seen = set() # holds lines already seen
outfile = open("insta_followers_of/cerclemusic.txt", "w")
for line in open("followersOf/cerclemusic2.txt", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()