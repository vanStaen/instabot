from datetime import datetime
from dateutil import tz


def getDateTime():

    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('Europe/Berlin')
    utc = datetime.utcnow()
    utc = utc.replace(tzinfo=from_zone)
    unformattedDateStamp = utc.astimezone(to_zone)
    formattedDateStamp = unformattedDateStamp.strftime("%d/%m/%Y %H:%M")

    return formattedDateStamp


def getHourTime():

    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('Europe/Berlin')
    utc = datetime.utcnow()
    utc = utc.replace(tzinfo=from_zone)
    unformattedDateStamp = utc.astimezone(to_zone)
    formattedDateStamp = unformattedDateStamp.strftime("%H:%M:%S")

    return formattedDateStamp


def diffTime(start, end, inputFormatTime):

    time1 = datetime.strptime(end, inputFormatTime)
    time2 = datetime.strptime(start, inputFormatTime)
    diffTime = time1 - time2

    return diffTime
