#Example 1
thislist = ["apple", "banana" , "cherry"]
print(thislist )

#Example 2[duplicate values]
thislist = ["apple","banana","cherry","apple","cherry"]
print(thislist)

#Example 3 [len of list]
thislist = ["apple","banana","cherry"]
print(len(thislist))

#Example 4 {any data type}
list1 = ["apple","banana","cherry"]
list2 = [1,5,7,9,3]
list3 = [True,False,False]

#Example 4[different types]
list1 = ["abc",34,True , 40, "male"]

#Example 5 [type()]
mylist = ["apple", "banana", "cherry"]
print(type(mylist)) #list

#Example 6 [list()]
thislist = list(("apple","banana","cherry"))
print(thislist)

#ACCESS LIST ITEMS
#Example 1 [access by index]
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Example 2 [negative indexes]
thislist = ["apple", "banana","cherry"]
print(thislist[-1])

#Example 3 [range of indexes ]
thislist =["apple","banana","cherry","orange",'kiwi','melon',"mango"]
print(thislist[2:5])# The search will start at index 2 (included) and end at index 5 (not included).

#Example 4
thislist = ["apple","banana","cherry","orange",'kiwi','melon',"mango"]
print(thislist[:4]) 

#Example 5
thislist = ["apple","banana","cherry","orange",'kiwi','melon',"mango"]
print(thislist[2:])

#Example 6
thislist = ["apple","banana","cherry","orange",'kiwi','melon',"mango"]
print(thislist[-4:-1])

#Example 7 [keyword 'in']
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist :
    print("Yes, 'apple' is in th fruits list" )

#CHANGE LIST ITEMS
#Example 1
thislist = ["apple","banana","cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Example 2 [ change range]
thislist = ["apple","banana","cherry","orange",'kiwi','melon',"mango"]
thislist[1:3] = ["blackcurrant","watermelon"]
print(thislist)

#Example 3 [If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:]
thislist = ["apple","banana","cherry"]
thislist[1:2] = ["blackcurrant","watermelon"]
print(thislist) # ['apple', 'blackcurrant', 'watermelon', 'cherry']

#Example 4 [If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:]
thislist = ["apple","banana","cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) #['apple', 'watermelon']

#Example 5 [ insert items]
thislist = ["apple","banana","cherry"]
thislist.insert(2,"watermelon")
print(thislist)

#ADD LIST ITEMS
#Example 1 [append items to the end]
thislist = [ "apple", "banana", "cherry" ]
thislist.append("orange")
print(thislist)

#Example 2 [insert items]
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#Example 3 [extend () to append el-s from another lost to the current]
thislist = ["apple", "banana", "cherry"]
tropical = ["mango","pineapple","papaya"]
thislist.extend(tropical)
print(thislist)

#Example 4 [extend() can add any iterible object (tuples, sets, dictionaries etc.)]
thislist = ["apple", "banana", "cherry" ]
thistuple =("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#REMOVE LIST ITEMS
#Example 1 [remove()]
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Example 2 [If there are more than one item with the specified value, the remove() method removes the first occurance:]
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#Example 3 [pop() removes the specified index]
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#Example 4 [If you do not specify the index, the pop() method removes the last item]
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#Example 5 [keyword del removes the specified index]
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#Example 6 [del can delete the list]
thislist = ["apple", "banana", "cherry"]
del thislist

#Example 7 [clear() The clear() method empties the list. The list still remains, but it has no content.]
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#LOOP LISTS
#Example 1 
thislist = ["apple", "banana", "cherry"]
for x in thislist :
    print(x)

#Example 3
thislist = ["apple", "banana", "cherry"]
for i in range (len(thislist)):
    print(thislist[i])

#Example 4
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

#Example 5
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#LIST COMPREHENSION
#Example 1 [list with for loop]
fruits = ["apple","banana", "cherry","kiwi","mango"]
newlist = []
for x in fruits:
    if "a" in x :
        newlist.append(x)
print (newlist)
#[with list comprehension]
fruits = ["apple", "banana", "cherry","kiwi","mango"]
newlist = [x for x in fruits  if "a" in x]
print(newlist)

#the syntax
newlist = [ expression for item in iterible if condition ==True ]

#no if statement 
newlist = [x for x in fruits]

#iterible   with a range 
newlist = [ x for x in range(10)]

#with range and if
newlist = [x for x in range (10) if x<5]

#we can maniuplate  before it ends up like a list item
newlist = [ x.upper() for x in fruits]

#You can set the outcome to whatever you like:
newlist =['hello' for x in fruits]

#The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome
newlist = [x if x != "banana" else "orange" for x in fruits]
#"Return the item if it is not banana, if it is banana return orange".

#SORT LISTS
# sort()
thislist = ["orange","mango","kiwi","pineapple","banana"]
thislist.sort()
print(thislist)

#sort the list descending
thislist = ["orange","mango","kiwi","pineapple","banana"]
thislist.sort(reverse =True)
print(thislist)

#sort function  [You can also customize your own function by using the keyword argument key = function.The function will return a number that will be used to sort the list (the lowest number first):]
def myfunc(n):
    return abs(n-50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#sort id case sensitive , esulting in all capital letters being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#if you want a case-insensitive sort function, use str.lower as a key function
thislist.sort(key = str.lower)
print(thislist)

#just reverse
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#COPY LISTS
#copy()
thislist = ["apple","banana","cherry"]
mylist = thislist.copy()
print(mylist)

#list()
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#JOIN LISTS
# JOIN WITH +
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#by appending in for loop
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#by extend()
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#Exercise 1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#Exercise 2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

#Exercise 3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#Exercise 4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

#Exercise 5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#Exercise 6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#Exercise 7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#Exercise 8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))