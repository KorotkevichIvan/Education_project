lastnames = input('Введите фамилии через пробел: ').split()
ans = []
for i in lastnames:
    if i[0] == 'П' and i[-1] == 'а':
        ans.append(i)
print(*ans)
