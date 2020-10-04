import json
import mysql.connector
from mysql.connector import Error

# Get Data for conection to mySQL
with open('../../config.mysql.db.json', 'r') as config:
    data = config.read()
dbData = json.loads(data)
for db in dbData['awardspace']:
    id = db['id']
    host = db['host']
    user = db['user']
    name = db['name']
    pwd = db['pwd']

print('###########')
print(name)

# Connect to MySQL
try:
    connection = mysql.connector.connect(host=host_mysqli,
                                         database=bd_mysqli,
                                         user=user_mysqli,
                                         password=pass_mysqli)
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
