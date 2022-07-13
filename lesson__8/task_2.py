spisok = [
    {
        'MC546': 1994
    },
    {
        'TK981': 1997
    },
    {
        'AO322': 2001
    }]
spisok_new = []
for i in spisok:
    for values in i.values():
        if values >= 2000:
            spisok_new.append(i)
print(spisok_new)
