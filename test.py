from postgreSQL.fetch import fetchFirst
from postgreSQL.delete import deleteUser
import logging

#Setting up logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('log/insta_bot.log')
file_formatter = logging.Formatter(
    "{'time':'%(asctime)s', 'level': '%(levelname)s', 'message': '%(message)s'}"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

account = 'clementvanstaen'
result = fetchFirst(account)
logging.info('Fetch user {} from postgreSQL table {}.'.format(result, account))
print('Username: {}'.format(result))

deleteUser('test', 'test4')
