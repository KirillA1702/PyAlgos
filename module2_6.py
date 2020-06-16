# done

from random import random

n = round(random() * 100)
print('Отгадайте число за 10 попыток!')
def rec(u, i):
    if i == 10:
        print('Вы исчерпали 10 попыток. Было загадано число', n)
        return
    if u > n:
        print('Много')
        i += 1
        rec(int(input(str(i))), i)
    elif u < n:
        print('Мало')
        i += 1
        rec(int(input(str(i))), i)
    else:
        print('Вы угадали!')
        return

rec(int(input('Введите число: ')), 1)
