def __main__():
    x = int(input("Enter lower bound: "))
    y = int(input("Enter upper bound: "))
    sum = 0

    for i in range(x, y+1, 1):
        if i % 2 == 1:
            sum += i
    print(f"Sum of odd numbers between {x} and {y} is {sum}")


if __name__ == "__main__":
    __main__()