print('ax²+bx+c=0')
a, b, c = int(input('Введите числа: a, b, c \n')), int(input()), int(input())
d = b ** 2 + 4 * a * c
if d > 0:
    print((-b - d ** 0.5) / 2 * a)
    print((-b + d ** 0.5) / 2 * a)
elif d == 0:
    print(-b / 2 * a)
else:
    print('Нет корней')
