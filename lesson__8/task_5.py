def x(s):
    total = 0
    for i in s:
        total += (int(i) ** 0.5 + int(i)) / 2
    return total

s = ['5', '12', '19']

print(x(s))
