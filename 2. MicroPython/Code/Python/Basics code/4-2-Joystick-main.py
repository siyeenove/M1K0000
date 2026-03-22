# Imports go at the top
from microbit import *

# Joystick
x_axis = pin1
y_axis = pin0
  
def readJoystickValue(axis):
    # Map 0-1023 values to -100 - +100
    return scale(axis.read_analog(), from_=(0, 1023), to=(-100, 100))

# Code in a 'while True:' loop repeats forever
while True:
    if readJoystickValue(x_axis) > 80:        
        display.show('L')
    if readJoystickValue(x_axis) < -80:        
        display.show('R')
    if readJoystickValue(y_axis) > 80:        
        display.show('U')
    if readJoystickValue(y_axis) < -80:        
        display.show('D')
    sleep(100)
