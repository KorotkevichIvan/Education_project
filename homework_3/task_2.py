n = int(input('Введите колличество гостей: \n'))
if n > 50:
    print('ресторан')
elif 20 <= n <= 50:
    print('кафе')
else:
    print('дом')
