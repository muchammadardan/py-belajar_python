#membuat list
datas = [1, 2, 3]
list_karyawan = ['joni', 'bambang', 'samsul', 'oni', 'lola', 'guntur']
no_kk         = [1, 2, 3, 4, 5, 6]

for data in datas:
    x = list_karyawan[data]
    y = no_kk[data]
    print('{} {}'.format(x, y))




'''
#acces item
print (list_karyawan[2])

#negative index
print (list_karyawan[-1])

#range of index
print (list_karyawan[2:5])

#jarak index ke 4 tidak dimasukan
print (list_karyawan [:4])

#ganti nama karyawan
list_karyawan[2] = 'karno'
print (list_karyawan)

#loop
for x in list_karyawan:
    print (x)

#pakai if
if 'samsul' in list_karyawan:
    print ('yes ada samsul')
else:
    print ('no false')

#list lenght
print (len(list_karyawan))
print ('---------------------------------------')
'''
#Add Item
list_karyawan.insert (1,'tejo')
print(list_karyawan)
#pakkai apend
list_karyawan.append ('poyo')
print(list_karyawan)
print('------------------------')

#remove item
#pakai remove menghapus sesuai nama
list_karyawan.remove ('poyo')
print(list_karyawan)
print('------------------------')

#pakaipop menghapus nama terakhir
list_karyawan.pop()
print(list_karyawan)
print('------------------------')

#pakai del menghapus sesuai index
del list_karyawan[0]
print(list_karyawan)
print('------------------------')

'''#pakai clear menghapus semua
list_karyawan.clear()
print(list_karyawan)'''

#Copy list
mylist = list_karyawan.copy()
print(mylist)
print('------------------------')

#join two list
list3 = no_kk + list_karyawan
print(list3)
print('------------------------')

#join menggunakan append
for x in no_kk:
    list_karyawan.append(x)
    print(no_kk)
print('------------------------')

#join menggunakan extend
list_karyawan.extend(no_kk)
print(list_karyawan)
print('------------------------')

#memakai construct
c = list_karyawan
print(c)