#int
x = 1
y = -213
print (type(x))
print (type(y))
print ('-------------------------------------------------------')
#float
x = 1.1
y = -213.21
print (type(x))
print (type(y))
print ('-------------------------------------------------------')
x = 12e33
y = 12.e33
z = 12E21
print (type(x))
print (type(y))
print (type(z))
print('---------------------------------------------------------')

#Complex
x = 12+21j
y = 12213j
z = -412j
print (type(x))
print (type(y))
print (type(z))
print ('--------------------------------------------------------')

#Data Convert
x = 21
y = 12.2
z = 12213j

#convert int to float
a = float (x)
print (a)
print (type(a))

#Convert float to complex
b = complex (y)
print (b)
print (type(b))

#Convert Float to int
c = int (y)
print (y)
print (type(c))
print  ('-----------------------------------------------------')

#Random number
import random
print (random.randrange(1,100))
print ('-------------------------------------------------------')

#Latihan
x = 5
x = float (5)
print (type (x))