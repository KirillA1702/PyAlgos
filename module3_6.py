# done

array = [6, 58, 50, 77, 49, 88, 42, 67, 14, 79]
print('Массив: ', array)
min_index = 0
max_index = 0
for i in range(1, len(array)):
    if array[i] < array[min_index]:
        min_index = i
    elif array[i] > array[max_index]:
        max_index = i

if min_index < max_index or min_index > max_index:
    min_index, max_index = max_index, min_index

summa = 0
for i in range(min_index + 1, max_index):
    summa += array[i]

print(
    f'Сумма элементов между минимальным ({array[max_index]}) и максимальным ({array[min_index]}) элементами: {summa}')
