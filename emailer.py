from decouple import config
import requests

url = 'https://mailman-cvs.herokuapp.com/api/instabot'
data = {'from': 'rewaer <info@rewaer.com>',
        'to': 'clement.vanstaen@gmail.com',
        'subject': 'mirror call ma couille',
        'body': 'This is working my dude.',
        'key': config('MAILMAN_KEY')}

request = requests.post(url, data=data)
print(request.text)
