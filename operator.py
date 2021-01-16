#operator perbandingan
x = 5
y = 3

print (x==y)
print (x!=y)
print (x<y)
print (x>y)
print (x<=y)
print (x>=y)
print('------------')

#operator logis
#and true jika semuanya benar
x = 5
print (x > 3 and x < 10) 
print (x < 3 and x < 10) 
print('------------')

#or true jika salah satu benar
x = 5
print (x > 3 or x < 10) 
print (x < 3 or x > 10) 
print('------------')

#not false jika semua hasil benar
x = 5
print (not(x > 3 and x < 10))
print (not(x < 3 and x > 10))
print('------------')

#operator identitas
#is true jika objek sama
x = 5
y = 5
z = 2

print (x is y )
print (x is z)
print('------------')

#is not true jika obje tidak sama
x = 5
y = 5
z = 2

print (x is not y )
print (x is not z)
print('------------')

#operator keanggotaan
#in true jika objek ada di variabel
x = 5, 6 ,7

print (5 in x)
print (10 in x)
print('------------')

#not in true jika objek tidak ada di variabel
x = 5, 6 ,7

print (5 not in x)
print (10 not in x)
print('------------')





