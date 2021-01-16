# Home dan intro
print("Pengenalan python")
print("Selamat Datang di Web saya")
print("--------------------------------")

# Syntax
if 5 > 2:
    print('lima lebih besar dari 2')
if 1 < 2:
    print('lima lebih kecil dari 2')
print('-------------------------------')

# Variabel
x = 5
y = "hai"
print(x)
print(y)

print('--------------------------------------')

# comment
# tanda ini untik comment
"""
ini juga comment 
untuk menjelaskan lebih banyak kata
seperti ini
"""
print('halooo')
print('------------------------------------------')

# variabel
x = 5
x = 'bambang'
print(x)
print('-------------------------------------------')

x, y, z = 'orange', 'banana', 'cherry'
print(x)
print(y)
print(z)
print('--------------------------------------')

x = y = z = "orange"
print(x)
print(y)
print(z)
print('-------------------------------------------')

x = 'awesome'
print("python is " + x)
print('-------------------------------------------')

x = 'python is'
y = 'awesome'
z = x + ' ' + y
print(z)
print('-------------------------------------------')

x = 5
y = 20
print(x+y)
print('-------------------------------------------')

# Global Variabel
x = 'awesome'


def funtion():
    print('Python is ' + x)


funtion()
print('------------------------------------------------')

x = 'eat'


def salam():
    x = 'Selamat Pagi'
    print('beri salam' + x)


salam()
print(x)
print('------------------------------------------------')

# Global Keyword


def myfunt():
    global x
    x = 'fantastis'


myfunt()

print('aku suka = ' + x)
print('------------------------------')
x = "awesome"


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)
