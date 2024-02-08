#Write a function that accepts string from user and print all permutations of that string.
from itertools import permutations

def perm(l):
    permu = permutations(l)
    return(permu)

s = input()
l = [ x for x in s ]

for x in perm(l) :
    string=""
    for y in x :
        string+=y
    print(string)