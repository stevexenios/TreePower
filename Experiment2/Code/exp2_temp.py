#!/usr/bin/python

# Nick Purcell
# UWT 2019
# Read temp sensors from ADC and save as csv

import csv

import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

import time
from datetime import datetime
from time import sleep

startTime = time.time()									# Instantiate time

# Instantiate SPI
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# Save Data for 30 Seconds
with open('/home/pi/temp_data.csv', 'w+', newline='') as f:           # Open CV file
        writedat = csv.writer(f)
        while (time.time() < startTime + 30):
            for i in range(8):
                values[i] = mcp.read_adc(i) * 3.3 / 1024             # Get data from ADC
            writedat.writerow([values[0], values[1], values[2], values[3],
                               values[4], values[5], values[6], values[7],
                               datetime.now().isoformat()])     # Write data and time to CSV
            sleep( 5 )                                  # Sleep for 5 seconds
                
# Back up latest csv before shutting down
copyfile('/home/pi/temp_data.csv', '/home/pi/temp_data_bak_" + datetime.now().isoformat() + '.csv')

sleep(10)
os.system("sudo shutdown -h now")						# Shutdown the pi
