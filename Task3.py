def __main__():
    a = int(input("Enter a number(1-3): ")) - 1
    b = int(input("Enter a number(1-3): ")) - 1

    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    print(matrix[a][b])


if __name__ == "__main__":
    __main__()
