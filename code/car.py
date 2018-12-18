import RPi.GPIO as GPIO
import time


class Drive:

	def __init__(self):
		self.steer_pin = 12
		self.drive_pin = 13
		self.degree_correction = 0

		GPIO.setwarnings(False)					# Do not show any warnings
		GPIO.setmode (GPIO.BCM)					# Programming the GPIO by BCM pin numbers
		GPIO.setup(self.steer_pin ,GPIO.OUT)	# Initialize pin for steering servo (front)
		GPIO.setup(self.drive_pin ,GPIO.OUT)	# Initialize pin for driving motor (back)
		self.s = GPIO.PWM(self.steer_pin, 50)	# steer_pin (s) as PWM output, with 50Hz frequency
		self.s.start(7.5)						# generate PWM signal with 7.5% duty cycle (90 degrees) 
		self.d = GPIO.PWM(self.drive_pin, 50)	# drive_pin (d) as PWM output, with 50Hz frequency
		self.d.start(0.0)						# generate PWM signal with 0% duty cycle (continuous servo)


	def _degrees_to_duty(self, degrees):
		self.degrees = degrees + self.degree_correction
		# Got this formula by plotting points in Excel and getting the equation.
		duty = 0.05556 * self.degrees + 2.5
		return duty


	def forward(self, seconds=1):
		print('Forward: {} seconds'.format(seconds))
		self.duty = self._degrees_to_duty(90)		# 90 degrees (straight ahead)
		self.s.ChangeDutyCycle(self.duty)
		self.d.ChangeDutyCycle(30)
		time.sleep(seconds)
		self.s.ChangeDutyCycle(90)
		self.d.ChangeDutyCycle(0)


	def reverse(self, seconds=1):
		print('Reverse: {} seconds'.format(seconds))
		self.duty = self._degrees_to_duty(90)		# 90 degrees (straight ahead)
		self.s.ChangeDutyCycle(self.duty)
		self.d.ChangeDutyCycle(1)
		time.sleep(seconds)
		self.s.ChangeDutyCycle(90)
		self.d.ChangeDutyCycle(0)


	def left(self, seconds=1):
		print('Left: {} seconds'.format(seconds))
		self.duty = self._degrees_to_duty(65.0)		# 67.5 degrees is midpt b/n 45 and 90)
		self.s.ChangeDutyCycle(self.duty)
		self.d.ChangeDutyCycle(30)
		time.sleep(seconds)
		self.s.ChangeDutyCycle(90)
		self.d.ChangeDutyCycle(0)


	def right(self, seconds=1):
		print('Right: {} seconds'.format(seconds))
		self.duty = self._degrees_to_duty(115.0)		# 112.5 degrees is midpt b/n 90 and 135)
		self.s.ChangeDutyCycle(self.duty)
		self.d.ChangeDutyCycle(30)
		time.sleep(seconds)
		self.s.ChangeDutyCycle(90)
		self.d.ChangeDutyCycle(0)


