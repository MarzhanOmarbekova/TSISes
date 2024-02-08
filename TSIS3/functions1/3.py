#Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
#How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):

def solve(numheads,numlegs):
    rabbits =int( (numlegs - numheads * 2 ) / 2)
    tauktar = int(numheads - rabbits)
    return rabbits, tauktar

numheads = int(input())
numlegs = int(input())

print("rabbits" , solve(numheads,numlegs)[0] , "tauktar" , solve(numheads,numlegs)[1])
