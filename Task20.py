def __main__():
    size = int(input("Enter a size of multiplication table: "))
    multi_table(size)


def multi_table(size):
    for i in range(1, size + 1):
        # line = ""
        for j in range(1, size + 1):
            print("{:4}".format(i * j), end="")
            # line += "{:4}".format(i * j)
        print()
        # with open("multiplication.txt", "a") as file:
        #     file.write(line + "\n")


if __name__ == "__main__":
    __main__()
