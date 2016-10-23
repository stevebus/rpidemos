import sys
import time

import Adafruit_DHT

sensor = Adafruit_DHT.DHT22
pin = 6

msg = "Temp=%0.2f , Humidity=%0.2f"

while 1:

	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

	temperature = temperature * 9/5.0 + 32

	if humidity is not None and temperature is not None:
	    print(msg % (temperature, humidity))
	else:
	    print('Failed to get reading. Trying again!')

	time.sleep(2)
