rub = int(input('Введите количество рублей: '))
coins = int(input('Ведите количество копеек: '))
if coins >= 100:
    rub += coins // 100
    coins %= 100
    if rub % 10 == 1:
        rub_text = 'рубль'
    elif 2 <= rub % 10 <= 4:
        rub_text = 'рубля'
    elif 5 <= rub % 10 <= 9 or rub % 10 == 0:
        rub_text = 'рублей'
    if coins % 10 == 1:
        coins_text = 'копейка'
    elif 2 <= coins % 10 <= 4:
        coins_text = 'копейки'
    elif 5 <= coins % 10 <= 9 or coins % 10 == 0:
        coins_text = 'копеек'
    print(str(rub), rub_text, str(coins), coins_text)
elif coins < 100:
    if rub % 10 == 1:
        rub_text = 'рубль'
    elif 2 <= rub % 10 <= 4:
        rub_text = 'рубля'
    elif 5 <= rub % 10 <= 9 or rub % 10 == 0:
        rub_text = 'рублей'
    if coins % 10 == 1:
        coins_text = 'копейка'
    elif 2 <= coins % 10 <= 4:
        coins_text = 'копейки'
    elif 5 <= coins % 10 <= 9 or coins % 10 == 0:
        coins_text = 'копеек'
    print(str(rub), rub_text, str(coins), coins_text)
