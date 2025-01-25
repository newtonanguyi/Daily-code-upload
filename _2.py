class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type, tank_capacity):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type
        self.tank_capacity = tank_capacity
        self.fuel_level = 0

    def refuel(self, amount):
        if amount + self.fuel_level > self.tank_capacity:
            print(f"{amount} litres exceeds fuel capacity. Refilling till {self.tank_capacity} litres.")
            self.fuel_level = self.tank_capacity

        else:
            self.fuel_level += amount
            print(f"Refuelled {amount} litres. Total fuel level is {self.fuel_level}")

    def display_car_info(self):
        print(f"Make: {self.make}\nMode: {self.model}\nYear: {self.year}\nFuel Type: {self.fuel_type}\nTank Capacity: {self.tank_capacity}\nFuel Level: {self.fuel_level}")


car1 = Car('Toyota', 'Hilux', 2020, 'Petrol', 50)
car1.refuel(60)

car2 = Car('Mercedese', 'G-Wagon', 2024, 'Diesel', 70)
car2.refuel(30)
car2.refuel(20)

print("-"*60)
car1.display_car_info()
print("-"*60)
car2.display_car_info()