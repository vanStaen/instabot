import psycopg2
from postgreSQL.configDB import configDB


def blacklist():

    try:
        params = configDB(section="heroku")
        connection = psycopg2.connect(**params)

        cursor = connection.cursor()
        postgreSQL_select_Query = "SELECT * FROM public.blacklisted;"

        cursor.execute(postgreSQL_select_Query)
        data = cursor.fetchall()

        return data

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching blacklist data from PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
