import json

# Get Data for conection to mySQL
with open('../../config.mysql.db.json', 'r') as config:
    data = config.read()
dbData = json.loads(data)
for db in dbData['mySQL']:
    host_mysqli = db['host_mysqli']
    user_mysqli = db['user_mysqli']
    pass_mysqli = db['pass_mysqli']
    bd_mysqli = db['bd_mysqli']

print(host_mysqli)
print(user_mysqli)
print(pass_mysqli)
print(bd_mysqli)