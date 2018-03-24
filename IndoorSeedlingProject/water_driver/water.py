import onionGpio, time
from datetime import datetime

def water(rack, t):

#1 find desired output
	output = waterTimer(17, t)
	desired = output[0]
#2 determine current output
	currOut = checkPumpStatus(rack)
#3 turn on/off, report
	if currOut == desired:
		print "Pumps nominal."
	else:
		#turn on or off light, report action.		
		pumpControl(rack,desired)
		if desired == 0:
			print ("Turned pump ON at: " + hourStr)
		else:
			print ("Turned pump OFF at: " + hourStr)


def trayPin(tray):
        #print tray
	if tray == 1:
        	waterPin = 0
        elif tray == 2:
        	waterPin = 1
        elif tray == 3: 
        	waterPin = 2
        elif tray == 4:
		waterPin = 3
        else:
		waterPin = 404
                #print 'Error: tray input out of range.'
	#print waterPin
	return waterPin


def waterTimer(stTime, dur):

	#determine start and end times
	startTime = stTime				# earliest acceptable time on
	endTime = startTime + dur	# time off, given a certain number of hours in the day.

	currHour = datetime.now().time().strftime("%H")	#determine the current hour (0-23)
	hourStr = currHour		# maintain original string for debugging (print function) purposes later.

	currMin = datetime.now().time().strftime("%M")
	minStr = currMin

	#cast currHour for logic operations:
	currHour = int(currHour)
	currMin = int(currMin)

	#determine desired output
	if currHour == startTime:
		if currMin <= dur:
			desiredOutput = 0
		else:
			desiredOutput = 1
	else:
		desiredOutput = 1
	
	#print desiredOutput
	response = (desiredOutput, hourStr)
	return response

def checkPumpStatus(tray):
	pin = trayPin(tray)
	pump = onionGpio.OnionGpio(pin)

	status = pump.getValue()
	print 'Gpio value: ' + status
	
	status = int(status)
	if status == 1:
		print 'Pump OFF'
	elif status == 0:
		print 'Pump ON'
	else:
		print 'Error: Bad status.'

	return status

def pumpControl(tray, desiredOutput):
	pin = trayPin(tray)
	pump = onionGpio.OnionGpio(pin)
	pump.setOutputDirection(1)
	pump.setValue(desiredOutput)
	
"""
initWater()
water(1,15)
water(2,15)
water(3,15)
water(4,15)
"""