import pygame
import pygame.gfxdraw
import os
from settings import *
#from interrupts import *
from datetime import datetime
from sendmail import *

pygame.init()
lcd = pygame.display.set_mode((1360, 768))
pygame.mouse.set_visible(False)
pygame.display.toggle_fullscreen()
background = pygame.Surface(lcd.get_size())
background = background.convert()

# initialized variables to not send emails too often
tm = tm2 = 0;
lm = lm2 = 0;

global v


def drawitall():
    os.putenv('SDL_FBDEV', '/dev/fb1')
    pygame.init()
    background.fill(bcolor)
    apron()
    circles(1, green)
    circles(2, green)
    circles(3, green)
    headers(zone1, 1)
    headers(zone2, 2)
    headers(zone3, 3)
    footers(1)
    footers(2)
    footers(3)
    title()
    complications(1)
    complications(2)
    complications(3)
    number(1, 0)
    number(2, 0)
    number(3, 0)
    compnumber(3, 0)
    compnumber(2, 0)
    compnumber(1, '04:00')
    comptext(1, c1t)
    comptext(2, c2t)
    comptext(3, c3t)
    lcd.blit(background, (0, 0))
    pygame.display.flip()


def apron():
    apron = pygame.Surface((ax, ay))
    apron.fill(acolor)
    background.blit(apron, (0, 0))


def circles(pos, color):
    if pos == 1:
        pygame.gfxdraw.aacircle(background, z1x, z1y, ocr + 1, bcolor)
        pygame.gfxdraw.filled_circle(background, z1x, z1y, ocr + 1, bcolor)
        pygame.gfxdraw.aacircle(background, z1x, z1y, ocr, color)
        pygame.gfxdraw.filled_circle(background, z1x, z1y, ocr, color)
        pygame.gfxdraw.aacircle(background, z1x, z1y, icr, ccolor)
        pygame.gfxdraw.filled_circle(background, z1x, z1y, icr, ccolor)
    elif pos == 2:
        pygame.gfxdraw.aacircle(background, z2x, z2y, ocr + 1, bcolor)
        pygame.gfxdraw.filled_circle(background, z2x, z2y, ocr + 1, bcolor)
        pygame.gfxdraw.aacircle(background, z2x, z2y, ocr, color)
        pygame.gfxdraw.filled_circle(background, z2x, z2y, ocr, color)
        pygame.gfxdraw.aacircle(background, z2x, z2y, icr, ccolor)
        pygame.gfxdraw.filled_circle(background, z2x, z2y, icr, ccolor)
    elif pos == 3:
        pygame.gfxdraw.aacircle(background, z3x, z3y, ocr + 1, bcolor)
        pygame.gfxdraw.filled_circle(background, z3x, z3y, ocr + 1, bcolor)
        pygame.gfxdraw.aacircle(background, z3x, z3y, ocr, color)
        pygame.gfxdraw.filled_circle(background, z3x, z3y, ocr, color)
        pygame.gfxdraw.aacircle(background, z3x, z3y, icr, ccolor)
        pygame.gfxdraw.filled_circle(background, z3x, z3y, icr, ccolor)


def innercircle(pos):
    # this updates the number and inner circle without changing color
    if pos == 1:
        pygame.gfxdraw.aacircle(background, z1x, z1y, icr, ccolor)
        pygame.gfxdraw.filled_circle(background, z1x, z1y, icr, ccolor)
    elif pos == 2:
        pygame.gfxdraw.aacircle(background, z2x, z2y, icr, ccolor)
        pygame.gfxdraw.filled_circle(background, z2x, z2y, icr, ccolor)
    elif pos == 3:
        pygame.gfxdraw.aacircle(background, z3x, z3y, icr, ccolor)
        pygame.gfxdraw.filled_circle(background, z3x, z3y, icr, ccolor)


def headers(zone, pos):
    h = hf.render(zone, 1, fcolor)
    hpos = h.get_rect()
    if pos == 1:
        hpos.center = (h1x, hy)
    elif pos == 2:
        hpos.center = (h2x, hy)
    elif pos == 3:
        hpos.center = (h3x, hy)
    background.blit(h, hpos)


def footers(pos):
    f = ff.render('minutes ago', 1, fcolor)
    fpos = f.get_rect()
    if pos == 1:
        fpos.center = (h1x, fy)
    elif pos == 2:
        fpos.center = (h2x, fy)
    elif pos == 3:
        fpos.center = (h3x, fy)
    background.blit(f, fpos)


def title():
    t1 = tf.render('Last', 1, tcolor)
    t2 = tf.render('Travel Path', 1, tcolor)
    t1pos = t1.get_rect()
    t2pos = t2.get_rect()
    t1pos.bottom = ty * 1
    t2pos.top = t1pos.bottom - 5
    t2pos.left = tx
    t1pos.left = tx
    background.blit(t1, t1pos)
    background.blit(t2, t2pos)


def complications(pos):
    if pos == 1:
        pygame.gfxdraw.filled_circle(background, comp1x, compy, compr, acolor)
        pygame.gfxdraw.aacircle(background, comp1x, compy, compr, acolor)
        pygame.gfxdraw.filled_circle(background, comp1x, compy, compr, green)
        pygame.gfxdraw.aacircle(background, comp1x, compy, compr, green)
    elif pos == 2:
        pygame.gfxdraw.filled_circle(background, comp2x, compy, compr, acolor)
        pygame.gfxdraw.aacircle(background, comp2x, compy, compr, acolor)
        pygame.gfxdraw.filled_circle(background, comp2x, compy, compr, yellow)
        pygame.gfxdraw.aacircle(background, comp2x, compy, compr, yellow)
    elif pos == 3:
        pygame.gfxdraw.filled_circle(background, comp3x, compy, compr, acolor)
        pygame.gfxdraw.aacircle(background, comp3x, compy, compr, acolor)
        pygame.gfxdraw.filled_circle(background, comp3x, compy, compr, red)
        pygame.gfxdraw.aacircle(background, comp3x, compy, compr, red)


