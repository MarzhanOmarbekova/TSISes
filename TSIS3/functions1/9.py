#Write a function that computes the volume of a sphere given its radius.
from math import pi

def volume_sphere(r):
    return (3/4)*pi*(r**2)

r = int(input())
print(volume_sphere(r))