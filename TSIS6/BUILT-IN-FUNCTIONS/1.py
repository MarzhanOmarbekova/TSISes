# Write a Python program with builtin function to multiply all the numbers in a list

import math

list = [int(x) for x in input().split()]

print(math.prod(list))