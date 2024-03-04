# Write a Python program that invoke square root function after specific milliseconds.

from time import sleep
from math import sqrt

num = int(input())
millisecond = int(input())

sleep(millisecond/1000)

print(f"Square root of {num} after {millisecond} miliseconds is {sqrt(num)}")