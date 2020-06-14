# done

def rec(num):
    if len(num) == 0:
        return num
    else:
        return rec(num[1:]) + num[0]
a = str(input('Введите последовательность чисел: '))
print(rec(a))
