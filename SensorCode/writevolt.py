#!/usr/bin/python

# Nick Purcell
# UWT 2019
# Takes peltier voltage data from arduino and saves it to a txt file.

from datetime import datetime
from time import sleep

time = datetime.now().isoformat()									#Instantiate time

f = open(fname, "w+")
f.close()

while True:
	try:
		if(ser.in_waiting > 0):
			log = open(fname,"a")
			ctime = datetime.now().isoformat()
			line = ser.readline().decode() 		  	#Decode data from Arduino
			log.write(ctime)				  		#Write date and time
			log.write(" (mV) " + line)		  		#Write arduino Data
			print(ctime + " " + line)
			log.close()
			ser.reset_input_buffer()
			sleep( 5 )
	except KeyboardInterrupt:
		break
		quit()
