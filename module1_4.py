# done
from random import random

from_num = int(input('Введите нижнюю границу: '))
to_num = int(input('Введите верхнюю границу: '))
print(int(random() * (to_num - from_num + 1)) + from_num)

from_num = float(input('Введите нижнюю границу: '))
to_num = float(input('Введите верхнюю границу: '))
print(round(random() * (to_num - from_num + 1) + from_num, 2))

from_letter = input('Введите первую букву: ')
to_letter = input('Введите вторую букву: ')
print(chr(int(random() * (ord(to_letter) - ord(from_letter) + 1)) + ord(from_letter)))
