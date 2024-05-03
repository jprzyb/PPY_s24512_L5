import random


def __main__():
    sample = []
    for i in range(100):
        sample.append(random.randint(1, 20))

    result = multiply_all(*sample)
    print(f"The result is: {result}")

    # result = multiply_all(2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29)
    # print(f"The result is: {result}")


def multiply_all(*args):
    res = 1
    for _ in args:
        res = res * _
    return res


if __name__ == "__main__":
    __main__()
