from decouple import config


def configDB(section):
    db = {}
    db['host'] = config(section.upper()+'_DATABASE_HOST')
    db['database'] = config(section.upper()+'_DATABASE_DATABASE')
    db['user'] = config(section.upper()+'_DATABASE_USER')
    db['password'] = config(section.upper()+'_DATABASE_PWD')

    return db
