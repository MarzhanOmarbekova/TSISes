from math import *
def filter_prime(n):
    l = n.copy()
    for x in n:
        for i in range(2,int(sqrt(x))+1):
            if x%i == 0 :
                l.remove(x)
    print(l)

l = [ int(x) for x in input().split()]
filter_prime(l)