class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        print(f" Instance created: {name,price,quantity}")
item1 = Item("Phone", 100, 5)

