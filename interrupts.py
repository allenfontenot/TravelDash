#!/usr/bin/env python

import RPi.GPIO as GPIO
import csv
import datetime
from settings import *
from datetime import timedelta
from datetime import datetime


def interrupt1(channel):
        print"falling edge 2"

        outputFile = open('travellog.csv', 'a')
        time1 = datetime.now()
        outputWriter = csv.writer(outputFile)
        outputWriter.writerow([time1, zone1, NSN])
        outputFile.close()
def interrupt2(channel):
        print"falling edge 3"
        outputFile = open('travellog.csv', 'a')
        time2 = datetime.now()
        outputWriter = csv.writer(outputFile)
        outputWriter.writerow([time2, zone2, NSN])
        outputFile.close()
def interrupt3(channel):
        print"falling edge 4"
        outputFile = open('travellog.csv', 'a')
        time3 = datetime.now()
        outputWriter = csv.writer(outputFile)
        outputWriter.writerow([time3, zone3, NSN])
        outputFile.close()
def interrupt4(channel):
        print"falling edge 14"
        outputFile = open('travellog.csv', 'a')
        time1 = datetime.now()
        outputWriter = csv.writer(outputFile)
        outputWriter.writerow([time1, zone1, NSN])
        outputFile.close()
def interrupt5(channel):
        print"falling edge 15"
        outputFile = open('travellog.csv', 'a')
        time2 = datetime.now()
        outputWriter = csv.writer(outputFile)
        outputWriter.writerow([time2, zone2, NSN])
        outputFile.close()
def interrupt6(channel):
        print"falling edge 18"
        outputFile = open('travellog.csv', 'a')
        time3 = datetime.now()
        outputWriter = csv.writer(outputFile)
        outputWriter.writerow([time3, zone3, NSN])
        outputFile.close()
