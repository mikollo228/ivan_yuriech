class ShoppingCart:
    def __init__(self):
       self.items = []

    def add_item(self,name: str, price: float, qty: int = 1):
        if price <= 0 or qty <= 0:
            raise ValueError("Цена и количество должны быть > 0")
        for i in self.items:
            if i["name"] == name:
                i["qty"] += qty
                return

        item = {"name": name, "price":price, "qty":qty}
        self.items.append(item)

    def remove_item(self,name, qty: int = 1):
        for i in self.items:
            self.items.remove(i)

    def total_price(self):
        a = ["price"]
        b = ["qty"]
        return a * b

    def __str__(self):
        return f'название-{["name"]} цена-{["price"]} количество{["qty"]}'




item1 = ShoppingCart()
item2 = ShoppingCart()
item1.add_item("lamoda",12000,1)
item2.add_item("lamoda",12000,2)

print(item1.items)