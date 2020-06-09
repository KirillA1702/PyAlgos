# done
num = int(input('Введите трехзначное целое число: '))
result_sum = (num // 100) + ((num // 10) % 10) + (num % 10)
result_mul = (num // 100) * ((num // 10) % 10) * (num % 10)
print(f'Сумма чисел = {result_sum} \nПроизведение = {result_mul}')