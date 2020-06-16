# done

array = [0] * 8
for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            array[j - 2] += 1
i = 0
while i < len(array):
    print('В диапазоне 2-99:', array[i], 'чисел кратны', i + 2)
    i += 1
