from random import randint
print("Hello! What is your name?")
name = input()
print("\nWell, " + name + ", I am thinking of a number between 1 and 20.")
num = randint(1,20)
guess = 0
tries = 0
while num != guess :
    tries += 1
    print("Take a guess.")
    guess = int(input())
    if guess == num :
        print("\nGood job, " + name + "! You guessed my number in " + str(tries) +" guesses!")
    elif guess < num :
        print("\nYour guess is too low.")
    else:
        print("\nYour guess is too high.")
