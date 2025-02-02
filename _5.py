class Animal:
    def __init__(self, species, name, habitat):
        self.species = species
        self.name = name
        self.habitat = habitat

class Mammal(Animal):
    def __init__(self, species, name, habitat, fur_color, fed=True):
        super().__init__(species, name, habitat)
        self.fur_color = fur_color
        self.fed = fed

    def feed(self):
        if self.fed:
            self.fed = False
            print(f"The animal '{self.name}' is being fed.")
        else:
            print(f"The animal '{self.name}' has already beed fed")

    def display_animal_info(self):
        status = 'Fed' if self.fed else "Not Fed"
        print(f"Species: {self.species}\nName: {self.name}\nCurrent State: {status}")

mammal1 = Mammal('African Elephant', 'Dumbo', 'Savanna', 'Grey')
mammal2 = Mammal('Polar Bear', 'Snowball', 'Arctic', 'White')

mammal2.feed()
mammal2.feed()


print('-'*60)
mammal1.display_animal_info()
print('-'*60)
mammal2.display_animal_info() 