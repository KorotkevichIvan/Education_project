import random
n = int(input())
s = 0
for i in range(1, n + 1):
    print()
    for j in range(1, n + 1):
        a = random.randint(1, 9)
        print(a, end=' ')
        if a % 3 == 0:
            s += a
print()
print(s)
