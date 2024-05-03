import random


def __main__():
    sample1 = set(random.sample(range(1001), 100))
    sample2 = set(random.sample(range(1001), 100))
    print(f'sample1: {sample1}')
    print(f'sample2: {sample2}')

    common = sample1.intersection(sample2)

    print(f"Common part: {common}")


if __name__ == "__main__":
    __main__()
