import psycopg2
from configparser import ConfigParser
from postgreSQL.configDB import configDB

# Move Test.py to the root, in order to test


def fetchAllAccount():

    try:
        params = configDB(section='postgresql_heroku')
        #print('Connecting to the PostgreSQL database...')
        connection = psycopg2.connect(**params)

        cursor = connection.cursor()
        postgreSQL_select_Query = "SELECT * FROM public.config_accounts_insta;"

        cursor.execute(postgreSQL_select_Query)
        data = cursor.fetchall()

        return data

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            #print("PostgreSQL connection is closed")


result = fetchAllAccount()
#print('Username: {}'.format(result))
for account in result:
    print('###################')
    print(account[0])
    print(account[1])
    print(account[2][0])
    print(account[3])
