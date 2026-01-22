class Product:

    def __init__(self, name, price, category, is_stock = False):
        self.name = name
        self.price = price
        self.category = category
        self.is_stock = is_stock

product1 = Product("Smartphone", 12999.99, "electronics", True)
product2 = Product("Headphones", 499.99, "electronics")

print(product1.name, "-", product1.price)
print(product2.name, "-", product2.price)