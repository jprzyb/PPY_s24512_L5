def __main__():
    name = input("Enter your name: ")
    surename = input("Enter your surename: ")

    say_hello(name, surename)


def say_hello(name, surename):
    print(f"Hello {name} {surename}!")


if __name__ == "__main__":
    __main__()
