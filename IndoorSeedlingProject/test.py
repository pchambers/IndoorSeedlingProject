import time, onionGpio

relay1 = onionGpio.OnionGpio(0)
relay2 = onionGpio.OnionGpio(1)
relay3 = onionGpio.OnionGpio(6)
relay4 = onionGpio.OnionGpio(7)
relay5 = onionGpio.OnionGpio(8)
relay6 = onionGpio.OnionGpio(9)
relay7 = onionGpio.OnionGpio(2)
relay8 = onionGpio.OnionGpio(3)


relay1.setOutputDirection(1)
relay2.setOutputDirection(1)
relay3.setOutputDirection(1)
relay4.setOutputDirection(1)
relay5.setOutputDirection(1)
relay6.setOutputDirection(1)
relay7.setOutputDirection(1)
relay8.setOutputDirection(1)
while 1:
	relay1.setValue(0)
	time.sleep(2)
	relay1.setValue(1)

	relay2.setValue(0)
	time.sleep(2)
	relay2.setValue(1)

	relay3.setValue(0)
	time.sleep(2)
	relay3.setValue(1)
	
	relay4.setValue(0)
	time.sleep(2)
	relay4.setValue(1)
	
	relay5.setValue(0)
	time.sleep(2)
	relay5.setValue(1)

	relay6.setValue(0)
	time.sleep(2)
	relay6.setValue(1)

	relay7.setValue(0)
	time.sleep(2)
	relay7.setValue(1)

	relay8.setValue(0)
	time.sleep(2)
	relay8.setValue(1)


"""
relay1.setValue(1)
relay2.setValue(1)
relay3.setValue(1)
relay4.setValue(1)
relay5.setValue(1)
relay6.setValue(1)
relay7.setValue(1)
relay8.setValue(1)
print 'init all to high'

while 1:
#	relay1.setValue(1)
#	relay2.setValue(1)
#	relay3.setValue(1)
#	relay4.setValue(1)
	relay5.setValue(1)
	relay6.setValue(1)
	relay7.setValue(1)
	relay8.setValue(1)
	print 'off'

	time.sleep(1)

#	relay1.setValue(0)
#	relay2.setValue(0)
#	relay3.setValue(0)
#	relay4.setValue(0)
	relay5.setValue(0)
	relay6.setValue(0)
	relay7.setValue(0)
	relay8.setValue(0)
	print 'on'
	
	time.sleep(1)
"""