m, n = int(input()), int(input())
for i in range(m, n + 1):
    print(i, ':', end=' ', sep='')
    for j in range(2, i):
        if i % j == 0:
            print(j, end=' ')
    print()
