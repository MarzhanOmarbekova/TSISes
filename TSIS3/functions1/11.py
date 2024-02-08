#Write a Python function that checks whether a word or phrase is palindrome or not.
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
def is_pal(s):
    if(s == s[::-1]):
        return True
    return False

s = input()
print(is_pal(s))