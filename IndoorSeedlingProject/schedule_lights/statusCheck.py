"""
statusCheck

"""

from int2Addr import int2Addr
from OmegaExpansion import relayExp

def checkStatus(light):

	led = int2Addr(light)


	status = relayExp.readChannel(led[0], led[1])

	if status == 1:
		print 'Relay ON'

	elif status == 0:
		print 'Relay OFF '
	else:
		print 'Error: Bad status.'

	return status
