class Product:

    def __init__(self, name, price, in_stock):
        self.name = name
        self.price = price
        self.in_stock = in_stock

p1 = Product("Olma", 2.5, True)
p2 = Product("Banan", 3.0, False)
p3 = Product("Shaftoli", 4.0, True)
p4 = Product("Anor", 5.5, True)
p5 = Product("Gilos", 6.0, False)

products = [p1, p2, p3, p4, p5]

total_price = sum(
    map(
        lambda product: product.price,
        filter(
            lambda product: product.in_stock,
            products
        )
    )
)

print(total_price)