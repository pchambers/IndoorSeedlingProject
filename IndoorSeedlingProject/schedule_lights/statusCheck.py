"""
statusCheck

"""
import onionGpio
from int2Addr import int2Addr


def checkStatus(light):

	led = int2Addr(light)
	gpio = onionGpio.OnionGpio(led)
	
	status = gpio.getValue()
	print 'Gpio value: ' + status
	
	status = int(status)
	if status == 1:
		print 'Relay OFF'
	elif status == 0:
		print 'Relay ON '
	else:
		print 'Error: Bad status.'

	return status
