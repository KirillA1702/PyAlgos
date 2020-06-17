# done

from random import random

array = [0] * 10
even = []
for i in range(len(array)):
    array[i] = int(random() * 10) + 10
    if array[i] % 2 == 0:
        even.append(i)

print(f'Исходный массив: {array}, результат: {even}')
