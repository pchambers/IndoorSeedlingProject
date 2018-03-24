import onionGpio, time


def water(rack, t):
	pp = trayPin(rack)
	
	if pp == 404:
		print(pp)
	#pp = 0
	pump = onionGpio.OnionGpio(pp)
	#pump._freeGpio()
	#pump.setInputDirection()
	pump.setOutputDirection(1)
	pump.setValue(0)
	time.sleep(t)
	pump.setValue(1)	
	
	#pump._freeGpio()


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

def initWater():
	water(1,0)
	water(2,0)
	water(3,0)
	water(4,0)

initWater()
water(1,15)
water(2,15)
water(3,15)
water(4,15)
