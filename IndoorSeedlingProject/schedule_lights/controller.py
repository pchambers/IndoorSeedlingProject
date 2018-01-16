import time
import datetime

from datetime import datetime

from lightScheduler import lightControl
from statusCheck import checkStatus
from initConfirm import confirmInit
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

#2	#make sure relay is initialized.
	confirmInit(tray)

#3	#determine current output
	currentOutput = checkStatus(tray)

	if currentOutput == desiredOutput:
		print 'All set!'
	else:
#4		#turn on or off light, report action.		
		lightControl(tray,desiredOutput)
		if desiredOutput:
			print ("Turned lights ON at: " + hourStr)
		else:
			print ("Turned lights OFF at: " + hourStr)
	
	return 1

