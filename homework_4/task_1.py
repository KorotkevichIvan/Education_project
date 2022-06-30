num_1 = input('Введите числа через пробел: ').split()
num_2 = []
for i in range(len(num_1)):
    num_2.append(int(num_1[i]) * -2)
print(*num_1, '\n', *num_2)

a = 0
while a != len(num_1):
    print(int(num_1[a]) * -2, end=' ')
    a += 1
