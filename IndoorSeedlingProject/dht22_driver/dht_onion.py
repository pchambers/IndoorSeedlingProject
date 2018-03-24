"""
dht_onion.py
"""

# Define error constants:
DHT_SUCCESS 		=  0
DHT_ERROR_TIMEOUT 	= -1
DHT_ERROR_CHECKSUM 	= -2
DHT_ERROR_ARGUMENT	= -3
DHT_ERROR_GPIO		= -4
TRANSIENT_ERRORS = [DHT_ERROR_CHECKSUM, DHT_ERROR_TIMEOUT]

#Define sensor type constants:
DHT11 	= 11
DHT22 	= 22
AM2302	= 22
SENSORS = [DHT11, DHT22, AM2302]

"""Read DHT sensor of specified sensor type (DHT11, DHT22, or AM2302) on
specified pin and return a tuple of humidity (as a floating point value
in percent) and temperature (as a floating point value in Celsius). Note that
because the sensor requires strict timing to read and Linux is not a real
time OS, a result is not guaranteed to be returned!  In some cases this will
return the tuple (None, None) which indicates the function should be retried.
Also note the DHT sensor cannot be read faster than about once every 2 seconds.
Platform is an optional parameter which allows you to override the detected
platform interface--ignore this parameter unless you receive unknown platform
errors and want to override the detection.
"""
def read(sensor, pin):
	if sensor not in SENSORS:
		raise ValueError('Expected DHT11, DHT22, or AM2302 sensor value.')
