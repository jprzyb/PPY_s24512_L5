def __main__():
    list = ["kot", "pies", "kon", "slon", "zyrafa"]

    print(first_element(list))
    print(penultimate(list))
    print(all_but_no_first_and_last(list))

    print("appending")
    list.append("surykatka")
    print(list)

    print("index 2 is jez")
    list.insert(2, "jez")
    print(list)

    list2 = ["krokodyl", "zolw"]
    print(f"list2 is {list2}")
    list.extend(list2)
    print(list)
    print(f"appended lists: {list}")

    print(f"sorted: {sorted(list)}")

    newList = [w.capitalize() for w in list]
    print(f"capitalized list={newList}")


def all_but_no_first_and_last(l):
    print("all_but_no_first_and_last")
    return l[1:-1]


def penultimate(l):
    print("penultimate")
    return l[::-1]


def first_element(l):
    print("first element")
    return l[0]


if __name__ == "__main__":
    __main__()