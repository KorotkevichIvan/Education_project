num = input('Введите числа через пробел: ').split()

def summ(listt):
    total = 0
    for i in range(len(listt)):
       total += (int(i) * int(listt[i]))
    return total

print(summ(num))
