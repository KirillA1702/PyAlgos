# done

numb = int(input('Сколько будет чисел? '))
cnt_numb = int(input('Какую цифру считать? '))
count = 0
for i in range(1, numb + 1):
    n = int(input('Число ' + str(i) + ': '))
    while n > 0:
        if n % 10 == cnt_numb:
            count += 1
        n = n // 10

print(f'Было введено {count} цифр "{cnt_numb}"')
