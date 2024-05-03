def __main__():
    text = "Ciężka, ogromna i pot z niej spływa:\n"
    with open("test1.txt", "r") as file:
        lines = file.readlines()
        print(lines)
        lines.insert(2, text)
        print(lines)
    with open("test1.txt", "w") as file:
        file.writelines(lines)


if __name__ == "__main__":
    __main__()
