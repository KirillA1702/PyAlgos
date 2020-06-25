# done

from collections import deque

def add_multi():
    num_1 = deque(input('Введите первое число: '))
    num_2 = deque(input('Введите второе число: '))
    num_1.extendleft('x0'), num_2.extendleft('x0')
    num_1, num_2 = int(''.join(num_1), 16), int(''.join(num_2), 16)
    add_int, multi_int = num_1 + num_2, num_1 * num_2
    add_hex, multi_hex = 'x%X' % int(add_int), 'x%X' % int(multi_int)
    add_hex, multi_hex = deque(add_hex), deque(multi_hex)
    add_hex.popleft(), multi_hex.popleft()
    return f'Сумма чисел из примера: {add_hex} \nПроизведение: {multi_hex}'

result = add_multi()
print(result)
