#A set is a collection which is unordered, unchangeable*, and unindexed.
# with curly brackets
thisset = {"apple","banana","cherry"}
print(thisset)

# no  duplicates 
thisset = {"apple","banana","cherry","apple"}
print(thisset) #{'banana', 'cherry', 'apple'}

# True ==1
thisset = {"apple", "banana", "cherry",True, 1 ,2}
print (thisset) #{True, 2, 'banana', 'cherry', 'apple'}

#False == 0
thisset = {"apple","banana","cherry",False , True , 0}
print(thisset) #{False, True, 'cherry', 'apple', 'banana'}

# len()
thisset = {"apple","banana", "cherry"}
print(len(thisset))

# any type
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#  different data types
set1 = {"abc",34,True,40,"male"}

# set() constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#ACCESS SET ITEMS
# Loop through the set, and print the values:
thisset = {"apple","banana","cherry"}
for x in thisset :
    print(x)
# check if in set
thisset = {"apple","banana","cherry"}
print("banana" in thisset)

#add() method
thisset = {"apple", "banana","cherry"}
thisset.add("orange")
print(thisset)

# update() method to add from another set
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple","mango","papaya"}
thisset.update(tropical)

#update can add any iterable object (dict,list,tuple)
thisset = {"apple","banana","cherry"}
mylist = ["kiwi","orange"]
thisset.update(mylist)
print(thisset) #{'banana', 'cherry', 'apple', 'orange', 'kiwi'}

#REMOVE ITEMS
#remove()
thisset = {"apple","banana","cherry"}
thisset.remove("banana")
print(thisset)
# Note: If the item to remove does not exist, remove() will raise an error.

#discard()
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
#Note: If the item to remove does not exist, discard() will NOT raise an error.

#pop()
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #removed item
print(thisset) #the set after removal
#Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed

#The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

#LOOP SETS
thisset = {"apple","banana","cherry"}
for x in thisset :
    print(x)

#JOIN SETS
#with union()
set1 = {"a","b","c"}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3)

#The update() method inserts the items in set2 into set1
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#The intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

#The intersection() method will return a new set, that only contains the items that are present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

#The symmetric_difference_update() method will keep only the elements
# that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

#set methods : https://www.w3schools.com/python/python_sets_methods.asp

#Exercises
#1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!")

#2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
