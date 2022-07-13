def palindrom(n):
    for i in n:
        if i == i[::-1]:
            print(i, i[::-1], "- палиндром")
        else:
            print(i, i[::-1], '-', 'не палиндром')

spisok = input('Введите слова через пробел: ').split()

palindrom(spisok)
