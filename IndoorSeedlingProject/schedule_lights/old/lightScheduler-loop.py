"""
lightScheduler.py
This file contains the functionality to run grow lights in the garden
The first iteration will be just to run 14h per day, 0500-1900
Intended implementation on omega2 with relay expansion
"""
import time
from OmegaExpansion import relayExp

led1 = 7
init = 0

#intiialize relay
status = relayExp.driverInit(led1)
print status
led1Init = relayExp.checkInit(1)
#check initialization
if led1Init == 0:
	print 'Initialization unsuccessful'
	led1Init = relayExp.driverInit(led1)
else:
	print 'Initialization successful'
while 1:
	#read current relay state
	state1 = relayExp.readChannel(led1, 1)
	if state1 == 1:
	        output1 = 0
	        print 'Relay found ON'
	else:
	        output1 = 1
	        print 'Relay found OFF'



	status1 = relayExp.setChannel(led1, 1, output1)
	time.sleep(2)