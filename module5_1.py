# done

from collections import defaultdict
from collections import Counter

amount = int(input('Введите количество предприятий для расчета прибыли: '))

firms = defaultdict(Counter)
average = 0
for i in range(amount):
    name = input('Введите название предприятия: ')
    quart_1 = int(input('Прибыль за 1-й квартал: '))
    quart_2 = int(input('Прибыль за 2-й квартал: '))
    quart_3 = int(input('Прибыль за 3-й квартал: '))
    quart_4 = int(input('Прибыль за 4-й квартал: '))
    firms[name] = Counter({
        'quart_1': quart_1,
        'quart_2': quart_2,
        'quart_3': quart_3,
        'quart_4': quart_4
    })
    average += sum(firms[name].values())

average = average / amount

print('Средняя годовая прибыль всех предприятий:', average)

print('\nПредприятия, с прибылью выше среднего значения: ')

for key in firms:
    if sum(firms[key].values()) > average:
        print(key)

print('\nПредприятия, с прибылью ниже среднего значения: ')

for key in firms:
    if sum(firms[key].values()) < average:
        print(key)
