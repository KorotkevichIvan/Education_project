num = input('Введите числа через пробел: ').split()

def summ(listt):
    total = 0
    x = 0
    for i in range(len(listt)):
        if int(listt[i]) > x:
            x = int(listt[i])
        total += int(listt[i])
    return total, x

summa, maxx = summ(num)
print(summa,maxx)
