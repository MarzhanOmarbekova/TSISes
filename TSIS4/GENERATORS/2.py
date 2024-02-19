# 2 Write a program using generator to print the even numbers between 0 and n
# in comma separated form where n is input from console.

def evens(n):
    for i in range(n+1):
        if i % 2 == 0 :
            yield i 

print(", ".join(list(map(str, evens(int(input()))))))