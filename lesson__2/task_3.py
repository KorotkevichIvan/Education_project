list_1 = [6, 9]
tuple_1 = (1, 3)
dict_1 = dict(zip(list_1, tuple_1))
del dict_1[9]
print(dict_1)
dict_2 = dict(zip(tuple_1, list_1))
del dict_2[1]
print(dict_2)
