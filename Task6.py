def __main__():
    sample_tuple = ("Yellow", "Orange", "Black")
    sample_list = ["Blue", "Green", "Red"]
    print(f"Sample tuple: {sample_tuple}")
    print(f"Sample list: {sample_list}")
    for _ in sample_list:
        sample_tuple = sample_tuple + (_,)
    print(f"New sample tuple: {sample_tuple}")

    new_tuple = ()

    for _ in sample_tuple:
        if _ == "Orange":
            new_tuple = new_tuple + ("Violete",)
        else:
            new_tuple = new_tuple + (_,)
    print(f"New tuple: {new_tuple}")


if __name__ == "__main__":
    __main__()
