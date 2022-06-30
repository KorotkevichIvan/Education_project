x = 0
total = 0
while x != 'стоп':
    x = input('Введите число или слово стоп: \n')
    if x == 'стоп':
        break
    total += int(x)
    print(total)
