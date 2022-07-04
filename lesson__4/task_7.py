a, b = int(input('Введите два любых числа в порядке возрастания: \n')), int(input())
for i in range(a, b + 1):
    print(i)
print('Общее число цифр:', b - a + 1)
