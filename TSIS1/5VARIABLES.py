# VARIABLES
#Example-1
x = 5 
y = "John"
print(x) 
print(y)

#Example-2[change type]
x = 4       # x is of type int
x = "Sally" # x is now of type str 
print(x)

#Example-3 [specify type ]
x = str(3)   # x will be '3'
y = int(3)   # y will be 3
z = float(3) # z will be 3.0

#Exapmle-4 [ type() ]
x = 5
y = "John"
print(type(x))
print(type(y))

#Example-5 [single / double quotes]
x = "John"
# is the same as 
x = 'John'

#Example-6 [case-sensitive]
a = 4
A = "Sally"
# A will not overwrite a

#VARIABLE NAMES
#Example-1 [legal variable names]
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Example-2 [Illegal names]
"""
2myvar = "John"
my-var = "John"
my var = "John"
"""

#ASSIGN MULTIPLE VALUES
#Example-1 [multiple values to multiple variables]
x , y , z = "Orange" , "Banana" , "Cherry"
print(x)
print(y)
print(z)
#Example-2 [one value to multiple variables]
x = y = z = "Orange"
print(x)
print(y)
print(z)
#Example-3 [Unpack a list]
fruits = ["apple", "banana" , "cherry"]
x, y, z  = fruits
print(x)
print(y)
print(z)

#OUTPUT VARIABLES
#Example-1 [print()]
x = "Python is awesome"
print(x)

#Example-2 [sep by comma]
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
 
#Exapmle-3 [+]
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#Example-4 [+ for math]
x = 5
y = 10
print(x + y)

#Example-5 [+ error when int+str]
x = 5
y = "John"
print(x + y)

#Example-6 [comma int, str]
x = 5
y = "John"
print(x , y)

#GLOBAL VARIABLES
#Example-1 [outside of function]
x = "awesome"

def myfunc():
    print("Python is " + x)
myfunc()

#Example-2 
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x )
myfunc () # Python is fantastic

print("Python is " + x ) #Python is awesome

#Example-3 [To create a global variable inside a function, you can use the global keyword]
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x )

#Example-4 [To change the value of a global variable inside a function, refer to the variable by using the global keyword:]
x = "awesome"
def myfunc():
    global x
    x = "fantastic"
myfunc()

print("Python is "+ x)

#execise-1
carname =  "Volvo"

#exercise-2
x = 50

#exercise-3
x = 5
y = 10
print(x+y)

#exercise-4
x = 5
y = 10
z= x + y 
print(z)

#exercise-5
x, y, z ="Orange", 'Banana' , "Cherry"

#exercise-6
x = y = z = "Orange"

#exercise-7
def myfunc():
    global x
    x = "fantastic"