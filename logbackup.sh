#!/bin/sh

cd /home/pi/TravelDash

sudo python logbackup.py

sudo ./dropbox_uploader.sh -s -f .duconfig upload /home/pi/TravelDash/TPDlogs/*.csv /TPDlogs-gehrig/

sudo ./dropbox_uploader.sh -s -f .duconfig upload /home/pi/TravelDash/debuglogs/*.txt /TPDlogs-gehrig/