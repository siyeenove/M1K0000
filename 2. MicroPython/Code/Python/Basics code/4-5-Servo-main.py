# Imports go at the top
from microbit import *

# Define servo pin
servo1 = pin13
servo2 = pin14
servo3 = pin15
servo4 = pin16

# Servo control function
# Set steering Angle (0-180 degrees)
def setServoAngle(pin, angle):
    # The period of the PWM signal is set to 20ms.
    pin.set_analog_period(20)
    
    # Convert Angle to pulse width (0.5ms-2.5ms)
    pulse_width = 500 + (angle * 2000 / 180)
    
    # Set PWM signal (20ms period)
    pin.write_analog(int(pulse_width / 20000 * 1023))

# Code in a 'while True:' loop repeats forever
while True:
    # 0 degrees
    setServoAngle(servo1, 0)
    setServoAngle(servo2, 0)
    setServoAngle(servo3, 0)
    setServoAngle(servo4, 0)
    sleep(2000)
    # 180 degrees
    setServoAngle(servo1, 180)
    setServoAngle(servo2, 180)
    setServoAngle(servo3, 180)
    setServoAngle(servo4, 180)
    sleep(2000)
