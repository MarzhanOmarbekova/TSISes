#print each in list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
#looping through a string
for x in "banana":
    print(x)

#With the break statement we can stop the loop before it has looped through all the items:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

#Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

#With the continue statement we can stop the current iteration of the loop, and continue with the next:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

#range()
for x in range(6):
    print(x)

#range(2, 6), which means values from 2 to 6 (but not including 6):
for x in range(2, 6):
    print(x)

#it is possible to specify the increment value by adding a third parameter:
for x in range(2, 30, 3):
    print(x)

#else will be executed after loop
for x in range(6):
    print(x)
else:
    print("Finally finished!")

# The else block will NOT be executed if the loop is stopped by a break statement.
for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")

#nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

#pass
for x in [0, 1, 2]:
    pass

#Exercises
#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

#3
for x in range(6):
    print(x)

#4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)