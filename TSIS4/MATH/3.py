# Write a Python program to calculate the area of regular polygon.
# Input number of sides: 4
# Input the length of a side: 25
# The area of the polygon is: 625

from math import *
def area_reg_polygon(sides,len):
    print(sides/4*len**2*(1/(tan(radians(180/sides)))))

sides = float(input("Input number of sides: "))
length = float(input("Input the length of a side: "))
print("The area of the polygon is: ")
area_reg_polygon(sides,length)