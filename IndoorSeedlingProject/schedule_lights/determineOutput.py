"""
determineOutput.py

"""
from datetime import datetime


"""
function determineOutput: 
inputs: (1)
	int timeOn: integer representing the number of hours of the day that a tray should receive light.
returns:
	int desiredOutput: returns 1 if desired output is 'ON' and 0 if desiredOutput is 'OFF'
"""
def determineOutput(timeOn):

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
	elif currHour >= endTime:
		desiredOutput = 0
	else:
		desiredOutput = 1

	response = (desiredOutput, hourStr)
	return response