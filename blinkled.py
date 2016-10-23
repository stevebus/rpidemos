import RPi.GPIO as GPIO
import time

def blink(pin):
	GPIO.output(pin, GPIO.HIGH)
	time.sleep(1)
	print("on")
	GPIO.output(pin, GPIO.LOW)
	time.sleep(1)
	print("off")
	return

GPIO.setmode(GPIO.BOARD)

GPIO.setup(35, GPIO.OUT)

for i in range(0, 50):
	blink(35)

GPIO.cleanup()

