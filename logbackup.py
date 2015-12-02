import os
import shutil
from settings import NSN

date = '20150831'#get day month year

newFileName = 'TL' + NSN + date + '.csv'
newFilePath = '/home/pi/TravelDash/logs/'+newFileName


os.rename('/home/pi/TravelDash/travellog.csv',newFilePath)

shutil.copyfile('/home/pi/TravelDash/travellog.old','/home/pi/TravelDash/travellog.csv')