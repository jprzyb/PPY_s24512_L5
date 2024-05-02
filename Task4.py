def __main__():
    p = True
    q = True
    s = True
    law_of_distributive_conjunctions(p, q, s)

    p = True
    q = True
    s = False
    law_of_distributive_conjunctions(p, q, s)

    p = True
    q = False
    s = True
    law_of_distributive_conjunctions(p, q, s)

    p = True
    q = False
    s = False
    law_of_distributive_conjunctions(p, q, s)

    p = False
    q = True
    s = True
    law_of_distributive_conjunctions(p, q, s)

    p = False
    q = True
    s = False
    law_of_distributive_conjunctions(p, q, s)

    p = False
    q = False
    s = True
    law_of_distributive_conjunctions(p, q, s)

    p = False
    q = False
    s = False
    law_of_distributive_conjunctions(p, q, s)


def left_side(a, b, c):
    return a and (b or c)


def right_side(a, b, c):
    return (a and b) or (a and c)


def implication(left, right):
    if left and not right:
        return False
    return True


def law_of_distributive_conjunctions(a, b, c):
    l = left_side(a, b, c)
    r = right_side(a, b, c)
    print(f"for p={a},q={b}, s={c} :=\t", implication(l, r))


if __name__ == "__main__":
    __main__()
