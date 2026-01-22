class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def info(self):
        print(f"{self.name} — narxi: {self.price}")

p1 = Product("Smartphone", 1200, "electronics")
p2 = Product("Laptop", 2500, "electronics")
p3 = Product("Headphones", 150, "electronics")
p4 = Product("Watch", 500, "accessories")
p5 = Product("Camera", 1800, "electronics")
p6 = Product("Backpack", 100, "accessories")

products = [p1, p2, p3, p4, p5, p6]

most_expensive = max(products, key=lambda p: p.price)
most_expensive.info()
