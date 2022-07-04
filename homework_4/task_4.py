num = input('Введите числа через пробел: ').split()
num += num[0]
for i in range(len(num) - 1):
    num[i] = num[i + 1]
del num[-1]
print(num)
