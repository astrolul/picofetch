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
print('\033[1m' + r"""
PPPP  III  CCC   OOO  FFFFF EEEEE TTTTT  CCC  H   H 
P   P  I  C   C O   O F     E       T   C   C H   H 
PPPP   I  C     O   O FFFF  EEEE    T   C     HHHHH 
P      I  C   C O   O F     E       T   C   C H   H 
P     III  CCC   OOO  F     EEEEE   T    CCC  H   H 
---------------------------------------------------""" + '\033[0m')

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

cause = machine.reset_cause()

print('\033[1m' + "Board Variant:" + '\033[0m', os.uname().machine)
print('\033[1m' + "Board ID:" + '\033[0m', machine.unique_id())
print('\033[1m' + "Platform:" + '\033[0m', sys.platform)
print('\033[1m' + "Firmware Version:" + '\033[0m', sys.version)
print(f"\033[1mTemperature:\033[0m {temperature:.2f} °C")
print('\033[1m' + "CPU Frequency:" + '\033[0m', machine.freq() // 1000000, "MHz")
print(f"\033[1mAllocated RAM:\033[0m {gc.mem_alloc() / 1024:.2f} KB")
print(f"\033[1mFree RAM:\033[0m {gc.mem_free() / 1024:.2f} KB")

if cause == machine.PWRON_RESET:
    print('\033[1m' + "Reset Cause:" + '\033[0m', "PWRON_RESET")
elif cause == machine.WDT_RESET:
    print('\033[1m' + "Reset Cause:" + '\033[0m', "WDT_RESET")
elif cause == machine.DEEPSLEEP_RESET:
    print('\033[1m' + "Reset Cause:" + '\033[0m', "DEEPSLEEP_RESET")
elif cause == machine.SOFT_RESET:
    print('\033[1m' + "Reset Cause:" + '\033[0m', "SOFT_RESET")
elif cause == machine.HARD_RESET:
    print('\033[1m' + "Reset Cause:" + '\033[0m', "HARD_RESET")
else:
    print('\033[1m' + "Reset Cause:" + '\033[0m', "N/A")

print()
print_color_blocks()