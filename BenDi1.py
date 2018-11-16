# coding=utf-8

import sys
import RPi.GPIO as GPIO
import time
import signal
import atexit

#设定GPIO 使用板物理引脚模式
GPIO.setmode(GPIO.BOARD)

#设定光敏传感器 
lightPin = 7
lightPin1 = 11

#设定引脚输入模式
GPIO.setup(lightPin, GPIO.IN)
time.sleep(0.5)
GPIO.setup(lightPin1, GPIO.IN)

#土壤检测传感器
turan = 13
GPIO.setup(turan, GPIO.IN)
time.sleep(0.5)

relay = 15
GPIO.setup(relay, GPIO.OUT)

#设定舵机控制
servopin = 40
GPIO.setup(servopin, GPIO.OUT, initial=False)
#设定频率50HZ  
p = GPIO.PWM(servopin, 50)
p.start(0)
time.sleep(2)

while(True):
    
    #检测土壤湿度
    t = GPIO.input(turan)
    if (t == GPIO.LOW):
        GPIO.output(relay, GPIO.HIGH)
        time.sleep(1)
    else:
        GPIO.output(relay, GPIO.LOW)
        time.sleep(1)
    
    v = GPIO.input(lightPin)
    if (v == GPIO.LOW):
        for i in range(0,180,10):
            p.ChangeDutyCycle(2.5 + 10 * i/180)
            time.sleep(0.02)
            p.ChangeDutyCycle(0)
            time.sleep(0.2)
    else:
        v1 = GPIO.input(lightPin1)
        if (v1 == GPIO.LOW):
            for i in range(180,0,-10):
                p.ChangeDutyCycle(2.5 + 10 * i/180)
                time.sleep(0.02)
                p.ChangeDutyCycle(0)
                time.sleep(0.2)

