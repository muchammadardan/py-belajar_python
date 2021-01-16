#penulisan dictionary berdasarkan key dan values
data_dic = { 
    "brand" : "ford",
    "model" : "mustang",
    "year"  : 1994
}
print(data_dic)
print('---------------------------')

#Acessing item menggunakan key name
print(data_dic["model"])
print(data_dic["year"])
print('---------------------------')

#get menggunakan method ini hasilnya sama
print(data_dic.get("model"))
print('---------------------------')

#change values
data_dic ["year"] = 2018
print(data_dic)
print('---------------------------')


#loop dictionary
for x in data_dic:
    #print(x) #hanya key name
    print(data_dic[x]) #hanya values name

print('---------------------------')
#menggunakan values untuk menampilkan value
for y in data_dic.values():
    print(y)
print('---------------------------')

#menggunakan ittemm untuk menampilkan key name dan values
for a, b in data_dic.items():
    print(a, b)
print('---------------------------')

#cek if 
if "model" in data_dic:
    print("yes ada")
print('---------------------------')

#Menambahkan item
data_dic ["color"] = "red"
print(data_dic)
print('---------------------------')


