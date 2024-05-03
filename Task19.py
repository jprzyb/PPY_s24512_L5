def __main__():
    data_list = []
    while data_list.__len__() < 20:
        text = str(len(data_list) + 1) + ". Enter a number between -20 and 20: "
        a = int(input(text))
        if -20 <= a <= 20:
            data_list.append(a)
        else:
            print("Wrong value!")

    copy_list = data_list.copy()
    print(f"The copy of list is: {copy_list}")

    primary_numbers = find_primary_numbers(data_list)
    print(f"The primary numbers are: {primary_numbers}")

    evenPowers = power_even_numbers(data_list)
    print(f"The even powers are: {evenPowers}")

    for i in range(0, len(data_list)):
        if data_list[i] % 2 == 0:
            data_list[i] = "A"
    print(f"data_list with A's: {data_list}")


def power_even_numbers(xlist):
    xtuple = ()

    for val in xlist:
        if val % 2 == 0:
            xtuple = xtuple + (val * val,)
    return xtuple


def is_primary(val):
    if val < 2:
        return False
    for i in range(2, int(val ** 0.5) + 1):
        if val % i == 0:
            return False
    return True


def find_primary_numbers(xlist):
    firsts = [val for val in xlist if is_primary(val)]
    return tuple(firsts)


if __name__ == "__main__":
    __main__()
