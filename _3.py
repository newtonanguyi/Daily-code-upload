class ShopItem:
    def __init__(self, name, price, stock_quantity):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

class Eletronics(ShopItem):
    def __init__(self, name, price, stock_quantity, warranty_period):
        super().__init__(name, price, stock_quantity)
        self.warranty_period = warranty_period

    def sell_item(self, quantity):
        if quantity <= self.stock_quantity:
            self.stock_quantity -= quantity
            print(f"{quantity} units of {self.name} have been sold. {self.stock_quantity} units are left.")
        else:
            print(f"Can't sell {quantity} units of {self.name} because it exceeds stock quantity!")

    def display_item_info(self):
        stock_qty = self.stock_quantity if self.stock_quantity > 0 else f"The item {self.name} is out of stock!"
        print(f"Name: {self.name}\nPrice: {self.price}\nStock Quantity: {stock_qty}\nWarrranty Period: {self.warranty_period}")

el1 = Eletronics("Television", 750000, 500, 2)
el2 = Eletronics("Fridge", 400000, 200, 1)

el1.sell_item(300)
el1.sell_item(200)
el2.sell_item(120)

print("-"*60)
el1.display_item_info()
print("-"*60)
el2.display_item_info()