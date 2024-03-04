# Write a Python program to copy the contents of a file to another file

with open("text.txt","r") as file:
    content = file.read()
    
with open("f2.txt","w") as file2:
    file2.write(content)
