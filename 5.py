x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(x, y, z)
print(type(x))
print(type(y))
print(type(z))

x = 1
y = 35656222554887711
z = -3255522
print(x, y, z)
print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100
print(x, y, z)
print(type(x))
print(type(y))
print(type(z))

x = 3+5j
y = 5j
z = -5j
print(x, y, z)
print(type(x))
print(type(y))
print(type(z))

x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(x, y, z)

#convert from int to float:
print("From x to float")
a = float(x)
#convert from float to int:
print("From y to int")
b = int(y)
#convert from int to complex:
print("From x to complex")
c = complex(x)

print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

#RANDOM
import random
print("Random number:", end = "")
print(random.randrange(1, 10))
