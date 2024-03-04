# Write a Python program to count the number of lines in a text file.

with open("text.txt", "r") as file:
    s = sum(1 for line in file)

print(s)