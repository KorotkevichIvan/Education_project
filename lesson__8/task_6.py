def kvad_urav(a, b, c):
    d = b ** 2 - 4 * a * c
    if d == 0:
        print('Корень уравнения: ', -b / (2 * a))
    elif d < 0:
        print('Нет корней')
    else:
        print('Корни уравнения: ', (-b + d ** 0.5) / 2 * a, (-b - d ** 0.5) / 2 * a)

x, y, z = int(input('Введите три числа через enter: ')), int(input()), int(input())
if x == 0:
    x = 1
elif y == 0:
    y = 1
elif z == 0:
    z = 1
print(x, 'x²', '+', y, 'x', '+', z, '=', '0', sep='')
kvad_urav(x, y, z)
