from random import randint
a = []
for i in range(19):
    a.append(randint(1, 99))
print(a)
x = max(a)
print(x)
for j in range(19):
    if a[j] % 2  == 0:
        a[j] = x
print(a)
