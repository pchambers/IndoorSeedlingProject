import subprocess
import time

DHT22 = 'DHT22'
DHT11 = 'DHT11'
AM2302 = 'AM2302'
SENSORS = [DHT22, DHT11, AM2302]

def read(pin, sensor):
	proc = subprocess.Popen(['/root/Documents/IndoorSeedlingProject/IndoorSeedlingProject/dht22_driver/checkHumidity/checkHumidity ' + str(pin) + ' ' + sensor], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()

	sensor_data = out.split('\n')
	RH = float(sensor_data[0])
	tempC = float(sensor_data[1])
	tempF = 1.8 * tempC + 32

	if RH < -250:
		RH = None
        else:
            H = str(RH)
	if tempF < -420:
		tempF = None
        else:
            T  = str(tempF) 

	return (H, T)

#return humidity then temp in F as strings
def read_retry(pin, sensor, retries=15, delay_seconds=2):
	for i in range(retries):
		rh, temp = read(pin, sensor)
		if rh is not None and temp is not None:
			return(rh, temp)
		time.sleep(delay_seconds)
	return(None, None)

#(RH, T) = read_retry(0, DHT22)

#print'Temp: ' + T +', Humidity: ' + RH 

