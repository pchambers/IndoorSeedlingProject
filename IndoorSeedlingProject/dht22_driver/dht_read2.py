"""

dht_read
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


DHT_MAXCOUNT = 32000
DHT_PULSES = 41

def dht_read(type, pin, humidity, temperature):
	#Validate humidity and temperature arguements and set them to 0.
	if humidity is None or temperature is None:
			return DHT_ERROR_ARGUMENT
	
	temperature = -255
	humidity = -255

	##***** insert fastGPIO
	"""
	FastGpioOmega2	gpioObj;
  	gpioObj.SetVerbosity(0);
  	gpioObj.SetDebugMode(0);
	"""
