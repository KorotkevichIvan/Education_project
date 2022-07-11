name = input('Введите 5 имен через пробел: ').split()

def hello(n):
    return print('Hello, ', n, '!!!', sep='')

for i in range(5):
    hello(name[i])
