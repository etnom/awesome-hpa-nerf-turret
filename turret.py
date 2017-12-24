# Made for Let's Robot
# By Monty C

from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_StepperMotor, Adafruit_DCMotor
import time
import atexit
import RPi.GPIO as GPIO
import threading

# Wrapper for step(), so stepping will be easier to manage when multitasking motors
def stepperWrapper (self, stepper, numOfSteps, direction):
    stepper.step(numOfSteps, direction, Adafruit_MotorHAT.INTERLEAVE)

class Turret ():