text = input('Введите предложение: ')
if len(text) % 3 == 0:     # если учитывать пробелы
    text = text + '!'
print(text)
