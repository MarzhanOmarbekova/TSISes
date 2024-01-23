#Example 1
x = 1 #int
y = 2.8 #float
z = 1j #complex
print(type(x))
print(type(y))
print(type(z))


#Example 2
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))

#Example 3
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))

#Example 4 [Float can also be scientific numbers with an "e" to indicate the power of 10]
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))

#Example 5 {Complex numbers are written with a "j" as the imaginary part:}
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))

#Example 6[type conversion]
x = 1
y = 2.8
z = 1j

#convert  from int to float:
a = float (x)
#convert from float to int
b = int(y)
#convert from int to complex
c = complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

#Example 7 [random]
import random
print (random.randrange(1,10))

#Exercise 1
x = 5
x = float(x)

#Exercise 2
x = 5.5
x = int(x)

#Exercise 3
x = 5
x = complex(x)
