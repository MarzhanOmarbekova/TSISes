#You are given list of numbers separated by spaces. Write a function filter_prime 
#which will take list of numbers as an agrument and returns only prime numbers from the list.
from math import *
def filter_prime(n):
    s = []
    for x in n:
        notp = False 
        for i in range(2, int(sqrt(x)) + 1):
            if x%i == 0:
                notp = True
                break
        if notp == False :
           s.append(x)
    print(s)
    
l = [int(x) for x in input().split()]
filter_prime(l)