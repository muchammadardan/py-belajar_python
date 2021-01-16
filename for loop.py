fruit = ["aple", "banana", "cheryy"]
for x in fruit:
    print(x)
print("=======================")

print("the break statemen")
for x in fruit:
    if x == "banana":
        break
    print(x)
print("=======================")

print("The continue statement")
for x in fruit:
    if x == "banana":
        continue
    print(x)
print("=======================")

print("for tough string")
for x in "banana":
    print(x)
print("=======================")

print("range funtion")
for x in range(6):
    print(x)
print("=======================")

for y in range(2,30,3):
   print(y) 
print("=======================")

print("else in loop")
for x in range(6):
    print(x)
else:
    print("finally finish")
print("=======================")


print("nested loop")
a = ["aku", "dia", "kamu"]
b = ["uwu", "jsl", "wef"]

for c in a:
    for d in b:
        print(c, d)
print("=======================")

print("The pass statement")
for x in [0, 1, 2]:
    pass