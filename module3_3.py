# done

array = [88, 26, 41, 75, 23, 52, -49, 60, 69, -18]
min_numb = 0
max_numb = 0

for i in range(len(array)):
    if array[i] < array[min_numb]:
        min_numb = i
    elif array[i] > array[max_numb]:
        max_numb = i

other_array = array[min_numb]
array[min_numb] = array[max_numb]
array[max_numb] = other_array

for i in range(10):
    print(array[i], end=' ')
