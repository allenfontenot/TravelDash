#!/usr/bin/env python

import pygame
import pygame.gfxdraw
import RPi.GPIO as GPIO
from background import *
from interrupts import *
from datetime import datetime
from pygame.locals import *
from sendmail import *

os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()

#Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN,pull_up_down=GPIO.PUD_UP); GPIO.setup(3, GPIO.IN,pull_up_down=GPIO.PUD_UP); GPIO.setup(4, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(14, GPIO.IN,pull_up_down=GPIO.PUD_UP); GPIO.setup(15, GPIO.IN,pull_up_down=GPIO.PUD_UP); GPIO.setup(18, GPIO.IN,pull_up_down=GPIO.PUD_UP)

#interrupt pin setup
GPIO.add_event_detect( 2, GPIO.FALLING, callback=interrupt1, bouncetime=300)
GPIO.add_event_detect( 3, GPIO.FALLING, callback=interrupt2, bouncetime=300)
GPIO.add_event_detect( 4, GPIO.FALLING, callback=interrupt3, bouncetime=300)
GPIO.add_event_detect(14, GPIO.FALLING, callback=interrupt4, bouncetime=300)
GPIO.add_event_detect(15, GPIO.FALLING, callback=interrupt5, bouncetime=300)
GPIO.add_event_detect(18, GPIO.FALLING, callback=interrupt6, bouncetime=300)

logging.basicConfig(filename = 'debug.log', level=logging.DEBUG)

#Draws initial UI
drawitall()

closed = os.path.exists('imhere.txt')

#store pid to file
writePidFile()

#circle status
imgreen = [False, False, False]
imyellow = [False,False,False]
imred = [False,False,False]

#mail timers for not spamming notifications
tm = tm2 =  0; lm = lm2 =  0;
thenRows = 0
logcount = 0
logcount2 = 0
while True:
	print "in first while"
	logging.debug(str(datetime.now()) + " in first while")
	#put time on comnplication 3
	timeComp()		
	while closed == True: #checks for offline from file inserted through cron
		timeComp()
		if logcount2 == 0:
			logging.debug(str(datetime.now()) + " offline")
			sendmail("offline",0,0,NSN,5)
			print str(datetime.now()) + " offline"
			logcount2 =1
		#EXIT#
		for event in pygame.event.get():
                	if event.type == pygame.QUIT:
                        	pygame.quit()
                        	sys.exit()
                	elif event.type == KEYDOWN:
                        	sys.exit()

		circles(1,red);circles(2,red);circles(3,red)
		footers(1);footers(2);footers(3)
		number(1,"offline");number(2,"offline");number(3,"offline")
		complications(1);complications(2)
		comptext(1,c1t);comptext(2,c2t)
		compnumber(1,"offline");compnumber(2,"offline")

		#HMT = '%Y-%m-%d %H:%M:%S.%f'
	        #currentTime = datetime.now()

		lcd.blit(background, (0,0))
		pygame.display.flip()
		
		logcount = 0 #so that online loggin and email only sent if offline first
		closed = os.path.exists('imhere.txt')
	while closed == False:
		timeComp()
		if logcount == 0:
			logging.debug(str(datetime.now()) + " online")
                	sendmail("online",0,0,NSN,5)
			logcount = 1
		#EXIT#
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                        elif event.type == KEYDOWN:
                                sys.exit()

		f = open('travellog.csv')#openfile
		nowRows = sum(1 for row in f)#store number of rows in nowRows
		diffRows = nowRows - thenRows #check for added rows
		
		if diffRows == 0:
			f.close()
		else:
			#avglong(nowRows,1,2) #puts average in complication 1 and long in comp2
			#pygame.display.flip()	
		
			if diffRows < 0:
				thenRows = nowRows
				importFile.close()
			#finds the last entry for each zone
			else:
				lastTime[0] = findLastTime(1)
				lastTime[1] = findLastTime(2)
				lastTime[2] = findLastTime(3)

			currentTime = datetime.now()
		#subtract stored time from current
		k = 0
		while k < 3:
			q = datetime.strptime(lastTime[k],FMT)
			r = currentTime - q
			timeDiff[k] = r 
			#extract whole elapsed time minutes

			nowMinutes[k] = int(timeDiff[k].total_seconds() / 60)

			if nowMinutes[k] != thenMinutes[k]:
				thenMinutes[k] = nowMinutes[k]
				if   thenMinutes[k] >= 0 and thenMinutes[k] < yellowLimit and imgreen[k] == False:
					print "changing zone " + str(k+1) + " to " + str(thenMinutes[k])
					logging.debug(str(datetime.now()) + " changing zone " + str(k+1) + " to " + str(thenMinutes[k]))
					circles(k+1,green)
					footers(k+1)
					number(k+1,thenMinutes[k])
					imgreen[k] != imgreen[k]
					lcd.blit(background, (0,0))
					pygame.display.flip()
			        elif thenMinutes[k] >= yellowLimit and thenMinutes[k] < redLimit and imyellow[k] == False:
					print "changing zone " + str(k+1) + " to " + str(thenMinutes[k])
					logging.debug(str(datetime.now()) + " changing zone " + str(k+1) + " to " + str(thenMinutes[k]))
					circles(k+1,yellow)
					footers(k+1)
                                        number(k+1,thenMinutes[k])
					imyellow[k] != imyellow[k]
					lcd.blit(background, (0,0))
                                        pygame.display.flip()
			        elif thenMinutes[k] >= redLimit and imred[k] == False:
					print "changing zone " + str(k+1) + " to " + str(thenMinutes[k])
					logging.debug(str(datetime.now()) + " changing zone " + str(k+1) + " to " + str(thenMinutes[k]))
					circles(k+1,red)
					footers(k+1)
                                        number(k+1,thenMinutes[k])
					imred[k] != imred[k]
					lcd.blit(background, (0,0))
                                        pygame.display.flip()
				else:
					print "changing zone " + str(k+1) + " to"  + str(thenMinutes[k])
					logging.debug(str(datetime.now()) + " changing zone " + str(k+1) + " to"  + str(thenMinutes[k]))
					innercircle(k+1)
					footers(k+1)
					number(k+1,thenMinutes[k])
					lcd.blit(background, (0,0))
					pygame.display.flip()
			k += 1
		#notify(lm)
		if thenMinutes[0] >= mailtimeLevel1 or thenMinutes[1] >= mailtimeLevel1 or thenMinutes[2] >= mailtimeLevel1:
        		lvl = 1
        		tm = time.time()  #this mail is now
        		tslm = tm - lm    #time since last mail = this mail - last mail
        		if tslm > tba:#time between alerts in seconds 30min = 1800
            		sendmail(thenMinutes[0], thenMinutes[1], thenMinutes[2],NSN,lvl)
            		print "level 1 email sent at " + str(datetime.now())
            		logging.debug(str(datetime.now()) + " level 1 email sent")
            		lm = tm
#level two email
	    if thenMinutes[0] >= mailtimeLevel2 or thenMinutes[1] >= mailtimeLevel2 or thenMinutes[2] >= mailtimeLevel2:
                lvl = 2
                tm2 = time.time()  #this mail is now
                tslm2 = tm2 - lm2    #time since last mail = this mail - last mail
                if tslm2 > tba:#time between alerts in seconds 30min = 1800
                    sendmail(thenMinutes[0], thenMinutes[1], thenMinutes[2],NSN,lvl)
                    print "level 2 email sent at " +  str(datetime.now())
                    logging.debug(str(datetime.now()) +  " level 2 email sent")
                    lm2 = tm2
	logcount2 = 0
	closed = os.path.exists('imhere.txt')