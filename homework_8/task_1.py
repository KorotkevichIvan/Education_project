def fac2(n):
    for i in n:
        if int(i) % 2 == 0:
            x = int(i)
            i = 1
            for j in range(2, x + 1, 2):
                i *= j
        if int(i) % 2 != 0:
            w = int(i)
            i = 1
            for k in range(1, w + 1, 2):
                i *= k
        print(i)

cifry = input('Введите 5 положительных чисел через пробел: ').split()

fac2(cifry)
