import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
servo1 = GPIO.PWM(11, 50)
servo2 = GPIO.PWM(12, 50)
servo3 = GPIO.PWM(13, 50)
servo1.start(0)
servo2.start(0)
servo3.start(0)

print("Waiting for 2 seconds...")
time.sleep(2)

print("Rotating 180 degrees in 10 steps...")
duty = 2
while duty <= 12:
    servo1.ChangeDutyCycle(duty)
    servo2.ChangeDutyCycle(duty)
    servo3.ChangeDutyCycle(duty)
    time.sleep(0.3)
    servo1.ChangeDutyCycle(0)
    servo2.ChangeDutyCycle(0)
    servo3.ChangeDutyCycle(0)
    time.sleep(0.5)
    duty += 1
time.sleep(2)

print("Turning back 90 degrees...")
servo1.ChangeDutyCycle(7)
servo2.ChangeDutyCycle(7)
servo3.ChangeDutyCycle(7)
time.sleep(0.5)

print("Waiting for 2 seconds...")
servo1.ChangeDutyCycle(0)
servo2.ChangeDutyCycle(0)
servo3.ChangeDutyCycle(0)
time.sleep(1.5)

print("Turning back to 0 degrees...")
servo1.ChangeDutyCycle(2)
servo2.ChangeDutyCycle(2)
servo3.ChangeDutyCycle(2)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)
servo2.ChangeDutyCycle(0)
servo3.ChangeDutyCycle(0)

servo1.stop()
servo2.stop()
servo3.stop()
GPIO.cleanup()
print("Goodbye")
