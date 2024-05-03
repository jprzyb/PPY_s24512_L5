def __main__():
    input_val = int(input("Enter a number: "))

    result = catalan_numbers(input_val)

    print(f"Catalans numbers (<{input_val}):")
    for catalan in result:
        print(catalan, end=" ")


def catalan_numbers(x):
    catalan = []
    c = 1
    while True:
        if c > x:
            break
        catalan.append(c)
        c = c * 2 * (2 * len(catalan) + 1) // (len(catalan) + 2)
    return catalan


if __name__ == "__main__":
    __main__()
