# python simplebeep.py &
# coding: utf-8

import RPi.GPIO as GPIO
import time

SOUNDER = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(SOUNDER, GPIO.OUT, initial = GPIO.LOW)

Hz = 100
p = GPIO.PWM(SOUNDER, 1)

p.start(50)

for i in range(1, 20) :

    p.ChangeFrequency(i * Hz)
    time.sleep(0.5)

p.stop()
GPIO.cleanup()
