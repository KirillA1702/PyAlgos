# done

from random import randint
import timeit
import memory_profiler
import time


def bubble_sort(numbers):
    change = True
    while change:
        change = False  # <---- здесь такого нет
        for i in range(len(numbers) - 1):
            if numbers[i] < numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                change = True
        if change == False:
            return numbers


numbers = [randint(-100, 99) for i in range(1000)]

print(f'Исходный массив: {numbers}')
print(f'Отсортированный массив: {numbers}')


if __name__ == '__main__':

    t1 = time.process_time()
    m1 = memory_profiler.memory_usage()

    cubes = bubble_sort(numbers)

    t2 = time.process_time()
    m2 = memory_profiler.memory_usage()

    time_diff = t2 - t1
    mem_diff = m2[0] - m1[0]
    print(f"Выполнение заняло {time_diff} сек and {mem_diff} Мб")

numbers = [randint(-100, 100) for i in range(10)]
# время выполнения для 10 - 0.0014834000000000236
print(timeit.timeit("bubble_sort(numbers)",
                    setup="from __main__ import bubble_sort, numbers", number=1000))

numbers = [randint(-100, 100) for i in range(100)]
# время выполнения для 100 - 0.01358769999999998
print(timeit.timeit("bubble_sort(numbers)",
                    setup="from __main__ import bubble_sort, numbers", number=1000))

numbers = [randint(-100, 100) for i in range(1000)]
# время выполнения для 1000 - 0.340421
print(timeit.timeit("bubble_sort(numbers)",
                    setup="from __main__ import bubble_sort, numbers", number=1000))

# не пойму почему разница во времени на 1000 почти в два раза?



def bubble_sort(orig_list):
    n = 1
    while n < len(orig_list):  # <---- слишком много вычислений что привоит к торможению!
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
        n += 1
    return orig_list


orig_list = [randint(-100, 100) for _ in range(10)]
print(orig_list)
bubble_sort(orig_list)
print(orig_list)
# время выполнения для 10 - 0.0089592
print(timeit.timeit("bubble_sort(orig_list)",
                    setup="from __main__ import bubble_sort, orig_list", number=1000))

orig_list = [randint(-100, 100) for _ in range(100)]
# время выполнения для 100 - 0.6965269000000001
print(timeit.timeit("bubble_sort(orig_list)",
                    setup="from __main__ import bubble_sort, orig_list", number=1000))

orig_list = [randint(-100, 100) for _ in range(1000)]
# время выполнения для 1000 - 76.1221738
print(timeit.timeit("bubble_sort(orig_list)",
                    setup="from __main__ import bubble_sort, orig_list", number=1000))

# итого из-за того что во второй реализации слишком много вычислений в цикле
# while, выполнение кода замедляется в 210 раз на массиве равному 1000!!
#
# Моя реализация:
# 10 - 0.0017923999999999163
# 100 - 0.016836300000000026
# 1000 - 0.34997619999999996
#
# Ваша реализация:
# 10 - 0.014191100000000012
# 100 - 0.7527278
# 1000 - 75.04646740000001



#
#
#