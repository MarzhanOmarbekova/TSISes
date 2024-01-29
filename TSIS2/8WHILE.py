#With the while loop we can execute a set of statements as long as a condition is true.
i = 1
while i < 6:
    print(i)
    i += 1

# break
i = 1
while i < 6 :
    print(i)
    if i == 3:
        break
    i += 1

# With the continue statement we can stop the current iteration, and continue with the next:
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# With the else statement we can run a block of code once when the condition no longer is true:
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

#Exercises
#1
i = 1
while i < 6:
    print(i)
    i += 1

#2
i = 1
while i < 6:
    if i == 3:
        break
    i += 1
#3
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#4
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")