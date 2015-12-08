#!/usr/bin/env python
import csv
import datetime

NSN = 'SIM'
zone1 = 'Lobby'
zone2 = 'Stockroom'
zone3 = 'Drive Thru'
time1=[]
time2=[]
time3=[]

FMT = '%Y-%m-%d %H:%M:%S.%f'

def findLastTime(zone):
    with open('travellog.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            if row[1].strip() == zone1:
                time1.append(row[0])
            if row[1].strip() == zone2:
                time2.append(row[0])
            if row[1].strip() == zone3:
                time3.append(row[0])
        if zone == 1:
            return max(time1)
        elif zone == 2:
            return max(time2)
        elif zone == 3:
            return max(time3)
        elif zone == 4:
            return max(time4)
        elif zone == 5:
            return max(time5)
        elif zone == 6:
            return max(time6)

print"simpush"
outputFile = open('travellog.csv', 'a')
now = datetime.datetime.now()

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