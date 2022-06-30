x = 0
total = 0
while x != 'стоп':
    x = input('Введите число или слово стоп: \n')
    if x == 'стоп':
        break
    if int(x) == 5:
        print(total)
        continue
    total += int(x)
    print(total)
