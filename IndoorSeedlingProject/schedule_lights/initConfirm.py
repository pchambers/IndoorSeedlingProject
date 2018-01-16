"""
initConfirm.py
"""
import time
from int2Addr import int2Addr
from OmegaExpansion import relayExp

def confirmInit(light):
	
	#get address
	led = int2Addr(light)
	ledAddr = led[0] 
	ledChannel = led[1]

	led1Init = 0
	cnt = 0 		#timer, 5 cycles and exit with failure.

	while led1Init == 0 or cnt < 5:
		#check initialization
		led1Init = relayExp.checkInit(ledAddr)	#confirm successful init.
		if led1Init == 0:
			print 'Initialization unsuccessful'
			led1Init = relayExp.driverInit(ledAddr)
			time.sleep(.5)
			cnt = cnt + 1
		else:
			return led1Init
			print 'Initialization confirmed'

		return 0
