#Write a Python program to calculate the area of a parallelogram.
#Length of base: 5
#Height of parallelogram: 6
#Expected Output: 30.0

def area_parallelogram(len,h):
    print(len*h)

length = float(input("Length of base: "))
h = float(input("Height of parallelogram: "))
area_parallelogram(length,h)