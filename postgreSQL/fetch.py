import psycopg2
from postgreSQL.configDB import configDB


def fetchFirst(table):

    try:
        params = configDB(section='postgresql_aws')
        connection = psycopg2.connect(**params)

        cursor = connection.cursor()
        postgreSQL_select_Query = "SELECT * FROM public.userlist_" + table + " LIMIT 1;"

        cursor.execute(postgreSQL_select_Query)
        data = cursor.fetchall()

        for row in data:
            return (row[0])

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()


def fetchAllAccount():

    try:
        params = configDB(section='postgresql_heroku')
        connection = psycopg2.connect(**params)

        cursor = connection.cursor()
        postgreSQL_select_Query = "SELECT * FROM public.config_accounts_insta;"

        cursor.execute(postgreSQL_select_Query)
        data = cursor.fetchall()

        return data

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()
