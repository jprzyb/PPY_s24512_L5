class Products:
    def __init__(self):
        self.products = []

    def add(self, name, count, price):
        self.products.append({'Name': name, 'Count': count, 'Price': price})

    def delete(self, index):
        if 0 <= index < len(self.products):
            del self.products[index]
        else:
            print("Incorrect index")

    def show(self):
        print("{:<5} {:<20} {:<10} {:<10}".format('Nr', 'Name', 'Count', 'Price'))
        for i, product in enumerate(self.products):
            print("{:<5} {:<20} {:<10} {:<10}".format(i + 1, product['Name'], product['Count'], product['Price']))

    def modify(self, index, name, count, price):
        if 0 <= index < len(self.products):
            self.products[index] = {'Name': name, 'Count': count, 'Price': price}
        else:
            print("Incorrect index")


def __main__():
    products = Products()

    products.add('Chleb', 2, 2.5)
    products.add('Mleko', 1, 3)
    products.add('Jajka', 12, 4)
    print("Original:")
    products.show()

    products.delete(1)
    print("Deleted pos at index 1:")
    products.show()

    products.modify(0, "kapcie", 999, 10.99)
    print("Modified pos at index 0:")
    products.show()


if __name__ == "__main__":
    __main__()
