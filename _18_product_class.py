class Product:
    def __init__(self, product_name, product_code, price):
        self.product_name = product_name
        self.product_code = product_code
        self.price = price

class Inventory:
    def __init__(self, inventory_id):
        self.inventory_id = inventory_id
        self.product_list = {}

    def add_product(self, product_name, quantity):
        if product_name not in self.product_list:
            self.product_list[product_name] = quantity
            print(f"The product '{product_name}' has been added to the product list. ")

        else:
            self.product_list[product_name] += quantity
            print(f"The product '{product_name}' has increased by a quantity of '{quantity}'. {self.product_list[product_name]} '{product_name}' are left.")

    def remove_product(self, product_name, quantity):
        if product_name in self.product_list:
            self.product_list[product_name] -= quantity
            print(f"The product '{product_name}' has decreased by a quantity of '{quantity}'. {self.product_list[product_name]} '{product_name}' are left.")

        else:
            print(f"The product '{product_name}' you are trying to remove does not exist in the product list.")




product = Product('Shoes', 'S23', 500)
inv = Inventory('I32')

inv.add_product('t-shirts', 45)
inv.add_product('pants', 60)
inv.add_product('jerseys', 300)

inv.remove_product('t-shirts', 20)

inv.remove_product('pens', 20)

