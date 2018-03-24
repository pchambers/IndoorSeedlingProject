"""
int2Addr.py

Takes an integer arguement (valid 1-4)
Returns tuple, first variable is i2c Addr, 2nd is channel
"""

def int2Addr(light):
	#set relay i2c Address
	if light == 1:
		ledAddr = 2
		ledChannel = light - 1
	elif light == 2:
		ledAddr = 3
		ledChannel = 1
	elif light == 3:
		ledAddr = 2
		ledChannel = 1
	elif light == 4:
		ledAddr = 3
		ledChannel = 1
	else:
		print ''
		print 'Make sure more than 1 expansion board is installed.'
		print ''
		ledAddr = 0 			# if not on first relay 0 is all.
		#determine if channel 1 or 2 by even/odd modulus
		if light % 2 == 0:		
			ledChannel = 1		# is even, channel 1 (4) (ie board1: 0, 1, board2:0, 1)
		else:
			ledChannel = 0		# is odd, channel 0 (3)
	
	response = (ledAddr, ledChannel)

	return response
