a = [1, 1]
b = a
for i in range(13):
    a.append(a[i] + a[i + 1])
print(a)

while len(b) != 15:
    b.append(b[-1] + b[-2])
print(b)
