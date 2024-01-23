#Example 1
print('Hello')
#is same as
print("Hello")

#Example 2
a = "Hello"
print(a)

#example 3 
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#OR
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Example 4
a = "Hello, World!"
print(a[1])

#Example 5
for x in "banana":
    print(x)

#Example 6
a = "Hello, World!"
print(len(a))

#Example 7 [keyword in]
txt = "The best things in life are free!"
print("free" in txt)

#Example 8 
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

#Example 9 [keyword not in]
if "expensive" not in txt :
    print("expensive' is NOT present.")

#SLICING
#Example 1 [slice syntax [start:end not included]]
b = "Hello, World!"
print(b[2:5])
#from the start
print(b[:5])
#to the end
print(b[2:])
#neg indexes  last not included
print(b[-5:-2])

#MODIFY STRINGS
#Example 1
a = "Hello, World!"
print(a.upper())
#Example 2
a = "Hello, World!"
print(a.lower())
#Example 3
print(a.strip()) #removes whitespaces from beginning or end
#Example 4
print(a.replace("H","J"))
#Example 5
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#CONCATENATE STRs
#Example 1
a = "Hello"
b = "World"
c = a + b
print(c)
#Example 2 [To add a space between them, add a " ":]
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#FORMAT-STRINGS
#Example 1
age=36
txt = "My name is John, and I am {}"
print(txt.format(age))

#Example 2
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#Example 3
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#ESCAPE CHARACTERS
#Example 1 [An escape character is a backslash \ followed by the character you want to insert.]
txt = "We are the so-called \"Vikings\" from the north."

#EXERCISE 1
x = "Hello World"
print(len(x))
#EXERCISE 2
txt = "Hello World"
x = txt[0]
#EXERCISE 3
txt = "Hello World"
x = txt[2:5]
#EXERCISE 4
txt = " Hello World "
x = txt.strip()
#EXERCISE 5
txt = "Hello World"
txt = txt.upper()
#EXERCISE 6
txt = "Hello World"
txt = txt.lower()
#EXERCISE 7
txt = "Hello World"
txt = txt.replace("H", "J")
#EXERCISE 8
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))