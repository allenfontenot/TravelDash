sudo chmod +x /home/pi/TravelDash/dashonrestart.sh
sudo chmod +x /home/pi/TravelDash/offline.sh
sudo chmod +x /home/pi/TravelDash/online.sh
sudo chmod +x /home/pi/TravelDash/rebootme.sh
sudo chmod +x /home/pi/TravelDash/initlog.py

sudo cp /home/pi/TravelDash/Crons/online /etc/cron.d/online
sudo cp /home/pi/TravelDash/Crons/offline /etc/cron.d/offline
sudo cp /home/pi/TravelDash/Crons/dashonrestart /etc/cron.d/dashonrestart

sudo chmod +x /etc/cron.d/online
sudo chmod +x /etc/cron.d/offline
sudo chmod +x /etc/cron.d/dashonrestart

sudo python initlog.py
