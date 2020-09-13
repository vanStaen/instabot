with open("followersOf/testfile.txt", "r") as file:
    lines = file.readlines()
with open("followersOf/testfile.txt", "w") as file:
    for line in lines:
        if line.strip("\n") != "4":
            file.write(line)