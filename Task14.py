import math


def __main__():
    x = input("Enter integer: ")
    if x.isdigit():
        print(fact(int(x)))
    else:
        print("Invalid input.")


def fact(x):
    return math.factorial(x)


if __name__ == "__main__":
    __main__()
