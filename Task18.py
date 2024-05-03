def __main__():
    name = input("Enter your name: ")
    birth_date = input("Enter your birth date: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")

    xlist = [name, birth_date, email, phone]
    xtuple = (name, birth_date, email, phone)
    xdictionary = {"name": name, "birth_date": birth_date, "email": email, 'phone number': phone}
    print(f"list = {xlist}")
    print(f"tuple = {xtuple}")
    print(f"dictionary = {xdictionary}")


if __name__ == "__main__":
    __main__()
