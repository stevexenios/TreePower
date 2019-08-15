#!/usr/bin/python

# Nick Purcell
# UWT 2019
# Read peltier voltage from ADC and save as csv

import csv

import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

import time
from datetime import datetime
from time import sleep

startTime = time.time()									# Instantiate time

# Instantiate software SPI
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Save Data for 30 Seconds
with open('/home/pi/volt_data.csv', 'w+', newline='') as f:           # Open CV file
        writedat = csv.writer(f)
        while (time.time() < startTime + 30):
            for i in range(8):
                values[i] = mcp.read_adc(i)             # Get data from ADC
            values[0] = values[0] * M0 / 1024
            values[1] = values[1] * M1 / 1024
            values[2] = values[2] * M2 / 1024
            values[3] = values[3] * M3 / 1024
            values[4] = values[4] * M4 / 1024           # CHANGE THE Ms after experimenting with TEGs
            values[5] = values[5] * M5 / 1024
            values[6] = values[6] * M6 / 1024
            values[7] = values[7] * M7 / 1024
            writedat.writerow([values[0], values[1], values[2],
                               values[3], datetime.now().isoformat()])     # Write data and time to CSV
            sleep( 5 )                                  # Sleep for 5 seconds
# Back up latest csv before shutting down
copyfile('/home/pi/volt_data.csv', '/home/pi/volt_data_bak_" + datetime.now().isoformat() + '.csv')
