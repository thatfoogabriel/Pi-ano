import RPi.GPIO as GPIO
import time

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        try:
            int(num)
            return True
        except ValueError:
            return False

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.OUT)
    servo1 = GPIO.PWM(11, 50)
    servo1.start(0)
    
    while True:
        angle = input("Enter an angle between 0 and 180 (q to exit): ")
        if angle == 'q':
            servo1.ChangeDutyCycle(2)
            time.sleep(0.3)
            break
        if (not isfloat(angle) or float(angle) < 0 or float(angle) > 180):
            print("Invalid Input")
            continue
        angle = float(angle)
        servo1.ChangeDutyCycle(2+(angle/18))
        time.sleep(0.3)
        servo1.ChangeDutyCycle(0)
    servo1.stop()
    GPIO.cleanup()
    print("Goodbye")
    
if __name__ == "__main__":
    main()
