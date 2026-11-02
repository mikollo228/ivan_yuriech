class ShoppingCart:
    def __init__(self):
       self.items = []

    def add_item(self,name: str, price: float, qty: int):
        item = {"name": name, "price":price, "qty":qty}
        self.items.append(item)

item1 = ShoppingCart()
item1.add_item("lamoda",12000,1)


print(item1.items)