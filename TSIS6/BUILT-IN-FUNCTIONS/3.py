# Write a Python program with builtin function that checks whether a passed string is palindrome or not.

def is_pal(string):
    rev_str = "".join(reversed(string))
    return rev_str == string

string = input()
if is_pal(string) :
    print(f"{string} is palindrome" )
else:
    print(f"{string} is not palindrome")