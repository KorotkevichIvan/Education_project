def spisok():
    return input('Введите числа через пробел: ').split(), int(input('Среднее геометрическое - 1 \nСреднее арифметическое - 2 \n'))

def arif(n):
    total = 0
    for i in range(len(n)):
        total += int(n[i])
    return print(total / len(n))

def geom(n):
    total = 1
    for i in range(len(n)):
        total *= int(n[i])
    return print(total ** (1 / 3))

x, b = spisok()
if b == 1:
    geom(x)
elif b == 2:
    arif(x)
