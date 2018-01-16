import time
import datetime

from datetime import datetime

from lightScheduler import lightControl
from statusCheck import checkStatus

"""
controller.py
intended to 
"""

##__________________ define inputs _____________________
tray1 = 1 		#tray1 is light 1 
timeOn = 16		#hours per day of light


##__________________ begin handling ____________________ 
lightAddr = tray1

#determine start and end times
startTime = 5					# earliest acceptable time on
endTime = startTime + timeOn	# time off, given a certain number of hours in the day.

currHour = datetime.now().time().strftime("%H")	#determine the current hour (0-23)
hourStr = currHour		# maintain original string for debugging (print function) purposes later.

#cast currHour for logic operations:
currHour = int(currHour)

#determine desired output
if currHour < startTime:
	desiredOutput = 0
elif currHour > endTime:
	desiredOutput = 0
else:
	desiredOutput = 1

#determine current output
currentOutput = checkStatus(lightAddr)

if currentOutput == desiredOutput:
	print 'All set!'
else:
	lightControl(lightAddr,desiredOutput)
	if desiredOutput:
		print ("Turned lights ON at: " + hourStr)
	else:
		print ("Turned lights OFF at: " + hourStr)

"""
## code for flipping output:
if led1Status:
	output1 = 0
elif led1Status == 0:
else:
	output1 = 1
	print 'Bad read, try initializing relay'
## end 
"""


