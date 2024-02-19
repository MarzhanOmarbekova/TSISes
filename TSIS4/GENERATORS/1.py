# 1 Create a generator that generates the squares of numbers up to some number N.

def squares(start , end):
    while start <= end :
        yield str(start**2)
        start +=1

print(", ".join(list(squares(int(input()),int(input())))))