def number(pos, number):
    n = nf.render(str(number), 1, fcolor)
    npos = n.get_rect()
    if pos == 1:
        npos.center = z1c
    elif pos == 2:
        npos.center = z2c
    elif pos == 3:
        npos.center = z3c
    background.blit(n, npos)


def compnumber(pos, number):
    cn = cf.render(str(number), 1, bcolor)
    cnpos = cn.get_rect()
    if pos == 1:
        cnpos.center = (comp1x, compy)
    elif pos == 2:
        cnpos.center = (comp2x, compy)
    elif pos == 3:
        cnpos.center = (comp3x, compy)
    background.blit(cn, cnpos)


def comptext(pos, text):
    ct = cff.render(str(text), 1, bcolor)
    ctpos = ct.get_rect()
    if pos == 1:
        ctpos.center = (c1tx, cty)
    elif pos == 2:
        ctpos.center = (c2tx, cty)
    elif pos == 3:
        ctpos.center = (c3tx, cty)
    background.blit(ct, ctpos)


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


def timecomp():
    tt = datetime.now()
    th = str(tt.hour)
    tm = str(tt.minute).zfill(2)
    complications(1)
    compnumber(1, th + ':' + tm)
    comptext(1, c1t)
    pygame.display.flip()


# function to store PID which is used to kill the task at night
def writePidFile():
    pid = str(os.getpid())
    f = open('pid.txt', 'w')
    f.write(pid)
    f.close()


#def avglong(rows, avgpos, longpos):  # positions are in complications
#    x = [];
#    y = []
#    with open('travellog.csv') as f:
#        reader = csv.reader(f, delimiter=',', quotechar='|')
#        for row in reader:
#            x.append(row[0])
#    i = 0
#    while i < rows - 1:
#        xa = datetime.strptime(x[i + 1], FMT)
#        xb = datetime.strptime(x[i], FMT)
#
#        y.append(xa - xb)
#
#    avg = sum(y) / len(y)
#    long = max(y)
#
#    avg = int(avg.total_seconds() / 60)
#    long = int(long.total_seconds() / 60)
#
#    complication(avgpos)
#    comptext(avgpos, c1t)
#    compnumber(avgpos, str(avg))
#
#    complication(longpos)
#    comptext(longpos, c2t)
#    compnumber(longpos, str(long))


class Violation:
    if not open('violations.txt', 'r+'):
        f = open('violations.txt', 'a+')
    else:
        f = open('violations.txt', 'r+')

    vcount = sum(1 for row in f)  # store number of rows in nowRows

    def __init__(self, time, zone, level):
        self.time = time
        self.zone = zone
        self.level = level
        f = open('violations.txt', 'a+')
        f.write(str(self.time) + ',' + str(self.zone) + ',' + str(self.level) + '\n')
        f.close()

    def count(self):
        return Violation.vcount

    def time(self):
        return 0
        #time of last violation





######interrupts###########

def interrupt1(channel):
        print"falling edge 2"
        outputFile = open('travellog.csv', 'a')
        now = datetime.now()
        lt = datetime.strptime(findLastTime(1), FMT)
        td = now - lt
        e = int(td.total_seconds() / 60)
        outputWriter = csv.writer(outputFile)
        outputWriter.writerow([now, zone1, e, NSN])
        outputFile.close()
def interrupt2(channel):
        print"falling edge 3"
        outputFile = open('travellog.csv', 'a')
        now = datetime.now()
        lt = datetime.strptime(findLastTime(2), FMT)
        td = now - lt
        e = int(td.total_seconds() / 60)
        outputWriter = csv.writer(outputFile)
        outputWriter.writerow([now, zone2, e, NSN])
        outputFile.close()
def interrupt3(channel):
        print"falling edge 4"
        outputFile = open('travellog.csv', 'a')
        now = datetime.now()
        lt = datetime.strptime(findLastTime(3), FMT)
        td = now - lt
        e = int(td.total_seconds() / 60)
        outputWriter = csv.writer(outputFile)
        outputWriter.writerow([now, zone3, e, NSN])
        outputFile.close()
def interrupt4(channel):
        print"falling edge 5"
        outputFile = open('travellog.csv', 'a')
        now = datetime.now()
        lt = datetime.strptime(findLastTime(4), FMT)
        td = now - lt
        e = int(td.total_seconds() / 60)
        outputWriter = csv.writer(outputFile)
        outputWriter.writerow([now, zone4, e, NSN])
        outputFile.close()
def interrupt5(channel):
        print"falling edge 6"
        outputFile = open('travellog.csv', 'a')
        now = datetime.now()
        lt = datetime.strptime(findLastTime(5), FMT)
        td = now - lt
        e = int(td.total_seconds() / 60)
        outputWriter = csv.writer(outputFile)
        outputWriter.writerow([now, zone5, e, NSN])
        outputFile.close()
def interrupt6(channel):
        print"falling edge 7"
        outputFile = open('travellog.csv', 'a')
        now = datetime.now()
        lt = datetime.strptime(findLastTime(6), FMT)
        td = now - lt
        e = int(td.total_seconds() / 60)
        outputWriter = csv.writer(outputFile)
        outputWriter.writerow([now, zone6, e, NSN])
        outputFile.close()