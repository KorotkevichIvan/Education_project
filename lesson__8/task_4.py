def counter(n):
    for i in s:
        d[i] = d.get(i, 0) + 1
    for i in d:
        print(i, '-', d[i], 'раз/а')

s = input('Введите цифры: ')
d = {}
print(counter(s))
# не понял откуда в ответе появляется none
