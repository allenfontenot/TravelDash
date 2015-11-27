#//This shuts down the timing and puts up a placeholder screen until the reload
#//the next morning. Happens at 10pm with restart at 4 am

cd /home/pi/TimerTest
sudo ./Timer.py
sudo kill $(cat /home/pi/TimerTest/pid2.txt)
