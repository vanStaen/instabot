from decouple import config
import psycopg2
from postgreSQL.fetch import fetchAllAccount
from helpers.sendMail import sendMail
from postgreSQL.configDB import configDB

# Loading Accounts infos
accounts = fetchAllAccount()

userID = 0
resultDataMail = {}

# Go though all the accounts
for account in accounts:

    if not account[0]:
        userID += 1
        resultMail[userID] = {'active': False}
    else:
        userID += 1
        resultDataMail[userID] = {
            'active': True,
            'name': account[3],
            'errors': 0,
            'iterations': 0
        }


# Info mail on script successful
# print(sendMail(0, resultDataMail))

for accountInfo in resultDataMail:
    if resultDataMail[accountInfo]['active']:
        print(resultDataMail[accountInfo])
    else:
        print(
            f"Account '{resultDataMail[accountInfo]['name']}' is deactivated.")
