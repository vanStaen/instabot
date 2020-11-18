import math
from time import sleep

# 10 min = 600 sec
# 15 min = 900 sec
# 30 min = 1800 sec
# 45 min = 2700 sec
# 1 hour = 3600 sec


def herokuLongSleeper(sleepTime):

    maxTimeSleep = 10
    sleeperIterations = math.floor(sleepTime / maxTimeSleep)
    sleeperRest = sleepTime - (sleeperIterations * maxTimeSleep)
    totalSleeptimeCalc = (sleeperIterations * maxTimeSleep) + sleeperRest

    i = 1

    while i <= sleeperIterations:
        print(f"Sleeping round {i}/{sleeperIterations}")
        sleep(maxTimeSleep)
        i += 1

    return f"({sleeperIterations} * {maxTimeSleep}) + {sleeperRest} = {totalSleeptimeCalc} "
