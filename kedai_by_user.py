#yg ditampilkan
print("Input Pesanan \n 0. Kopi \n 1.Teh \n 2.Susu" )
user = int(input("Silahkan masukan nomer pesanan Anda : " ))

#input data
orders = []
orders.append(user)
num = [0, 1, 2]
minuman = ["Kopi", "teh", "Susu"]
harga = [3000, 2500, 5000]

for order in orders:
    mnm = minuman[order]
    no = num[order]
    hrg = harga[order]
    print("Anda pesan {} dengan harga {}".format(mnm, hrg ))


#output yg ditampilkan
#print("Pesanan Anda Nomer : {}" + user)
#print('{}'.format(mnm))