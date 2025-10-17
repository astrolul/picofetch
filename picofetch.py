# Imports
import machine
from machine import Pin
import utime
import sys
import os
import micropython
import rp2
import gc

# Switch the pico on-board led on.
led = Pin("LED", Pin.OUT)
led.value(1)

# Print ASCII Art
print(r"""
PPPP  III  CCC   OOO  FFFFF EEEEE TTTTT  CCC  H   H 
P   P  I  C   C O   O F     E       T   C   C H   H 
PPPP   I  C     O   O FFFF  EEEE    T   C     HHHHH 
P      I  C   C O   O F     E       T   C   C H   H 
P     III  CCC   OOO  F     EEEEE   T    CCC  H   H 
---------------------------------------------------""")

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

reading = sensor_temp.read_u16() * conversion_factor

# The temperature sensor measures the Vbe voltage of a biased bipolar diode, connected to the fifth ADC channel
# Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree.
temperature = 27 - (reading - 0.706)/0.001721
print("Temperature:", temperature, "°C")
print("Board ID:", machine.unique_id())
print("Processor:", sys.platform)
print("MicroPython Version:", sys.version)
print("Board Variant:", os.uname().machine)
print("CPU Frequency:", machine.freq())
print("Allocated RAM:", gc.mem_alloc())
print("Free RAM: ", gc.mem_free())
