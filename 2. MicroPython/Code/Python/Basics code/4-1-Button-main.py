# Imports go at the top
from microbit import *

# Button
button_a = pin5
button_b = pin11
button_c = pin12
button_d = pin8

def readButtonValue(button):
    return button.read_digital()

# Code in a 'while True:' loop repeats forever
while True:
    if readButtonValue(button_a) == 0:
        display.show('A')
    if readButtonValue(button_b) == 0:
        display.show('B')
    if readButtonValue(button_c) == 0:
        display.show('C')
    if readButtonValue(button_d) == 0:
        display.show('D')
    sleep(100)
