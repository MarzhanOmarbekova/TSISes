#Examples
# 1
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : 1964
}
print(thisdict["brand"])

#duplicate values will overwrite existing values
thisdict = {
    "brand":"Ford",
    "model" :"Mustang",
    "year" : 1964,
    "year": 2020
}

#dict len()
print(len(thisdict))

#any data type
thisdict = {
    "brand":"Ford",
    "electric":False,
    "year": 1964,
    "colors":["red","white","blue"]
}

#dict() method
thisdict = dict(name = "John",age =36,county="Norway")
print(thisdict)

#ACCESS DICTIONARY ITEMS
#with keyname inside sqare brackets
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
# get()
x = thisdict.get("model")
#all keys()
x = thisdict.keys()
#any changes done to the dictionary will be reflected in the keys list.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change  dict_keys(['brand', 'model', 'year'])

car["color"] = "white"

print(x) #after the change dict_keys(['brand', 'model', 'year', 'color'])

# values() a list of all th values
x = thisdict.values()

#any changes will be in the values list
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change dict_values(['Ford', 'Mustang', 1964])

car["year"] = 2020

print(x) #after the change dict_values(['Ford', 'Mustang', 2020])

#The items() method will return each item in a dictionary, as tuples in a list.
x = thisdict.items() #dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

#Make a change in the original dictionary,
# and see that the items list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

car["year"] = 2020

print(x) #after the change dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])

#To determine if a specified key is present in a dictionary use the in keyword
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

#CHANGE DICT ITEMS
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

#update()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year":2020})

#ADD DICTONARY ITEMS
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#update()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color":"red"})

#REMOVE DICTIONARY ITEMS
#pop() removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#popitem()  removes last inserted item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#del keyword removes the item with specified key name 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

#also keyword del can delete whole dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict 
print(thisdict)

#clear( ) empties the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#LOOP DICTIONARIES
#return keys
for x in thisdict :
    print(x)

#print all values
for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
    print(x)

# return keys
for x in thisdict.keys():
    print(x)

#loop through keys and values With items()
for x, y in thisdict.items():
    print(x, y)

#copy dictionary
#You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to
# dict1, and changes made in dict1 will automatically also be made in dict2.
#copy()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
# dict() function
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#NESTED DICTIONARIES
#A dictionary can contain dictionaries, this is called nested dictionaries.
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#Access items in nested dictionaries
print(myfamily["child1"]["name"])

#get value by get()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x= car.get("model")
print(x)

#setdefault()
#The setdefault() method returns the value of the item with the specified key.
#If the key does not exist, insert the key, with the specified value, see example below
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "white")

print(x) #white and inserted to dict

#Exercises
#1
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#2
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

#3
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"
#4
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
#5
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
