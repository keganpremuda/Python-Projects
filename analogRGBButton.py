#This program  takes input from three switches that represent the value of red, blue,
# or green hue a RGB light emits and displays those values in the terminal.
# The program also simulates the light color change in a simulation window
# via Virtual Python.
from vpython import *
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
from time import sleep

rin=15	 #Red hue value input
gin=13	 #Green hue vaue input
bin=11	 #Blue hue value input
rout=37	#Red hue value output
gout=35	#Green hue value output
bout=33	#Blue hue value output
ts=0.1

oldrinState=1
oldginState=1
oldbinState=1

#Outputs to RGB LED
GPIO.setup(rout,GPIO.OUT)
GPIO.setup(gout,GPIO.OUT)
GPIO.setup(bout,GPIO.OUT)

#Switch inputs with pull-up resistor
GPIO.setup(rin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(gin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(bin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

#PWM State of each output hue value
rState=GPIO.PWM(rout,100)
gState=GPIO.PWM(gout,100)
bState=GPIO.PWM(bout,100)

rVal=0
gVal=0
bVal=0

rState.start(rVal)
gState.start(gVal)
bState.start(bVal)

rBP=0
gBP=0
bBP=0

#Virtual Python Objects
mySphere=sphere(color=color.white,radius=1,pos=vector(0,2.5,0))
myCyl=cylinder(color=color.white,radius=1,length=2.5,axis=vector(0,1,0))
myBase=cylinder(color=color.white,radius=1.3,length=0.25,axis=vector(0,1,0))
myLeg1=box(color=vector(0.4,0.4,0.4),size=vector(0.1,4,0.1),pos=vector(-0.3,-2,0))
myLeg2=box(color=vector(0.4,0.4,0.4),size=vector(0.1,4,0.1),pos=vector(0.3,-2,0))

try:
	while True:
		rate(20)
		rinState=GPIO.input(rin)
		ginState=GPIO.input(gin)
		binState=GPIO.input(bin)
		print('LED Values ',rVal,gVal,bVal)
		sleep(ts)
		if rinState==0 and oldrinState==1:
			print('Red Channel Registered')
			rVal=(1.7760)**rBP
			if rVal>99:
				rVal=0.9
				rBP=-1
			rState.ChangeDutyCycle(int(rVal))
			rBP=rBP+1
		if ginState==0 and oldginState==1:
			print('Green Channel Registered')
			gVal=(1.7760)**gBP
			if gVal>99:
				gVal=0.9
				gBP=-1
			gState.ChangeDutyCycle(int(gVal))
			gBP=gBP+1
		if binState==0 and oldbinState==1:
			print('Blue Channel Registered')
			bVal=(1.7760)**bBP
			if bVal>99:
				bVal=0.9
				bBP=-1
			bState.ChangeDutyCycle(int(bVal))
			bBP=bBP+1
		oldrinState=rinState
		oldginState=ginState
		oldbinState=binState
		mySphere.color=vector(rVal/25,gVal/25,bVal/25)
		myCyl.color=vector(rVal/25,gVal/25,bVal/25)
		myBase.color=vector(rVal/25,gVal/25,bVal/25)
except KeyboardInterrupt:
	rState.stop()
	gState.stop()
	bState.stop()
	GPIO.cleanup()
	print('Goodbye')

