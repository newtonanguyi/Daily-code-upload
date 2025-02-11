# i. Customer class
class Customer:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number

# ii. Order class
class Order:
    def __init__(self, order_number, order_date, status="Pending"):
        self.order_number = order_number
        self.order_date = order_date
        self.status = status
        self.is_placed = False  # To track if an order is placed

    # b) Methods to place and cancel an order
    def place_order(self):
        if not self.is_placed:
            self.status = "Placed"
            self.is_placed = True
            print(f"Order {self.order_number} has been placed.")
        else:
            print(f"Order {self.order_number} is already placed.")

    def cancel_order(self):
        if self.is_placed:
            self.status = "Cancelled"
            print(f"Order {self.order_number} has been cancelled.")
        else:
            print(f"Order {self.order_number} cannot be cancelled because it hasn’t been placed yet.")

    # d) Method to display order details
    def display_order_details(self):
        print(f"Order Number: {self.order_number}")
        print(f"Order Date: {self.order_date}")
        print(f"Order Status: {self.status}")

# Create two customers
customer1 = Customer("Alice", "alice@example.com", "123-456-7890")
customer2 = Customer("Bob", "bob@example.com", "987-654-3210")

# Create orders for each customer
order1 = Order(101, "2024-12-16")
order2 = Order(102, "2024-12-16")

# Customer 1 places and cancels an order
order1.place_order()
order1.cancel_order()

# Customer 2 tries to cancel an order before placing it
order2.cancel_order()

# Customer 2 places the order
order2.place_order()
