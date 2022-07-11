n = int(input('Введите любое число: '))

def fact(num):
    total = 1
    for i in range(2, num + 1):
        total *= i
    return total

print(fact(n))
