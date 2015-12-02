import os
import shutil
from settings import NSN
import datetime
import subprocess


date = datetime.date.today()#get day month year

#moves current travellog.csv to log folder and renames travellog.old which is initialized
#to travellog.csv. So backs up and clears the log

newFileName = 'TL' + NSN + '-' + str(date) + '.csv'
newFilePath = '/home/pi/TravelDash/logs/'+newFileName


os.rename('/home/pi/TravelDash/travellog.csv',newFilePath)

shutil.copyfile('/home/pi/TravelDash/travellog.old','/home/pi/TravelDash/travellog.csv')

subprocess.call(["/home/pi/Dropbox-Uploader/dropbox_uploader.sh","upload " + newFilePath + " /logs/"])