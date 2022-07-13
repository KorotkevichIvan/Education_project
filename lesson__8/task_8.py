def sums(n):
    sum_plus = 0
    sum_minus = 0
    for i in n:
        if int(i) > 0:
            sum_plus += int(i)
        elif int(i) < 0:
            sum_minus += int(i)
    print(sum_plus, sum_minus)

x = input('Введите 10 целых чисел(положительных и отрицательных): ').split()

sums(x)
