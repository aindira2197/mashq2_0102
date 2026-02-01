class Fruit:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def total_price(self):
        return self.price * self.weight


apple = Fruit("Olma", 5000, 2)
print("Umumiy narx:", apple.total_price())
