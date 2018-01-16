"""
lightScheduler.py
"""

import time
from OmegaExpansion import relayExp
from int2Addr import int2Addr

#lightControl receives to int inputs. 
#light: This int input refers to the numbered tray in the system, ie: 1 ==== top tray
#desiredState: This int input is either 1 to turn on the light, or 0 to turn off.
def lightControl(light, desiredState):

	#set relay i2c address
	led = int2Addr(light)
	ledAddr = led[0]
	ledChannel = led[1]

	#set output to desiredState input
	status1 = relayExp.setChannel(ledAddr, ledChannel, desiredState)
		
	return 1
	

