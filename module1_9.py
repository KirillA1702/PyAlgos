# done
a, b, c = int(
    input('Ввдедите число a: ')), int(
        input('Ввдедите число b: ')), int(
            input('Ввдедите число c: '))

if b < a < c or c < a < b:
    print(a)
elif a < b < c or c < b < a:
    print(b)
else:
    print(c)
