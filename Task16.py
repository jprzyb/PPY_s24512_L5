import random


def __main__():
    sample = []
    for i in range(100):
        sample.append(random.randint(1, 20))

    result_m, result_d = multiply_all(*sample)
    print(f"The result of multiplication is: {result_m}")
    print(f"The result of division is: {result_d}")


def multiply_all(*args):
    res_m = args[0]
    res_d = args[0]
    for i in range(len(args)-1):
        res_m = res_m * args[i+1]
        res_d = res_d / args[i+1]
    return res_m, res_d


if __name__ == "__main__":
    __main__()
