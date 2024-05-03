def __main__():
    count = 0

    while True:
        a = input("Enter st: ")
        if a == "red pill":
            break
        count += len(a)
    print(f"The total number of characters is: {count}")


if __name__ == "__main__":
    __main__()
