#!/bin/sh

cd /home/pi/TravelDash

sudo python logbackup.py

sudo touch debug.log

sudo ./dropbox_uploader.sh -s -f .duconfig upload /home/pi/TravelDash/TPDlogs/*.csv /TPDlogs-gehrig/

sudo ./dropbox_uploader.sh -s -f .duconfig upload /home/pi/TravelDash/debuglogs/*.txt /debuglogs-gehrig/