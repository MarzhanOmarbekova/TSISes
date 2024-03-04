# Write a Python program with builtin function that accepts a string
# and calculate the number of upper case letters and lower case letters

def num_of_letterS(dtring):
    up = sum(1 for let in string if let.isupper())
    low = sum(1 for let in string if let.islower())
    return up , low

string = input()
up , low = num_of_letterS(string)
print(f"number of upper letters {up}")
print(f"number of lower letters {low}")