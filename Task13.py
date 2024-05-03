def __main__():
    fibonacci(30)


def fibonacci(length):
    a, b = 0, 1
    for _ in range(length):
        print(a, end=" ")
        a, b = b, a + b


if __name__ == "__main__":
    __main__()
