#!/usr/bin/python

# Nick Purcell
# UWT 2019
# Takes peltier voltage data from arduino and saves it to a txt file.

import serial
from datetime import datetime
from time import sleep

ser = serial.Serial('/dev/ttyUSB0', 115200)		  #Instatiate connection to Arduino

ctime = datetime.now().isoformat() #Instantiate time

F=open("/home/pi/VoltageData" + ctime + ".txt","w+")		  #create TXT file

while True:
	try:
		if(ser.in_waiting > 0):
			ctime = datetime.now().isoformat()
			line = ser.readline().decode() 		  #Decode data from Arduino
			F.write(ctime)				  #Write date and time
			F.write(" (mV) " + line)		  #Write arduino Data
	except KeyboardInterrupt:
		break
		quit()
	ser.reset_input_buffer()
	sleep( 60 )
