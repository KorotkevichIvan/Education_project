num = input('Введите числа через пробел: ').split()
counter = 0
for i in num:
    if int(i) % 2 == 0:
        counter += 1
print(counter)

a = 0
coun = 0
while a != len(num):
    if int(a) % 2 == 0:
        coun += 1
    a += 1
print(coun)
