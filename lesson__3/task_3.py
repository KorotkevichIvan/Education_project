text = input('Введите предложение из двух слов: '). split()
text.append('!')
text.append('!')
text[0], text[2] = text[2], text [0]
print(*text)
