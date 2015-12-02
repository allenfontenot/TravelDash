import os
import shutil
from settings import NSN
import datetime

date = datetime.date.today()#get day month year

#moves current travellog.csv to log folder and renames travellog.old which is initialized
#to travellog.csv. So backs up and clears the log

newFileName = 'TPDlog-' + NSN + '-' + str(date) + '.csv'
newFilePath = '/home/pi/TravelDash/TPDlogs/'+newFileName

newFileNameDebug = 'debug-' + NSN + '-' + str(date) + '.txt'
newFilePathDebug = '/home/pi/TravelDash/debuglogs/'+newFileNameDebug

os.rename('/home/pi/TravelDash/travellog.csv',newFilePath)

shutil.copyfile('/home/pi/TravelDash/travellog.old','/home/pi/TravelDash/travellog.csv')

os.rename('/home/pi/TravelDash/debug.log', newFilePathDebug)