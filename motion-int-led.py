import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BCM)

PIR_PIN = 22
LED_PIN = 19

motion_count = 0

GPIO.setwarnings(False)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

def BlinkLED():
	GPIO.output(LED_PIN, GPIO.HIGH)
	time.sleep(2)
	GPIO.output(LED_PIN, GPIO.LOW)

class LEDManager( threading.Thread):
	def run(self):
		#print "blink the led"
		BlinkLED()

def OnMotion(PIR_PIN):
	global motion_count
	print "Motion detected! %0d" % (motion_count)
	motion_count += 1
	LEDManager().start()

GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=OnMotion)

while 1:
	time.sleep(100)
