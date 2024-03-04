# Write a Python program to write a list to a file.

list = input().split()

with open ("text.txt", "w") as file:
    file.write(" ".join(list))
    