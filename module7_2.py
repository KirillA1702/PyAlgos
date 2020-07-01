# done

import random
import timeit


def sorting(arr):
    if len(arr) == 1:
        return
    midd = len(arr) // 2
    l_arr = arr[:midd]
    r_arr = arr[midd:]

    sorting(l_arr)
    sorting(r_arr)

    left_i, right_i, midd_i = 0, 0, 0
    while left_i < len(l_arr) and right_i < len(r_arr):
        if l_arr[left_i] < r_arr[right_i]:
            arr[midd_i] = l_arr[left_i]
            left_i += 1
        else:
            arr[midd_i] = r_arr[right_i]
            right_i += 1
        midd_i += 1

    for i in range(left_i, len(l_arr)):
        arr[midd_i] = l_arr[i]
        midd_i += 1

    for i in range(right_i, len(r_arr)):
        arr[midd_i] = r_arr[i]
        midd_i += 1

    return arr


arr = [50 * random.random() for i in range(int(input('Введите число элементов: ')))]

print(f'Исходный - {arr}')
print(f'Отсортированный - {sorting(arr)}')

print(timeit.timeit("sorting(arr)",
                    setup="from __main__ import sorting, arr", number=1000))

# вроде тут не нужно никакой аналитики.

