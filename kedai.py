#input data
orders  = [1, 2]
minuman = ['susu', 'coklat', 'kopi', 'teh']
harga   = [5000, 4000, 3000, 1000]
tot_yar = 0
#diberi proses karena ada yanng pesan
#menggunakan looping dikarenakan mengulang data
for order in orders:
    mnm = minuman[order]
    hrg = harga[order]
    tot_yar += hrg
    print('{} {}'.format(mnm, hrg)) #mengubah format menjadi str

#tidak ikut for karena berdiri sendiri
print(tot_yar)
print(minuman)