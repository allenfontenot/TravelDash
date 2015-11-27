#!/usr/bin/env python

import os
import sys
import time
import csv
import datetime
from datetime import datetime
from settings import *

outputFile = open('travellog.csv', 'a')
time1 = datetime.now()
outputWriter = csv.writer(outputFile)
outputWriter.writerow([time1, zone1, NSN])
outputWriter.writerow([time1, zone2, NSN])
outputWriter.writerow([time1, zone3, NSN])
outputFile.close()
