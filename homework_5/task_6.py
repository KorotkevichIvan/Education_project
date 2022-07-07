from random import randint
a = []
coun = 0
for i in range(10):
    a.append(randint(1, 99))
print(a)
for j in range(1, 10):
    if a[j] > a[j - 1]:
        if a[j] >= a[j - 1]:
            coun += 1
        else:
            continue
    else:
        continue
print(coun - 1)
