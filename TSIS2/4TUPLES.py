#create tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuples allow duplicate values:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#len() function
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#One item tuple, remember the comma:

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) #str

#any data type
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#different data types
tuple1 = ("abc", 34, True, 40, "male")

#data type of tuple is tuple
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#Using the tuple() method to make a tuple:

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#ACCESS TUPLE ITEMS
#WITH INDEX
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#negative indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

# a range of indexes , the return value will be a new tuple with the specified items
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#To determine if a specified item is present in a tuple use the in keyword:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

#UPDATE TUPLES
#change tuple values
x = S("apple","banana","cherry")
y = list(x)
y[1] = "kiwi"
x=tuple(y)
print(x)

#add items
# 1 convert into a list
thistuple = ("apple","banana","cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#add tuple to a tuple 
thistuple = ("apple","banana","cherry")
y = ("orange",)
thistuple += y
print(thistuple)

#remove items
thistuple = ("apple","banana","cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#delete tuple completely 
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #error because the tuple doesnt exist

#unpack tuples
#packing is When we create a tuple, we normally assign values to it
fruits = ("apple", "banana", "cherry")

#unpacking
fruits = ("apple","banana","cherry")
(green , yellow , red) = fruits
print(green)
print (yellow)
print(red)

#using asterisk *
#If the number of variables is less than the number of values, you can add an * to the variable name
# and the values will be assigned to the variable as a list:
fruits = ("apple","banana",'cherry',"strawberry","raspberry")
(green,yellow, *red) = fruits
print(green)
print(yellow)
print(red)

#If the asterisk is added to another variable name than the last, 
#Python will assign values to the variable until the number of values left matches the number of variables left.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#LOOP TUPLES
#loop through the tuple items
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
#with indexes
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])
#using while loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

#JOIN TUPLES
# + operator
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

#multiply tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

# Exercises
# 1
fruits = ("apple", "banana", "cherry")
print(fruits[0])
# 2
fruits = ("apple", "banana", "cherry")
print(len(fruits))
# 3 
fruits = ("apple", "banana", "cherry")
print(fruits[-1])
# 4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])
