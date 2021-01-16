print("sintax while")
i = 1
while i < 6:
    print(i)
    i += 1
print("==================")

print("brake statemen")
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
print("==============")

print("continus statemen")
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
print("==============")

print("else statement")
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("isff")
