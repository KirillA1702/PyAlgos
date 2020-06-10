# done
a = int(input())
b = int(input())
c = int(input())

if a != 0 and b != 0 and c != 0:
    if a == b == c:
        print('Равнобедренный треугольник.')
    elif a == b or b == c or c == a:
        print('Равносторонний треугольник.')
    else:
        print('Разносторонний треугольник.')
else:
    print('Такой треугольник существовать не может!')
