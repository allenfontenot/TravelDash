#!/usr/bin/env python

import csv
from settings import *
import datetime
from background import findLastTime


def interrupt1(channel):
        print"falling edge 2"
        outputFile = open('travellog.csv', 'a')
        now = datetime.datetime.now()
        lt = datetime.datetime.strptime(findLastTime(1), FMT)
        td = now - lt
        e = int(td.total_seconds() / 60)
        outputWriter = csv.writer(outputFile)
        outputWriter.writerow([now, zone1, e, NSN])
        outputFile.close()
def interrupt2(channel):
        print"falling edge 3"
        outputFile = open('travellog.csv', 'a')
        now = datetime.datetime.now()
        lt = datetime.datetime.strptime(findLastTime(2), FMT)
        td = now - lt
        e = int(td.total_seconds() / 60)
        outputWriter = csv.writer(outputFile)
        outputWriter.writerow([now, zone2, e, NSN])
        outputFile.close()
def interrupt3(channel):
        print"falling edge 4"
        outputFile = open('travellog.csv', 'a')
        now = datetime.datetime.now()
        lt = datetime.datetime.strptime(findLastTime(3), FMT)
        td = now - lt
        e = int(td.total_seconds() / 60)
        outputWriter = csv.writer(outputFile)
        outputWriter.writerow([now, zone3, e, NSN])
        outputFile.close()
def interrupt4(channel):
        print"falling edge 5"
        outputFile = open('travellog.csv', 'a')
        now = datetime.datetime.now()
        lt = datetime.datetime.strptime(findLastTime(4), FMT)
        td = now - lt
        e = int(td.total_seconds() / 60)
        outputWriter = csv.writer(outputFile)
        outputWriter.writerow([now, zone4, e, NSN])
        outputFile.close()
def interrupt5(channel):
        print"falling edge 6"
        outputFile = open('travellog.csv', 'a')
        now = datetime.datetime.now()
        lt = datetime.datetime.strptime(findLastTime(5), FMT)
        td = now - lt
        e = int(td.total_seconds() / 60)
        outputWriter = csv.writer(outputFile)
        outputWriter.writerow([now, zone5, e, NSN])
        outputFile.close()
def interrupt6(channel):
        print"falling edge 7"
        outputFile = open('travellog.csv', 'a')
        now = datetime.datetime.now()
        lt = datetime.datetime.strptime(findLastTime(6), FMT)
        td = now - lt
        e = int(td.total_seconds() / 60)
        outputWriter = csv.writer(outputFile)
        outputWriter.writerow([now, zone6, e, NSN])
        outputFile.close()