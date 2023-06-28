#This program takes in values from two switches which control the brightness of an LED.
#The brightness increments by the power of a number to account for the large jumps in
#perceivedbrightness as the brightness changes at low voltages. The program alerts the
#terminal when the brightness values are at its max and min, and the current value of 
#the LED brightness.
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
from time import sleep

#Output LED pin
ledPin=12

#Dimness and Brightness pin inputs
dimPin=32
brightPin=18
dt=0.1

GPIO.setup(ledPin,GPIO.OUT)
GPIO.setup(brightPin,GPIO.IN,pull_up_down=GPIO.PUD_UP) #Brightness pin with pull-up
GPIO.setup(dimPin,GPIO.IN,pull_up_down=GPIO.PUD_UP) #Dimness pin with pull-up

brightState=1
brightStateOld=1
dimState=1
dimStateOld=1
ledState=GPIO.PWM(ledPin,100)
ledVal=0
ledState.start(ledVal)
BP=0

try:
	while True:
		brightState=GPIO.input(brightPin)
		dimState=GPIO.input(dimPin)
		if brightState==0 and brightStateOld==1:
			BP=BP+1
			ledVal=(1.5849)**BP
			if ledVal>100:
				BP=10
				ledVal=100
				print('Max brightness!')
			ledState.ChangeDutyCycle(int(ledVal))
		if dimState==0 and dimStateOld==1:
			BP=BP-1
			ledVal=(1.5849)**BP
			if ledVal<1.1:
				BP=0
				ledVal=0
				print('The LED is off!')
			ledState.ChangeDutyCycle(int(ledVal))
		brightStateOld=brightState
		dimStateOld=dimState
		print(ledVal)
		sleep(dt)
except KeyboardInterrupt:
	ledState.stop()
	GPIO.cleanup()
	print('Bye!')

