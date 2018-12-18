import RPi.GPIO as GPIO
import time

drivepin = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(drivepin, GPIO.OUT)

pwm_d = GPIO.PWM(drivepin, 50)
pwm_d.start(0)


if __name__ == '__main__':
	pwm_d.ChangeDutyCycle(1)	# 30 is forward
	time.sleep(1.5)
