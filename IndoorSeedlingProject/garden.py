from time import sleep
import urllib2

import dht22_driver.dhtOnion as DHT
import schedule_lights.controller as Controller
import water_driver.water as WaterControl
DHT22 = 'DHT22'
DHT11 = 'DHT11'
myAPI = "W0987CQMSNY4XIC3"


#define Thingspeak Uplink
def speak(pin, sensor):
    baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
    print 'starting thingspeak'
    try:
        (RH1, T1) = DHT.read(pin, sensor)
        f = urllib2.urlopen(baseURL +
                              "&field1=%s&field2=%s" % (RH1, T1))
        f.close()
        print'Temp: ' + T1 +', Humidity: ' + RH1
    except:
        print 'exiting'
        

#call garden control
Controller.gardenControl(1,16)
Controller.gardenControl(2,16)
WaterControl.water(2,15)
#speak(0, DHT22)
