# Imports go at the top
from microbit import *
import radio

# Joystick
x_axis = pin1
y_axis = pin0

# Button
button_a = pin5
button_b = pin11
button_c = pin12
button_d = pin8

def readButtonValue(button):
    return button.read_digital()
    
def readJoystickValue(axis):
    # Map 0-1023 values to -100 - +100
    return scale(axis.read_analog(), from_=(0, 1023), to=(-100, 100))

# Display image
display.show(Image.HAPPY)
sleep(400)

# Configure the radio
radio.config(group=1, power=3)
radio.on()

# Code in a 'while True:' loop repeats forever
while True:
    if readJoystickValue(x_axis) > 80:
        radio.send('1')
    if readJoystickValue(x_axis) < -80:
        radio.send('2')
    if readJoystickValue(y_axis) > 80:
        radio.send('3')
    if readJoystickValue(y_axis) < -80:
        radio.send('4')

    if readButtonValue(button_a) == 0:
        radio.send('5')
    if readButtonValue(button_b) == 0:
        radio.send('6')
    if readButtonValue(button_c) == 0:
        radio.send('7')
    if readButtonValue(button_d) == 0:
        radio.send('8')

        