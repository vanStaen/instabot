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
