class Publisher:
    def __init__(self, name, location, founded_year):
        self.name = name
        self.location = location
        self.foundes_year = founded_year

class Magazine(Publisher):
    def __init__(self, name, location, founded_year, issue_number=None):
        super().__init__(name, location, founded_year)
        self.issue_number = issue_number

    def publish(self):
        if self.issue_number != None:
            print(f"Publishing the magazine '{self.name}'.")
        else:
            print(f"Cannot publish the magazine '{self.name}' without an issue number")

    def display_magazine_info(self):
        pub_status = 'Published' if self.issue_number else "Not Published"
        print(f"Name: {self.name}\nLocation: {self.location}\nFounded Year: {self.foundes_year}\nIssue Number: {self.issue_number}\nPublish Status: {pub_status}")

mag1 = Magazine('Rising Sun', 'Kampala', 2013, 2323)
mag2 = Magazine('The Moon Sets', 'Wakiso', 2020)

mag1.publish()
mag2.publish()

print("-"*60)
mag1.display_magazine_info()
print("-"*60)
mag2.display_magazine_info()