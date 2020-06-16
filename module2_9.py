# done

print('Для завершения ввода, нажмите "0".')
n = int(input('Введите число: '))
max_sum = 0
max_num = 0
while n != 0:
    m = n
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    if s > max_sum:
        max_sum = s
        max_num = m
    n = int(input('Введите очередное число: '))
print(f'Наибольшее число по сумме цифр: {max_num}, сумма его цифр: {max_sum}')
