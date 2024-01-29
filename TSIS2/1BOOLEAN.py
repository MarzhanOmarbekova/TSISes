#Example 1 [comparing to values py give us boolean answer]
print(10 > 9 )
print(10 == 9)
print (10 < 9)
#Example 2[in if statement ]
a = 200
b = 33
if b > a :
    print("b id greater than a")
else:
    print("b is not greater than a")

#Example 3 [bool() function evaluate any value]
print(bool("Hello"))
print(bool(15))

#Example 4 [evaluate two values]
x = "Hello"
y = 15
print(bool(x))
print(bool(y))

#Example 5 [most  values are true]
bool("abc")
bool(123)
bool(["apple","cherry","banana"])

#Example 6 [some values are false ]
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#Example 7 [One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:]
class myclass():
    def ___len___(self):
        return 0
myobj = myclass()
print(bool(myobj))

#Example 8 [Functions can Return a Boolean]
def myFunction():
    return True
print(myFunction())

#Example 9 
def myFunction():
    return True
if myFunction():
    print("YES!")
else :
    print("NO!")
 
#example 10 [isinstance() function to determine if an object is of a certain data type]
x = 200
print(isinstance(x,int))

#Exercise 1
print(10 > 9) #True
    
#Exerecise 2
print(10 == 9) #False

#Exerecise 3
print(10 < 9) #False

#Exerecise 4
print(bool("abc")) #True

#Exercise 5
print(bool(0)) #False