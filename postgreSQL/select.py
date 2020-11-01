import psycopg2
from postgreSQL.configDB import configDB


def selectCount(table):

    try:
        params = configDB(section='aws')
        connection = psycopg2.connect(**params)

        cursor = connection.cursor()
        postgreSQL_select_Query = "SELECT COUNT(username) FROM public.userlist_" + \
            table + ";"

        cursor.execute(postgreSQL_select_Query)
        data = cursor.fetchall()

        return data[0][0]

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()
