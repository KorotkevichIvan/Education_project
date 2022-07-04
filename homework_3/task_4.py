n = input('Введите строку текста: \n')
cen = ((len(n)) - 1) / 2
print(n[int(cen)])
if n[0] == n[int(cen)]:
    print(n[1:int(cen)])
