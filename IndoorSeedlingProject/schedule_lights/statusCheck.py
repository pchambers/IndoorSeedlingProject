"""
statusCheck

"""

from int2Addr import int2Addr
from OmegaExpansion import relayExp

def checkStatus(light):

	led = int2Addr(light)
	gpio = onionGpio.OnionGpio(led[0])

	#status = relayExp.readChannel(led[0], led[1])
	
	status = gpio.getValue()
	if status == 1:
		print 'Relay OFF'
	elif status == 0:
		print 'Relay ON '
	else:
		print 'Error: Bad status.'

	return status
