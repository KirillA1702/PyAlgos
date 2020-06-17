# done

array = [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]

for i in range(len(array)):
    if array[0] > array[1]:
        min_numb_1 = 0
        min_numb_2 = 1
    else:
        min_numb_1 = 1
        min_numb_2 = 0
print('Исходный массив: ', array)

for i in range(2, len(array)):
    if array[i] < array[min_numb_1]:
        b = min_numb_1
        min_numb_1 = i
        if array[b] < array[min_numb_2]:
            min_numb_2 = b
    elif array[i] < array[min_numb_2]:
        min_numb_2 = i

print('Наименьший элемент:', array[min_numb_1])
print('Второй наименьший элемент:', array[min_numb_2])
