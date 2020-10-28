from decouple import config
import datetime as datetime
import psycopg2
from postgreSQL.fetch import fetchAllAccount
from helpers.getDateTime import getDateTime
from postgreSQL.configDB import configDB
from helpers.sendMail import sendMail

# Setup
minIterations = 10
decreaseIterationsBy = 20
maxIterations = 100
increaseIterationsBy = 10

# Loading Accounts infos
accounts = fetchAllAccount()

# Get a TimeStamp
formattedTimeStamp = getDateTime()


def update(account, iterations, active):

    try:
        params = configDB(section='heroku')
        connection = psycopg2.connect(**params)

        cursor = connection.cursor()
        postgreSQL_select_Query = f"UPDATE  public.config_accounts_insta SET active=\'{active}\', iterations=\'{iterations}\' WHERE username=\'{account}\';"
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


if datetime.date.today().isoweekday() == 1:

    # Go though all the accounts
    for account in accounts:

        if account[0] and account[1] < (maxIterations - increaseIterationsBy):
            # Update accountiterations + 10
            print(update(account[3], account[1] +
                         increaseIterationsBy, account[0]))

        elif account[0] and account[1] >= (maxIterations - increaseIterationsBy):
            # Update accountiterations to maxIterations
            print(update(account[3], maxIterations, account[0]))

        elif not account[0] and account[1] > (minIterations + decreaseIterationsBy):
            # Update accountiterations to maxIterations
            print(update(account[3], account[1]-decreaseIterationsBy, True))

        elif not account[0] and account[1] <= (minIterations + decreaseIterationsBy):
            # Update accountiterations to maxIterations
            print(update(account[3], minIterations, True))

    # Info mail on script successful
    print(sendMail(3, ''))

else:

    print('Today is not monday!')
