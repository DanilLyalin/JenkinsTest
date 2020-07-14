
while True:
    op = input("Введите знак операции (+,-,*,/) или exit для выхода: ")
    if op == 'exit':
        break
    if op in ('+', '-', '*', '/'):
        x = float(input("Введите x: "))
        y = float(input("Введите y: "))
        if op == '+':
            print("Ответ: %.2f" % (x+y))
        elif op == '-':
            print("Ответ: %.2f" % (x-y))
        elif op == '*':
            print("Ответ: %.2f" % (x*y))
        elif op == '/':
            print("Ответ: %.2f" % (x/y))
    else:
        print("Неверный параметр!")