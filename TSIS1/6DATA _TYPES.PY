#Example-1
x = 5
print(type(x))

#Example-2 [setting data types ]
x = "Hello World" 
print (type(x)) #str
x = 20
print(type(x)) #int
x = 20.5
print(type(x)) #float
x = 1j
print(type(x)) #complex
x = ["apple","banana","cherry"]
print(x) #list
x = ("apple","banana","cherry")
print(type(x) ) #tuple
x = range (6)
print(type(x)) #range
x = {"name" : "John" , "age": 36}
print(type(x)) #dict
x = {"apple","banana" , "cherry"}
print(type(x)) # set
x = frozenset({"apple","banana","cherry"})
print(type(x)) #frozenset
x = True
print(type(x))  #bool
x = b"Hello" 
print(type(x)) #bytes
x = bytearray(5)
print(type(x)) #bytearray
x = memoryview(bytes(5))
print(type(x) ) #memoryview
x = None
print(type(x)) #NoneType

#Example-3 [setting specific data type]
x = str("Hello World") #str
x = int(20) #int
x = float(20.5)
x = complex(1j)
x = list(("apple","banana","cherry"))
x = tuple(("apple", "banana","cherry"))
x = range(6)
x = dict(name="John",age=36)
x = set(("apple","banana","cherry"))
x = frozenset(("apple","banana","cherry"))
x = bool(5)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))

#exercise-1
x = 1
print(type(x))#int

#exercise-2
x = "Hello World"
print(type(x)) #str

#exercise-3
x = 20.5
print(type(x)) # float

#exercise-4
x = ["apple", "banana" ,"cherry"]
print(type(x)) #list

#exercise-5
x = ("apple", "banana" ,"cherry")
print(type(x)) #tuple

#exercise-6
x = {"name" : "John", "age" : 36}
print(type(x)) #dict 

#exercise-7
x = True
print(type(x)) #bool

