# done

from random import random

column = 4
lines = 3
array = []
for i in range(lines):
    line = []
    for j in range(column):
        n = int(random() * 50)
        line.append(n)
        print(f'%4d' % n, end='')
    array.append(line)
    print()

max_numb = -1
min_array = []
for j in range(column):
    min_numb = 50
    for i in range(lines):
        if array[i][j] < min_numb:
            min_numb = array[i][j]
    min_array.append(min_numb)
    if min_numb > max_numb:
        max_numb = min_numb

print('Минимальные значения по столбцам:', min_array)
print('Максимальный среди минимальных:', max_numb)