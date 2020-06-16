# done

x = 5
y = 4
array = []

for i in range(y):
    matrix_lines = []
    summa = 0
    print(f'Введите значение {i+1}-й строки:')
    for j in range(x - 1):
        numb = int(input('> '))
        summa += numb
        matrix_lines.append(numb)
    matrix_lines.append(summa)
    array.append(matrix_lines)

print('=====Матрица=====')

for i in array:
    print(i)
