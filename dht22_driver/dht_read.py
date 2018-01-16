#This program is meant to follow dht_read.cpp fro the Adafruit library

# There is a #include for a dht_read header, not sure what it is, but we'll find out!

import onionGpio

# This is the only processor specific magic value, the maximum amount of time to
# spin in a loop before bailing out and considering the read a timeout.  This should
# be a high value, but if you're running on a much faster platform than a Raspberry
# Pi or Beaglebone Black then it might need to be increased.
DHT_MAXCOUNT = 32000

# Number of bit pulses to expect from the DHT.  Note that this is 41 because
# the first pulse is a constant 50 microsecond pulse, with 40 pulses to represent
# the data afterwards.
DHT_PULSES = 41

def dht_read(type, pin, humidity, temperature):
	#validate imputs for temp and humid and then set to 0
	if humidity is None || temperature is None:
		print("DHT Arguement Error")
		return DHT_ERROR_ARGUEMENT
	temperature = -255.0
	humidity = -255.0

	#initialize GPIO pin
	dhtGpio = onionGpio.OnionGpio(pin)
	status = dhtGpio.setOutputDirection(0)
	
	#Store the count that each DHT bit pulse is low and high.
	#Make sure array is initialized to start at zero.
	pulseCounts[DHT_PULSES*2] = {0}




