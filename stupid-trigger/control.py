import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)


def triggerFan():
    print "LED on"
    GPIO.output(18,GPIO.LOW)
    time.sleep(3)
    print "LED off"
    GPIO.output(18,GPIO.HIGH)

    GPIO.cleanup()

triggerFan()