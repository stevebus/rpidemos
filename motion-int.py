import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PIR_PIN = 22
motion_count = 0

GPIO.setup(PIR_PIN, GPIO.IN)

def OnMotion(PIR_PIN):
	global motion_count
	print "Motion detected! %0d" % (motion_count)
	motion_count += 1

GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=OnMotion)

while 1:
	time.sleep(100)
