class Product:
    def __init__(self,product_name, price, stock):
        self.product_name = product_name
        self.price = price
        self.stock = stock

class Order:
    def  __init__(self, order_name):
        self.order_name = order_name
        self.ordered_products = []

    def add_product(self, product):
        if product in self.ordered_products:
            print(f"Product '{product}' has already been added")

        else:
            self.ordered_products.append(product)
            print(f"Product '{product}' has been added")

    def remove_product(self, product):
        pass


product = Product('soap', 23, 500)
order = Order('OD1')

order.add_product('Washing Powder')


