# Imports
import machine
from machine import Pin
import utime
import sys
import os
import micropython
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

def print_color_blocks():
    BLOCK = '   '  # Or '\u2588' * 3 for solid blocks
    # Standard colors
    print(''.join(f"\033[4{i}m{BLOCK}\033[0m" for i in range(8)))

print("Board Variant:", os.uname().machine)
print("Board ID:", machine.unique_id())
print("Platform:", sys.platform)
print("Firmware Version:", sys.version)
print(f"Temperature: {temperature:.2f} °C")
print("CPU Frequency:", machine.freq() // 1000000, "MHz")
print(f"Allocated RAM: {gc.mem_alloc() / 1024:.2f} KB")
print(f"Free RAM: {gc.mem_free() / 1024:.2f} KB")
print("Reset Cause:", machine.reset_cause())
print()
print_color_blocks()