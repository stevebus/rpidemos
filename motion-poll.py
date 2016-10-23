import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PIR_PIN = 22
motion_count = 0

GPIO.setup(PIR_PIN, GPIO.IN)

while 1:
	if GPIO.input(PIR_PIN):
		print "motion detected! %0d" % (motion_count)
		motion_count += 1

	time.sleep(1)
