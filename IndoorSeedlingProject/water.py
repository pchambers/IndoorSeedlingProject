import onionGpio

def water(tray):
	pp = trayPin(tray)
	
	pump = onionGpio.OnionGpio(pp)
	pump.setOutputDirection(1)
	time.sleep(15)
	pump.setOutputDirection(0)	



def trayPin(tray):
        if(tray is 1):
                waterPin = 1
        if (tray is 2)
                waterPin = 2
        if (tray is 3) 
                waterPin = 3
        if (tray is 4)
                waterPin = 4
        else:
		waterPin = 404
                print 'Error: tray input out of range.'
	return waterPin


