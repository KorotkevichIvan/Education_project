a, b = [1, 2, 3, 4], []
print(id(a), id(b), sep='\n')
b = a
print(id(a), id(b), sep='\n')
b.append(9)
print(a, b, sep='\n')
