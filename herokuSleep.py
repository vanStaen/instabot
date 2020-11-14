import math
from time import sleep


def herokuLongSleeper(sleepTime):

    maxTimeSleep = 15
    sleeperIterations = math.floor(sleepTime / maxTimeSleep)
    sleeperRest = sleepTime - (sleeperIterations * maxTimeSleep)
    totalSleeptimeCalc = (sleeperIterations * maxTimeSleep) + sleeperRest

    i = 1

    while i <= sleeperIterations:
        print(f"Sleeping round {i}/{sleeperIterations}")
        sleep(maxTimeSleep)
        i += 1

    return f"({sleeperIterations} * {maxTimeSleep}) + {sleeperRest} = {totalSleeptimeCalc} "


print(herokuLongSleeper(35))
