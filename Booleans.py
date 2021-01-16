a = 200
b = 33

if b > a:
    print ('b grater than a')
else:
    print ('b not greater than a')
print('--------------------------------------')

#Evaluasi string dan int
print (bool('isi'))
print (bool(''))
print (bool(3))
print ('--------------------------------------')

#evaluasi nilai false
print (bool(False))
print (bool(None))
print ('--------------------------------------')

class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print (bool(myobj))
print ('--------------------------------------')

#mengambalikan fungsi
def myfuntion():
    return True

if myfuntion():
    print ("yes")
else:
    print ('no')
print ('--------------------------------------')

#periksa objek

a = "200"
print(isinstance(a, int))