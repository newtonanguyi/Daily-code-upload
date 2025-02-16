class Customer:
    def __init__(self, name, email, balance):
        self.name = name
        self.email = email
        self.balance = balance

class EcommerceSite:
    def __init__(self, site_name, available_items):
        self.site_name = site_name
        self.available_items = available_items

    def purchase_item(self, item, quantity):
        