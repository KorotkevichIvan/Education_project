list_1 = [1, 2, 3]
list_2 = [7, 8, 9]
list_1.append(4)
list_1.insert(0, 0)
list_2.append(10)
list_2.insert(0, 6)
print(list_1)
print(list_2)
list_1.extend(list_2)
print(list_1)
