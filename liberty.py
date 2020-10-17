from pumpkinpi import PumpkinPi
from time import sleep

# Define a function to control our Pumpkin which takes a PumpkinPi as an argument.
# This script contains flashing LEDs, please take care if you are sensitive to flashing lights.
def pump_pulse(pumpkin):
    pumpkin.sides.left.bottom.pulse(10, 0.5, 1) # Fade in for 5 seconds, fade out for .5 seconds and do this once.
    sleep(.5)
    pumpkin.sides.left.midbottom.pulse(10, 0.5, 1)
    sleep(.5)
    pumpkin.sides.left.middle.pulse(10, 0.5, 1)
    sleep(.5)
    pumpkin.sides.left.midtop.pulse(10, 0.5, 1)
    sleep(.5)
    pumpkin.sides.left.top.pulse(10, 0.5, 1)
    sleep(.5)
    pumpkin.sides.right.top.pulse(10, 0.5, 1)
    sleep(.5)
    pumpkin.sides.right.midtop.pulse(10, 0.5, 1)
    sleep(.5)
    pumpkin.sides.right.middle.pulse(10, 0.5, 1)
    sleep(.5)
    pumpkin.sides.right.midbottom.pulse(10, 0.5, 1)
    sleep(.5)
    pumpkin.sides.right.bottom.pulse(10, 0.5, 1)
    sleep(.5)
    pumpkin.eyes.pulse(5, 0.5, 1)
    sleep(15)

pumpkin = PumpkinPi(pwm=True)

while True:
    pump_pulse(pumpkin)
else:
    pumpkin.close()
