#Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We

def rev_str(s):
    return (s[::-1])

s =  input().split()
for x in rev_str(s):
    print(x, end=" ")