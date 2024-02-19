# 5 Implement a generator that returns all numbers from (n) down to 0.

def int_n_0(n):
    while n>=0:
        yield n
        n -= 1 

iter = int_n_0(int(input()))
for i in iter:
    print(i,end=" ")