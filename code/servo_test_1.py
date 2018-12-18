# https://circuitdigest.com/microcontroller-projects/raspberry-pi-pwm-tutorial

servopin = 12
#servopin = 19

import RPi.GPIO as IO 	# calling for header file for GPIOs of PI
import time		# calling for time to provide delays in program

IO.setwarnings(False)		# do not show any warnings
IO.setmode (IO.BCM)		# programming the GPIO by BCM pin numbers. (like PIN29 as 'GPIO5')
IO.setup(servopin ,IO.OUT)	# initialize GPIO19 as an output

p = IO.PWM(servopin,50)	# GPIO19 as PWM output, with 50Hz frequency
p.start(7.5)		# generate PWM signal with 7.5% duty cycle

while 1:				# execute loop forever
	#p.ChangeDutyCycle(7.5)		# change duty cycle for getting the servo position to 90 deg
	#time.sleep(1)			# sleep for 1 second
	#p.ChangeDutyCycle(12.5)		# change duty cycle for getting the servo position to 180 deg
	#time.sleep(1)			# sleep for 1 second
	#p.ChangeDutyCycle(2.5)		# change duty cycle for getting the servo position to 0 deg
	#time.sleep(1)			# sleep for 1 second
	p.ChangeDutyCycle(6.11)         # LEFT
	time.sleep(1)                   # sleep for 1 second
	p.ChangeDutyCycle(8.89)			# RIGHT
	time.sleep(1)                   # sleep for 1 second
