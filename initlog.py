#!/usr/bin/env python
import csv
import datetime
from settings import *
from background import findLastTime

print"simpush"
outputFile = open('travellog.csv', 'a')
now = datetime.now()

lt1 = datetime.datetime.strptime(findLastTime(1), FMT)
td1 = now - lt1
e1 = int(td1.total_seconds() / 60)
outputWriter = csv.writer(outputFile)
outputWriter.writerow([now, zone1, e1, NSN])

lt2 = datetime.datetime.strptime(findLastTime(2), FMT)
td2 = now - lt2
e2 = int(td2.total_seconds() / 60)
outputWriter = csv.writer(outputFile)
outputWriter.writerow([now, zone2, 2, NSN])

lt3 = datetime.datetime.strptime(findLastTime(3), FMT)
td3 = now - lt3
e3 = int(td3.total_seconds() / 60)
outputWriter = csv.writer(outputFile)
outputWriter.writerow([now, zone3, e3, NSN])



outputFile.close()