"""
int2Addr.py

Takes an integer arguement (valid 1-4)
Returns tuple, first variable is i2c Addr, 2nd is channel
"""

def int2Addr(light):
	#set relay i2c Address
	if light == 1:
		ledAddr = 2
	elif light == 2:
		ledAddr = 3
	elif light == 3:
		ledAddr = 2
	elif light == 4:
		ledAddr = 3
	else:
		print ''
		print 'Make sure more than 1 expansion board is installed.'
		print ''

	response = ledAddr

	return response
