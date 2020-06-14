# done

while True:
    operation = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    if operation == '0': break
    if operation in ('+', '-', '*', '/'):
        x = float(input("x = "))
        y = float(input("y = "))
        if operation == '+':
            print("%.2f" % (x + y))
        elif operation == '-':
            print("%.2f" % (x - y))
        elif operation == '*':
            print("%.2f" % (x * y))
        elif operation == '/':
            if y != 0:
                print("%.2f" % (x / y))
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")
