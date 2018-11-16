# coding=utf-8

import PRI.GPIO as GPIO
import time
import signal
import atexit


lightPin = 4  # GPIO Pin 18
lightPin1 = 5 # GPIO Pin 19 


GPIO.setup(lightPin1, GPIO.OUT)
GPIO.output(lightPin1, GPIO.LOW)
time.sleep(0.5)
GPIO.setup(lightPin1, GPIO.IN)


GPIO.setup(lightPin, GPIO.OUT)
GPIO.output(lightPin, GPIO.LOW)
time.sleep(0.5)
GPIO.setup(lightPin, GPIO.IN)


turan = 6 

GPIO.setup(turan, GPIO.OUT)
GPIO.output(turan, GPIO.LOW)
time.sleep(0.5)
GPIO.setup(turan, GPIO.IN)

#atexit.register(GPIO.cleanup)
 

relay = 24 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay, GPIO.OUT)  


servopin = 21  

GPIO.setmode(GPIO.BCM)  
GPIO.setup(servopin, GPIO.OUT, initial=False)  
p = GPIO.PWM(servopin,50) #50HZ  
p.start(0)  
time.sleep(2)
 

while(True):

   t = GPIO.input(turan)
   if (t == GPIO.LOW):
      GPIO.output(relay, GPIO.HIGH)
      time.sleep(1)
   else
       GPIO.output(relay, GPIO.LOW)
       time.sleep(1)
   

   v = GPIO.input(lightPin)
   if (v == GPIO.LOW):
      for i in range(0,180,10):
         p.ChangeDutyCycle(2.5 + 10 * i/180)
         time.sleep(0.02)
         p.ChangeDutyCycle(0)
         time.sleep(0.2)
  else
      v1 = GPIO.input(lightPin1)
      if (v1 == GPIO.LOW):
          for i in range(180,0,-10):
              p.ChangeDutyCycle(2.5 + 10 * i/180)
              time.sleep(0.02)
              p.ChangeDutyCycle(0)
              time.sleep(0.2)

