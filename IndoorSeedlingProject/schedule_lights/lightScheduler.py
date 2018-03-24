"""
lightScheduler.py
"""

import time, onionGpio
from OmegaExpansion import relayExp
from int2Addr import int2Addr

#lightControl receives to int inputs. 
#light: This int input refers to the numbered tray in the system, ie: 1 ==== top tray
#desiredState: This int input is either 0 to turn on the light, or 1 to turn off.
def lightControl(light, desiredState):

	#set relay i2c address
	led = int2Addr(light)
	ledAddr = led[0]
	
	#ledChannel = led[1]
	#print ledAddr
	#set output to desiredState input
	#status1 = relayExp.setChannel(ledAddr, ledChannel, desiredState)
	
	led = onionGpio.OnionGpio(ledAddr)
	led.setOutputDirection(1)
	led.setValue(desiredState)
	#print desiredState
	return 1
	
#lightControl(1, 0)
#lightControl(2,0)
