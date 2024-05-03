def __main__():
    a = int(input("Enter number1: "))
    b = int(input("Enter number2 :"))
    o = input("Enter operator( +, - , * , / ):")

    print(a, o, b, " = ", calculate(a, b, o))


def calculate(a, b, o):
    match o:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b
        case _:
            return a + b


if __name__ == "__main__":
    __main__()
