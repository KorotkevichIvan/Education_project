num = input('Введите числа через пробел: ').split()
total = 0
for i in range(len(num)):
    if int(num[i]) > 10:
        total += int(num[i])
print(total)
