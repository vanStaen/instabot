import psycopg2
from postgreSQL.configDB import configDB


def deleteUser(table, user):

    try:
        params = configDB()
        #print('Connecting to the PostgreSQL database...')
        connection = psycopg2.connect(**params)

        cursor = connection.cursor()
        postgreSQL_select_Query = "DELETE FROM public.userlist_" + table + " WHERE username=\'" + user + "\';"
        cursor.execute(postgreSQL_select_Query)
        connection.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error while deleteing data from PostgreSQL", error)

    finally:
        #closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            #print("PostgreSQL connection is closed")