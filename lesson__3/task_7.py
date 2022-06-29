text = input('Введите предложение или строку: ')
if len(text) > 5:
    print(len(text))
elif len(text) < 5:
    print('Need more!')
else:
    print('It is five!')
