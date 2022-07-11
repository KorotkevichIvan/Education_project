import random
n, m = int(input()), int(input())
coun = 0
for i in range(n):
    print()
    for j in range(m):
        a = random.randint(1, 9)
        print(a, end=' ')
        if a == 7:
            coun += 1
print()
print(coun)
