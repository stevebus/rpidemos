import RPi.GPIO as GPIO
import time
import smbus

GPIO.setmode(GPIO.BCM)

BUTTON_PIN = 16
click_count = 1

GPIO.setwarnings(False)
GPIO.setup(BUTTON_PIN, GPIO.IN)

bus = smbus.SMBus(1)

DEVICE=0x20
PIN_DIR_REG = 0x00
PIN_VALUES = 0x14

# set all pins as outputs (by writing zeros)
bus.write_byte_data(DEVICE, PIN_DIR_REG, 0x00)

# turn off all LEDs
bus.write_byte_data(DEVICE, PIN_VALUES, 0x00)

def SetPinValues(value):
	bus.write_byte_data(DEVICE, PIN_VALUES, value)

def OnButton(BUTTON_PIN):
	global click_count
	if click_count > 15:
		print "Button detected! zero"
		SetPinValues(0)
		click_count = 1
	else:
		print "Button detected! %0d" % (click_count)
		SetPinValues(click_count)
		click_count += 1

GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=OnButton)

while 1:
	time.sleep(100)
