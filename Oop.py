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
            if i["name"] == name:
                self.items.remove(i)
            return



    def total_price(self):
        pris = 0
        for i in self.items:
            price = i["price"]
            qty = i["qty"]
            pris = pris + (price * qty)
        return pris


    def __str__(self):
        lines = [f'Название: {i["name"]} | Цена: {i["price"]} руб. | Количество: {i["qty"]}' for i in self.items]
        return "\n".join(lines)




#проверку нейронкой сделал.

raw_products = [
    {"name": "Молоко", "price": 89.90, "qty": 2},
    {"name": "Хлеб", "price": 45.00, "qty": 1},
    {"name": "Шоколад", "price": 120.00, "qty": 3},
    {"name": "Яблоки", "price": 150.00}, # количество сработает по умолчанию (=1)
]

# 2. Создаем один объект корзины
cart = ShoppingCart()

# 3. Автоматически загружаем все товары одной строчкой кода
for prod in raw_products:
    cart.add_item(**prod) # Оператор ** распаковывает ключи словаря в аргументы функции

# Проверяем работу
print("--- Содержимое корзины ---")
print(cart)

print("\n--- Общая стоимость ---")
print(f"{cart.total_price()} руб.")