a, b = 0, 0

while True:
    try:
        choose = int(input("""Please, select any option below:

1 - Addition;
2 - Subtraction;
3 - Multiplication;
4 - Division;
5 - Exit.

> """))
        if choose == 5:
            break

        a = float(input("A value: "))
        b = float(input("B value: "))

    except ValueError:
        print("Incorrect value! Please, try again.")

    else:
        match choose:
            case 1:
                print(f"{a} + {b} = {a+b}")
            case 2:
                print(f"{a} - {b} = {a-b}")
            case 3:
                print(f"{a} * {b} = {a*b}")
            case 4:
                try:
                    print(f"{a} / {b} = {a/b}")
                except ZeroDivisionError:
                    print("You cannot divide {a} by zero")
                else:
                    pass
