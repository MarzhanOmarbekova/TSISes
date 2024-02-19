#Write a Python program to calculate the area of a trapezoid.
#Height: 5
#Base, first value: 5
#Base, second value: 6
#Expected Output: 27.5

def area_trapezoid(h,a,b):
    print(h*(1/2)*(a+b)) 

area_trapezoid(float(input("Height: ")),float(input("Base, first value: ")),float(input("Base, second value: ")))