from functools import reduce
def spisok(n):
    a = []
    for i in n:
        if int(i) % 3 == 0:
            a.append(int(i))
    return a

numbers =  input('Введите числа через пробел: ').split()

print(reduce(lambda x, y: x * y, spisok(numbers), 1))
