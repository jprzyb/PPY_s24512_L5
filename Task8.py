def __main__():
    moj_slownik = {"imie": "Jan", "nazwisko": "Kowalski", "wiek": "30", "hobby": "czytanie"}
    print(moj_slownik)

    for key, value in moj_slownik.items():
        if len(value) <= 5:
            print(key)


if __name__ == "__main__":
    __main__()
