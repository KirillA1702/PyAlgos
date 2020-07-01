# done

import random

m = int(input('Введите длинну массива: '))
arr = [random.randint(0, 49) for i in range(2 * m + 1)]

def mediana(arr, k):

    if len(arr) == 1 and k == 0:
        return arr[0]

    n = random.choice(arr)

    min, max, midd = [], [], []

    for i in arr:
        if i < n:
            min.append(i)
        elif i > n:
            max.append(i)
        else:
            midd.append(i)

    if k < len(min):
        return mediana(min, k)
    elif k < len(min) + len(midd):
        return n
    else:
        return mediana(max, k - len(min) - len(midd))


print(arr)
print(mediana(arr, len(arr) // 2))
print(sorted(arr))
