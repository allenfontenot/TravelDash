#!/bin/sh

cd /home/pi/TravelDash

sudo ./logbackup.py

sudo ./dropbox_uploader.sh -s -f .duconfig upload /home/pi/TravelDash/TPDlogs/*.csv /TPDlogs-gehrig/

sudo ./dropbox_uploader.sh -s -f .duconfig upload /home/pi/TravelDash/debuglogs/*.csv /TPDlogs-gehrig/