import psycopg2
from postgreSQL.configDB import configDB


def deactivate(account):

    try:
        params = configDB(section='heroku')
        connection = psycopg2.connect(**params)

        cursor = connection.cursor()
        postgreSQL_select_Query = "UPDATE  public.config_accounts_insta SET active=\'false\' WHERE username=\'" + account + "\';"
        cursor.execute(postgreSQL_select_Query)
        connection.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error while deleteing data from PostgreSQL", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            #print("PostgreSQL connection is closed")


def kill(account):

    try:
        params = configDB(section='heroku')
        connection = psycopg2.connect(**params)

        cursor = connection.cursor()
        postgreSQL_select_Query = "UPDATE  public.config_accounts_insta SET active=\'false\', alive=\'false\' WHERE username=\'" + account + "\';"
        cursor.execute(postgreSQL_select_Query)
        connection.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error while deleteing data from PostgreSQL", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            #print("PostgreSQL connection is closed")
