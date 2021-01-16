#String are array
a = 'akuRDA'
print (a[1])
print ('--------------------------')

#Slicing / irisan
a = 'hurawqefd'
print (a[2:5])
print('----------------------------')

#Leght String
a = 'bakul sayur'
print (len(a))
print ('---------------------------')

#String Metods
#Strip
a = ' rujwq'
print (a.strip())
print ('---------------------------')

#Lower
a = 'Hello World!'
print (a.lower())
print ('---------------------------')

#Upper
a = 'Hello World!'
print (a.upper())
print ('---------------------------')

#Replace
a = 'Hello World!'
print (a.replace('H', 'J'))
print ('---------------------------')

#Split
a = 'Hello World!'
print (a.split(','))
print ('---------------------------')

#Check String
txt = 'the rain expextly'
x = 'ain' in txt
print (x)
print ('---------------------------')
txt = 'the rain expextly'
x = 'ain' not in txt
print (x)
print ('---------------------------')

#String Concenation
a = "Hello"
b = 'World'
c = a + b
print (c)
print ('---------------------------')

#string Format
age = 36
tct = 'my name is ardan {}'
print (tct.format(age))
print ('---------------------------')

#Escape Character
txt = 'hallo my name is \'ardan\' yoiii'
print (txt)