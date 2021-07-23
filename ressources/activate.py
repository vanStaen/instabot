from decouple import config
import datetime as datetime
import psycopg2
from postgreSQL.fetch import fetchAllAccount
from helpers.getDateTime import getDateTime
from postgreSQL.configDB import configDB

# Loading Accounts infos
accounts = fetchAllAccount()


def update(account, active):

    try:
        params = configDB(section='heroku')
        connection = psycopg2.connect(**params)

        cursor = connection.cursor()
        postgreSQL_select_Query = f"UPDATE  public.config_accounts_insta SET active=\'{active}\' WHERE username=\'{account}\';"
        cursor.execute(postgreSQL_select_Query)
        connection.commit()

        return f"Account '{account}' updated!"

    except (Exception, psycopg2.Error) as error:
        print("Error while deleteing data from PostgreSQL", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            # print("PostgreSQL connection is closed")


# Go though all the accounts
for account in accounts:

    # Update accountiterations to maxIterations
    print(update(account[3], True))
