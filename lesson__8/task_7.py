def step(k,n):
    for i in k:
        for j in range(2, 100):
            if n ** j == i:
                print(i, n, 'True')

x = [36, 100, 1024, 625, 64, 16, 128, 81, 2187, 4096]
y = int(input('Введите число: '))
step(x, y)
