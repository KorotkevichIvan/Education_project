while True:
    x, y = int(input()), int(input())
    z = input()
    if z in ['+', '-', '/', '*', '0']:
        if z == '+':
            print(x + y)
        elif z == '_':
            print(x - y)
        elif z == '*':
            print(x * y)
        elif z == '/':
            if y == 0:
                print('На ноль делить нельзя, попробуйте еще раз')
            else:
                print(a / b)
        elif z == '0':
            print('На этом все')
    else:
        print('Попробуйте еще раз')
