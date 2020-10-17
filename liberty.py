from pumpkinpi import PumpkinPi
from time import sleep

# Define a function to control our Pumpkin which takes a PumpkinPi as an argument.
# This script contains flashing LEDs, please take care if you are sensitive to flashing lights.
def pump_pulse(pumpkin):
    pumpkin.sides.left.bottom.pulse(20, 0.5, 1) # Fade in for 5 seconds, fade out for .5 seconds and do this once.
    sleep(.5)
    pumpkin.sides.left.midbottom.pulse(18, 0.5, 1)
    sleep(.5)
    pumpkin.sides.left.middle.pulse(16, 0.5, 1)
    sleep(.5)
    pumpkin.sides.left.midtop.pulse(14, 0.5, 1)
    sleep(.5)
    pumpkin.sides.left.top.pulse(12, 0.5, 1)
    sleep(.5)
    pumpkin.sides.right.top.pulse(10, 0.5, 1)
    sleep(.5)
    pumpkin.sides.right.midtop.pulse(8, 0.5, 1)
    sleep(.5)
    pumpkin.sides.right.middle.pulse(6, 0.5, 1)
    sleep(.5)
    pumpkin.sides.right.midbottom.pulse(4, 0.5, 1)
    sleep(.5)
    pumpkin.sides.right.bottom.pulse(2, 0.5, 1)
    sleep(.5)
    pumpkin.eyes.blink(.1, .1, 0, 0, 12) # Blink on for .1 seconds, off for .1 seconds, do not fade and do this 12 times.
    sleep(3)
    pumpkin.eyes.blink(.1, .1, 0, 0, 12) # Blink on for .1 seconds, off for .1 seconds, do not fade and do this 12 times.
    sleep(5)

pumpkin = PumpkinPi(pwm=True)

while True:
    pump_pulse(pumpkin)
else:
    pumpkin.close()
