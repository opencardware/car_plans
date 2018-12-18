åimport RPi.GPIO as GPIO
import time

servopin = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(servopin, GPIO.OUT)

pwm_s = GPIO.PWM(servopin, 50)

pwm_s.start(0)

def update(angle):
	duty = angle / 18 + 2
	GPIO.output(servopin, True)
	pwm_s.ChangeDutyCycle(duty)
	time.sleep(1)
	GPIO.output(servopin, False)
	pwm_s.ChangeDutyCycle(0)

if __name__ == '__main__':
	update(90)
	pwm_s.ChangeDutyCycle(30)
	time.sleep(3)
	pwm_s.ChangeDutyCycle(0)
	update(30)
	time.sleep(1)
	GPIO.cleanup()

