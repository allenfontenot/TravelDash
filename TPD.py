#!/usr/bin/env python

import pygame
import pygame.gfxdraw
import RPi.GPIO as GPIO
from background import *
from interrupts import *
import datetime
from pygame.locals import *
from sendmail import *
import logging
from datetime import timedelta

os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# interrupt pin setup
GPIO.add_event_detect(2, GPIO.FALLING, callback=interrupt1, bouncetime=300)
GPIO.add_event_detect(3, GPIO.FALLING, callback=interrupt2, bouncetime=300)
GPIO.add_event_detect(4, GPIO.FALLING, callback=interrupt3, bouncetime=300)
GPIO.add_event_detect(14, GPIO.FALLING, callback=interrupt4, bouncetime=300)
GPIO.add_event_detect(15, GPIO.FALLING, callback=interrupt5, bouncetime=300)
GPIO.add_event_detect(18, GPIO.FALLING, callback=interrupt6, bouncetime=300)

logging.basicConfig(filename='debug.log', level=logging.DEBUG)

# Draws initial UI
drawitall()

closed = os.path.exists('imhere.txt')

# store pid to file
writePidFile()

# mail timers for not spamming notifications initialized for first pass
tm = tm2 = datetime.datetime(1999,1,1,0,0,0,0)
lm = lm2 = datetime.datetime(1999,1,1,0,0,0,0)
thenRows = 0
logcount = 0
logcount2 = 0

while True:
    offlinetime = datetime.time(22, 0, 0, 0)
    onlinetime = datetime.time(4, 0, 0, 0)
    timecomp()

    while datetime.datetime.now().time() > offlinetime or datetime.datetime.now().time() < onlinetime:
        timecomp()
        if logcount2 == 0:
            logging.debug(str(datetime.datetime.now()) + " offline")
            sendmail("offline", 0, 0, NSN, 5)
            print str(datetime.datetime.now()) + " offline"
            circles(1, red); circles(2, red); circles(3, red)
            footers(1); footers(2); footers(3)
            number(1, "offline"); number(2, "offline"); number(3, "offline")
            complications(1); complications(2)
            comptext(1, c1t); comptext(2, c2t)
            compnumber(1, "offline"); compnumber(2, "offline")
            logcount2 = 1

        # EXIT#
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == KEYDOWN:
                pygame.quit()
                sys.exit()
        lcd.blit(background, (0, 0))
        pygame.display.flip()
        logcount = 0  # so that online loggin and email only sent if offline first

    # EXIT#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            sys.exit()

    #########not offline
    timecomp()
    avgcomp()
    viocomp()
    pygame.display.flip()

    if logcount == 0:  # online notification first time through
        logging.debug(str(datetime.datetime.now()) + " online")
        sendmail("online", 0, 0, NSN, 5)
        logcount = 1

    currentTime = datetime.datetime.now()
    # subtract stored time from current

    for i in range(3):
        j = i + 1
        lastTime[i] = findLastTime(j)
        q = datetime.datetime.strptime(lastTime[i], FMT)
        r = currentTime - q
        e = int(r.total_seconds() / 60)
        if e < yellowLimit:
            color = green
        elif redLimit > e >= yellowLimit:
            color = yellow
        else:
            color = red
        circles(j, color)
        footers(j)
        number(j, e)

    lcd.blit(background, (0, 0))
    pygame.display.flip()

    ltsec = []
    for i in range(3):
        q = datetime.datetime.strptime(lastTime[i], FMT)
        ltsec[i] = int(q.totalseconds()*60)
        print lastTime[i]
        print ltsec[i]
    # notify(lm)
    if ltsec[0] >= mailtimeLevel1 or ltsec[1] >= mailtimeLevel1 or ltsec[2] >= mailtimeLevel1:
        lvl = 1
        tm = datetime.datetime.now()  # this mail is now

        if lm + timedelta(0, tba) < tm:
            sendmail(lastTime[0], lastTime[1], lastTime[2], NSN, lvl)
            print "level 1 email sent at " + str(datetime.datetime.now())
            logging.debug(str(datetime.datetime.now()) + " level 1 email sent")
            lm = tm
            Violation(datetime.datetime.now(), 'zone', lvl, max(lastTime))

    if ltsec[0] >= mailtimeLevel2 or ltsec[1] >= mailtimeLevel2 or ltsec[2] >= mailtimeLevel2:
        lvl = 2
        tm2 = datetime.datetime.now()  # this mail is now

        if lm2 + timedelta(0, tba) < tm: #check for last email sent and don't send if within tba
            sendmail(lastTime[0], lastTime[1], lastTime[2], NSN, lvl)
            print "level 2 email sent at " + str(datetime.datetime.now())
            logging.debug(str(datetime.datetime.now()) + " level 2 email sent")
            lm2 = tm2
            Violation(datetime.datetime.now(), 'zone', lvl, max(lastTime))

    logcount2 = 0

datetime.datetime.minute(30)