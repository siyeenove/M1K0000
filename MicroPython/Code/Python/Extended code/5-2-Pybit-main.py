# Imports go at the top
from microbit import *
import radio
import speech

# Car I2C address
i2cAddr = 0x2a

# For wheels
leftwheel  = 0
rightwheel = 1
backward = 0
forward  = 1
i2cBuf = bytearray([0x00, 0x00])

# For head RGB LED
leftLed  = 0
rightLed = 1

# Set the wheel speed function
# wheel: 0 = left wheel, 1 = right wheel
# direction: 0 = backward, 1 = forward
# speed: 0--100
def setWheelSpeed(wheel, direction, speed):
    # Important! The speed is between 0 and 100.
    if speed > 100:      
        speed = 100
    elif speed < 0:
        speed = 0

    if wheel == leftwheel:          
        i2cBuf[0] = 0x05  # left wheel register 
        if direction == forward:
            # speed value, 101 is the default required data.
            i2cBuf[1] = speed + 101     
        elif direction == backward:
            i2cBuf[1] = speed
        i2c.write(i2cAddr, i2cBuf)

    if wheel == rightwheel:         
        i2cBuf[0] = 0x06  # right wheel register
        if direction == forward:
            i2cBuf[1] = speed     
        elif direction == backward:
            # speed value, 101 is the default required data.
            i2cBuf[1] = speed + 101
        i2c.write(i2cAddr, i2cBuf)

# Set the head RGB LED function
# led: 0 is the left led and 1 is the right LED.
# r: red brightness value
# g: green brightness value
# b: blue brightness value
def setHeadRgbLed(led, r, g, b):
    if led == leftLed:          
        i2cBuf[0] = 0x07  # red register 
        i2cBuf[1] = r     # red brightness value
        i2c.write(i2cAddr, i2cBuf)
        i2cBuf[0] = 0x08  # green register
        i2cBuf[1] = g     # green brightness value
        i2c.write(i2cAddr, i2cBuf)
        i2cBuf[0] = 0x09  # blue register
        i2cBuf[1] = b     # blue brightness value
        i2c.write(i2cAddr, i2cBuf)
    if led == rightLed:         
        i2cBuf[0] = 0x0a  # red register
        i2cBuf[1] = r     # red brightness value
        i2c.write(i2cAddr, i2cBuf)
        i2cBuf[0] = 0x0b  # green register
        i2cBuf[1] = g     # green brightness value
        i2c.write(i2cAddr, i2cBuf)
        i2cBuf[0] = 0x0c  # blue register
        i2cBuf[1] = b     # blue brightness value
        i2c.write(i2cAddr, i2cBuf)
        
# Display image
display.show(Image.HAPPY)
sleep(400)

# Configure the radio
radio.config(group=1)
radio.on()

# Code in a 'while True:' loop repeats forever
while True:
    message = radio.receive()
    if message == '1':
        # Turn right at place
        setWheelSpeed(leftwheel, forward, 60)
        setWheelSpeed(rightwheel, backward, 60)  
    elif message == '2':
        # Turn left at place
        setWheelSpeed(leftwheel, backward, 60)
        setWheelSpeed(rightwheel, forward, 60)
    elif message == '3':
        # Forward
        setWheelSpeed(leftwheel, forward, 100)
        setWheelSpeed(rightwheel, forward, 100) 
    elif message == '4':
        # Backward
        setWheelSpeed(leftwheel, backward, 100)
        setWheelSpeed(rightwheel, backward, 100) 
    elif message == '5':
        # Speech
        speech.say('Hello, world. How are you?')
    elif message == '6':
        setHeadRgbLed(leftLed, 0, 255, 0)    # green    
        setHeadRgbLed(rightLed, 0, 255, 0)  
    elif message == '7':
        setHeadRgbLed(leftLed, 0, 0, 255)    # blue
        setHeadRgbLed(rightLed, 0, 0, 255)
    elif message == '8':
        setHeadRgbLed(leftLed, 0, 0, 0)      # back
        setHeadRgbLed(rightLed, 0, 0, 0)
    else:
        # Stop
        setWheelSpeed(leftwheel, backward, 100)
        setWheelSpeed(rightwheel, backward, 100)
    sleep(200)
     

