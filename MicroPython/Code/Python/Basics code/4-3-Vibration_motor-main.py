# Imports go at the top
from microbit import *

ON = 1
OFF = 0

def setVibrationMotor(OnOrOff):
    if OnOrOff == ON:    # Turn on the vibration motor
        pin2.write_digital(1)
    if OnOrOff == OFF:   # Turn off the vibration motor
        pin2.write_digital(0)

# Code in a 'while True:' loop repeats forever
while True:
    setVibrationMotor(ON)
    sleep(1000)
    setVibrationMotor(OFF)
    sleep(1000)
