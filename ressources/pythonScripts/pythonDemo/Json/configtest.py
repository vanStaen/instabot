import json

# read file
with open('../../config.json', 'r') as config:
    data=config.read()

# parse file
apps = json.loads(data)

i = 0

for app in apps:
    if (i == 0):
        print('> INSTAGRAM') 
        for account in app['accounts']:
            try: 
                print(account['tags'][0])
            except:
                print('Error with account {}'.format(account['username']))
    elif (i == 1):
        print('> SOUNDCLOUD') 
        for account in app['accounts']:
            try: 
                print(account['username'])
            except:
                print('Error with account {}'.format(account['username']))
    else: 
        break
    i = i + 1