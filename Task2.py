def __main__():
    a = 5
    b = "xyz"

    print("Przed:")
    print(f"a={a}")
    print(f"b={b}")

    a, b = b, a

    print("Po:")
    print(f"a={a}")
    print(f"b={b}")


if __name__ == "__main__":
    __main__()
