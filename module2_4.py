# done

enum = int(input('Введите количество элементов: '))
n = 1
summ = 0
for i in range(enum):
    summ += n
    n /= -2
print(f'Количество элементов - {enum}, их сумма - {summ}')