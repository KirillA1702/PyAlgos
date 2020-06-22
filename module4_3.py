import cProfile, timeit
from random import randint


# цикл №1, время отработки: 1.8525417
print(timeit.timeit('''
for i in range(1, 100 + 1):
    m = 100 * (100 + 1) // 2
    '''), '- обычный цикл "for".\n')


def num_1(n):
    return example_1(n) == res(n)

def num_2(n):
    return example_2(n) == res(n)

def num_3(n):
    return example_3(n) == res(n)

def res(n):
    return n * (n + 1) // 2

# рекурсия, время отработки: 0.018392899999999823
def example_1(n):
    if n == 1:
        return n
    return n + example_1(n - 1)

# цикл №2, время отработки: 0.008052600000000076
def example_2(n):
    summa = 0
    while n >= 1:
        summa += n
        n -= 1
    return summa

# цикл №3, время отработки: 0.00446309999999972
def example_3(n):
    summa = 0
    for i in range(n+1):
        summa += i
    return summa

print(timeit.timeit('example_1(100)', setup='from __main__ import example_1', number=1000), '- реккурсия.\n')
# 0.018392899999999823
print(timeit.timeit('example_2(100)', setup='from __main__ import example_2', number=1000), '- функция цикл "while".\n')
# 0.008052600000000076
print(timeit.timeit('example_3(100)', setup='from __main__ import example_3', number=1000), '- функция цикл "for".\n')
# 0.00446309999999972


cProfile.run('example_1(10)')
# # 10/1    0.000    0.000    0.000    0.000 module4_3.py:28(example_1)
#
cProfile.run('example_1(100)')
# # 100/1    0.000    0.000    0.000    0.000 module4_3.py:28(example_1)
#
cProfile.run('example_1(500)')
# # 500/1    0.000    0.000    0.000    0.000 module4_3.py:28(example_1)
#
cProfile.run('example_1(900)')  # свыше 993 стеков произошло переполнение
# # 993/1    0.001    0.000    0.001    0.001 module4_3.py:28(example_1)



cProfile.run('example_2(1000)')
# # 1    0.000    0.000    0.000    0.000 module4_3.py:34(example_2)
#
cProfile.run('example_2(100000)')
# # 1    0.012    0.012    0.012    0.012 module4_3.py:34(example_2)
#
cProfile.run('example_2(500000)')
# # 1    0.069    0.069    0.069    0.069 module4_3.py:34(example_2)
#
cProfile.run('example_2(1000000)')
# # 1    0.152    0.152    0.152    0.152 module4_3.py:34(example_2)


cProfile.run('example_3(1000)')
# 1    0.000    0.000    0.000    0.000 module4_3.py:42(example_3)

cProfile.run('example_3(100000)')
# 1    0.007    0.007    0.007    0.007 module4_3.py:42(example_3)

cProfile.run('example_3(500000)')
# 1    0.035    0.035    0.035    0.035 module4_3.py:42(example_3)

cProfile.run('example_3(1000000)')
# 1    0.076    0.076    0.076    0.076 module4_3.py:42(example_3)


# цикл 'for' вне функции: (1.8525417)
# рекурсия: 0.018392899999999823, до 993 вызовов
# функция цикл 'while': 0.008052600000000076
# функция цикл 'for': 0.00446309999999972
#
# Итого: для решения данной задачи при большом натуральном числе
# лучшего всего применять цикл "for" в рамках самописной функции.
#
# Сложность алгоритмов - O(n) – линейная сложность.
