import sys
import RPi.GPIO as GPIO
import time
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
blink_rate=int(input("Blinkrate?"))
runtime=int(input("Runtime?"))
DEBUG=False
if '-debug' in sys.argv:
   DEBUG=True
endTime= time.time() + runtime
startTime = time.time()
LED_PIN=11
SWITCH_PIN=7
LED_STATE=False
loops=0

GPIO.setup(SWITCH_PIN,GPIO.IN)
GPIO.setup(LED_PIN,GPIO.OUT,initial=GPIO.LOW)
with open('data.txt', 'w') as data:
   while time.time() <endTime:
      if GPIO.input(SWITCH_PIN):
         GPIO.output(LED_PIN, LED_STATE)
         LED_STATE=not(LED_STATE)
         time.sleep(blink_rate)
      else:
         GPIO.output(LED_PIN,False)
         LED_STATE=False
         time.sleep(1)
      loops=loops+1
      data.write(f'{time.time():1.0f} {GPIO.input(SWITCH_PIN)}\n')
      if DEBUG:
          t=time.time() - startTime
          print(f'Time: {t} Loops: {loops} State: {LED_STATE}')
GPIO.cleanup()      
