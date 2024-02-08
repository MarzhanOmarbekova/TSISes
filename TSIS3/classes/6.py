from math import sqrt
def filter(n):
    for i in range(2, n):
        if x%i == 0:
            return True
    return False 
    
l = [int(x) for x in input().split()]
l2 = []

f = lambda x : filter(x) 

for x in l:
    if f(x):
        continue
    else:
        l2.append(x)
print(l2)