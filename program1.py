import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
GPIO.setup(11,GPIO.OUT, initial=GPIO.LOW)
while True:
   if GPIO.input(7):
      GPIO.output(11,True)
   else:
      GPIO.output(11,False)
