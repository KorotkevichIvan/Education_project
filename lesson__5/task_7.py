from random import randint
a, b = int(input()), int(input())
k = int(input())
x = randint(a, b)
f = 0
while True:
    n = int(input())
    if n == x:
        print('You are the winner')
        break
    elif n > x:
        print('Попробуй число поменьше')
    elif n < x:
        print('Попробуй число побольше')
    f += 1
    if f == k:
        print('У Вас закончились попытки')
        break
