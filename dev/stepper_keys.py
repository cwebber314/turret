"""
Move two stepper motors with keyboard.
"""
import RPi.GPIO as GPIO
import time
from curtsies import Input

GPIO.setmode(GPIO.BCM)

enable_pin = 18
HORIZ_A2 = 26
HORIZ_A1 = 19
HORIZ_B2 = 13
HORIZ_B1 = 6

VERT_A2 = 21
VERT_A1 = 20
VERT_B2 = 16
VERT_B1 = 12

GPIO.setup(enable_pin, GPIO.OUT)

GPIO.setup(HORIZ_A1, GPIO.OUT)
GPIO.setup(HORIZ_A2, GPIO.OUT)
GPIO.setup(HORIZ_B1, GPIO.OUT)
GPIO.setup(HORIZ_B2, GPIO.OUT)

GPIO.setup(VERT_A1, GPIO.OUT)
GPIO.setup(VERT_A2, GPIO.OUT)
GPIO.setup(VERT_B1, GPIO.OUT)
GPIO.setup(VERT_B2, GPIO.OUT)


GPIO.output(enable_pin, 1)

def left(delay, steps):  
  for i in range(0, steps):
    setStepH(1, 0, 1, 0)
    time.sleep(delay)
    setStepH(0, 1, 1, 0)
    time.sleep(delay)
    setStepH(0, 1, 0, 1)
    time.sleep(delay)
    setStepH(1, 0, 0, 1)
    time.sleep(delay)

def right(delay, steps):  
  for i in range(0, steps):
    setStepH(1, 0, 0, 1)
    time.sleep(delay)
    setStepH(0, 1, 0, 1)
    time.sleep(delay)
    setStepH(0, 1, 1, 0)
    time.sleep(delay)
    setStepH(1, 0, 1, 0)
    time.sleep(delay)

def up(delay, steps):  
  for i in range(0, steps):
    setStepV(1, 0, 1, 0)
    time.sleep(delay)
    setStepV(0, 1, 1, 0)
    time.sleep(delay)
    setStepV(0, 1, 0, 1)
    time.sleep(delay)
    setStepV(1, 0, 0, 1)
    time.sleep(delay)

def down(delay, steps):  
  for i in range(0, steps):
    setStepV(1, 0, 0, 1)
    time.sleep(delay)
    setStepV(0, 1, 0, 1)
    time.sleep(delay)
    setStepV(0, 1, 1, 0)
    time.sleep(delay)
    setStepV(1, 0, 1, 0)
    time.sleep(delay)

  
def setStepH(w1, w2, w3, w4):
  GPIO.output(HORIZ_A1, w1)
  GPIO.output(HORIZ_A2, w2)
  GPIO.output(HORIZ_B1, w3)
  GPIO.output(HORIZ_B2, w4)
 
def setStepV(w1, w2, w3, w4):
  GPIO.output(VERT_A1, w1)
  GPIO.output(VERT_A2, w2)
  GPIO.output(VERT_B1, w3)
  GPIO.output(VERT_B2, w4)


GPIO.output(HORIZ_A1, 0)
GPIO.output(HORIZ_A2, 0)
GPIO.output(HORIZ_B1, 0)
GPIO.output(HORIZ_B2, 0)

GPIO.output(VERT_A1, 0)
GPIO.output(VERT_A2, 0)
GPIO.output(VERT_B1, 0)
GPIO.output(VERT_B2, 0)


delay = 5
steps = 1
with Input(keynames='curses') as input_generator:
  for e in input_generator:
    if e == 'a':
      left(int(delay) / 1000.0, int(steps))
    if e == 'd':
      right(int(delay) / 1000.0, int(steps))
    if e == 'w':
      up(int(delay) / 1000.0, int(steps))
    if e == 's':
      down(int(delay) / 1000.0, int(steps))

