# done
numb = int(input("Введите число: "))
even = 0
odd = 0

while numb > 0:
    if numb % 2 == 0:
        even += 1
    else:
        odd += 1
    numb = numb // 10
print(f"Четных чисел - {even} \nНечетных чисел - {odd}")
