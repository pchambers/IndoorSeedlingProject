import time
import datetime

from datetime import datetime

from lightScheduler import lightControl
from statusCheck import checkStatus
from determineOutput import determineOutput


"""
controller.py
Does:
1 - Determine desired output of lights
2 - Confirm successful initialization of relay
3 - Checks the current output status
4 - Changes output if neccessary
"""

def gardenControl(tray, timeOn):

#1	#find desired output:
	output = determineOutput(timeOn)
	desiredOutput = output[0]
	hourStr = output[1]					#function also returns current hour for debug
	print "desired output: "
	print  desiredOutput

#2	#determine current output
	currentOutput = checkStatus(tray)

	if currentOutput == desiredOutput:
		print 'Lights nominal.'
	else:
#3		#turn on or off light, report action.		
		lightControl(tray,desiredOutput)
		if desiredOutput == 0:
			print ("Turned lights ON at: " + hourStr)
		else:
			print ("Turned lights OFF at: " + hourStr)
	
	return 1

