from decouple import config
import requests
import json

url = 'https://mailman-cvs.herokuapp.com/api/instabot'
data = {'from': 'instabot <info@clementvanstaen.com>',
        'to': 'clement.vanstaen@gmail.com',
        'subject': 'test emailer Python/PHP',
        'body': 'test emailer Python/PHP',
        'key': config('MAILMAN_KEY')}

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
request = requests.post(url, data=json.dumps(data), headers=headers)
print(request.text)
