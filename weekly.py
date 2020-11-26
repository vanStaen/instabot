from decouple import config
import datetime as datetime
import psycopg2
from helpers.getDateTime import getDateTime
from helpers.getDateTime import getHourTime
from helpers.getDateTime import diffTime
from helpers.sendMail import sendMail
from postgreSQL.configDB import configDB
from postgreSQL.fetch import fetchAllAccount
from postgreSQL.select import selectCount

# Setup
minIterations = 10
decreaseIterationsBy = 20
maxIterations = 100
increaseIterationsBy = 5
minUsernameLeftInDb = 100

weekDaysWhenThisShouldRun = [1, 4]  # 1: monday, 2: tuesday, etc ...

# Create array for email
resultDataMail = {}
userID = 0

# Loading Accounts infos
accounts = fetchAllAccount()


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


if datetime.date.today().isoweekday() in weekDaysWhenThisShouldRun:

    # When the script started
    startTime = getHourTime()

    # Go though all the accounts
    for account in accounts:

        if account[4]:

            if account[0] and account[1] < (maxIterations - increaseIterationsBy):
                # Update accountiterations + 10
                print(update(account[3], account[1] +
                             increaseIterationsBy, account[0]))

            elif account[0] and account[1] >= (maxIterations - increaseIterationsBy):
                # Update accountiterations to maxIterations
                print(update(account[3], maxIterations, account[0]))

            elif not account[0] and account[1] > (minIterations + decreaseIterationsBy):
                # Update accountiterations to maxIterations
                print(update(account[3], account[1] -
                             decreaseIterationsBy, True))

            elif not account[0] and account[1] <= (minIterations + decreaseIterationsBy):
                # Update accountiterations to maxIterations
                print(update(account[3], minIterations, True))

        # Info array for email
        userID += 1
        resultDataMail[userID] = {
            'name': account[3],
            'iterationMax': account[1],
            'tags': account[2],
            'alive': account[4],
            'usernameLeft': selectCount(account[3].replace(".", ""))
        }

    print(resultDataMail)

    # When the script ended
    endTime = getHourTime()
    runTime = diffTime(startTime, endTime, "%H:%M:%S")

    # Info mail on script successful
    print(sendMail(3, '', '', runTime))

else:

    print('Today is not an update day! Try again Monday, Wednesday or Friday.')

    # Go though all the accounts
    for account in accounts:

        restUser = selectCount(account[3].replace(".", ""))
        # debuggig: print(f"{account[3]} : {restUser}")

        if restUser < minUsernameLeftInDb:
            # Info mail on script successful
            print(sendMail(4, account[3], minUsernameLeftInDb, ''))
