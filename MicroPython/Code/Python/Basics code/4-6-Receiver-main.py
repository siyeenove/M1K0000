# Imports go at the top
from microbit import *
import radio

# Display image
display.show(Image.HEART)
sleep(400)

# Configure the radio
radio.config(group=1)
radio.on()

# Code in a 'while True:' loop repeats forever
while True:
    message = radio.receive()
    if message == '1':
        display.show(1)  
    elif message == '2':
        display.show(2) 
    elif message == '3':
        display.show(3)
    elif message == '4':
        display.show(4)
    elif message == '5':
        display.show(5)
    elif message == '6':
        display.show(6)
    elif message == '7':
        display.show(7)
    elif message == '8':
        display.show(8)

     

