print("Calling funtion") #memanggil funtion
def myfuntion():
    print("my funtion is bla bla")

myfuntion()
print("===================================")

print("Argumen") #function dengan argumen
def myfuntion(fname):
    print(fname + " refsnes")

myfuntion("tobias")
myfuntion("romi")
myfuntion("robby")
print("===================================")

print("Number of argumen") #argumen dengan nomor dan nama
def myfuntion(fname, lname):
    print(fname + " " + lname)

myfuntion("Emil", "Refnes")
myfuntion("Muchammad", "Ardan")
print("===================================")

print("Arbitrary and argumen") #ketika tidak tau jumlah argumennya ke tuple
def my_function(*kids):
    print("the young is " + kids[1])

my_function("Emil", "Tobias", "Linus")
print("===================================")

print("Keyword Argumen") #Anda dapat mengirimkan perintah dengan value
def my_function(child3, child2, child1):
    print("Nama anak kecilnya adalah " + child2)

my_function(child1 = "Emil", child2 = "sastro", child3 = "bambang")
print("===================================")

print("**kwargs")# ke dictionary
def my_function(**kid):
    print("nama anak kecilnya adalah " + kid["fname"])

my_function(fname = "samsul", lname = "sastro")
print("===================================")

print("default parameter") #memanggil tanpa menggunakan parameter
def my_function(country = "norway"):
    print("i'm from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
print("===================================")

print("passing list as a argument")
def my_function(food):
    for x in food:
        print(x)
fruits = ["aplle", "Bannana", "chery"]

my_function(fruits)

print("return values")
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
print("===================================")

print("The pass statement")
def my_function():
    pass