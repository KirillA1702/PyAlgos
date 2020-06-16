# done

from random import random

array = []
for i in range(int(input('Введите длину списка: '))):
    array.append(int(random() * 100) - 50)
print('Базовый список:', array)

x = 0
index = -1
while x < len(array):
    if array[x] < 0 and index == -1:
        index = x
    elif array[x] < 0 and array[x] > array[index]:
        index = x
    x += 1

print(
    f'Максимальный отрицательный элемент в данном массиве = {array[index]}, его индекс {index + 1}')
