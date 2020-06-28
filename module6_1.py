# done

from sys import getsizeof, version_info
from random import randint
from memory_profiler import profile
import platform
from distutils import util


def calc_size(x):
    res_size = getsizeof(x)
    print(f'size = {getsizeof(x)}, object = {x}')

    if hasattr(x, 'NaN'):
        if hasattr(x, 'NaN'):
            for k, v in x:
                res_size += calc_size(k)
                res_size += calc_size(v)
        elif not isinstance(x, str):
            for xx in x:
                res_size += calc_size(xx)

    return res_size

@profile
def module_3():

    array = [randint(-50, 50) for i in range(50)]

    max_i = 0
    min_i = 0
    max_numb = array[0]
    min_numb = array[0]

    for i, numb in enumerate(array):
        if max_numb < numb:
            max_numb = numb
            max_i = i

        if min_numb > numb:
            min_numb = numb
            min_i = i

    array[max_i] = min_numb
    array[min_i] = max_numb

    return locals()

res_module_3 = module_3()

print(f'Вариант решения {module_3.__name__}:')

size_of_all_var_3 = 0

for i in res_module_3.keys():
    size_of_all_var_3 += calc_size(res_module_3[i])

print(f'\nСписок переменных: {res_module_3}')
print(f'Общий размер переменных: {size_of_all_var_3} байт\n')

@profile
def module_3_2():

    array = [randint(-50, 50) for i in range(50)]

    max_numb = max(array)
    min_numb = min(array)
    max_i = array.index(max_numb)
    min_i = array.index(min_numb)

    array[max_i], array[min_i] = min_numb, max_numb

    return locals()

res_module_3_2 = module_3_2()

print(f'Вариант решения {module_3_2.__name__}:')

size_of_all_var_3_2 = 0

for i in res_module_3_2.keys():
    size_of_all_var_3_2 += calc_size(res_module_3_2[i])

print(f'\nСписок переменных: {res_module_3_2}')
print(f'Общий размер переменных: {size_of_all_var_3_2} байт\n')

@profile
def module_3_3():

    array = [randint(-50, 50) for i in range(50)]

    if array.index(max(array)) > array.index(min(array)):
        array[array.index(max(array))], array[array.index(min(array))] = min(array), max(array)
    else:
        array[array.index(min(array))], array[array.index(max(array))] = max(array), min(array)

    return locals()

res_module_3_3 = module_3_3()

size_of_all_var_3_3 = 0

print(f'Вариант решения {module_3_3.__name__}:')

for i in res_module_3_3.keys():
    size_of_all_var_3_3 += calc_size(res_module_3_3[i])

print(f'\nСписок переменных: {res_module_3_3}')
print(f'Общий размер переменных: {size_of_all_var_3_3} байт')

print('*' * 100)
print(platform)
print(version_info)
print(platform.python_version())
print(platform)
print(util.get_platform())
print(platform.architecture())


# Оптимизируем задачу №3 3-го урока.
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
#
# По итогам анализа лучшим вариантом оказался третий вариант решения задачи.
# В данном варианте все нужные значения вычисляются без использования дополнительных
# переменных, при этом память используется только на хранение массива и объекта random,
# в противоположность первым двум вариантам где на переменные выделяется
# отдельная память для хранения.
#
# module_3 - Общий размер переменных: 344 байт
# module_3_2 - Общий размер переменных: 316 байт
# module_3_3 - Общий размер переменных: 260 байт
