import os
from settings import NSN

date = '20150831'#get day month year

newFileName = 'TL' + NSN + date + '.csv'
newFilePath = '~/TravelDash/logs/'+newFileName


os.rename('travellog.csv',newFilePath)