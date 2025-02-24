class Hotel:
    def __init__(self, hotel_name, location, rooms_available):
        self.hotel_name = hotel_name
        self.location = location
        self.rooms_available = rooms_available

class Reservation:
    def __init__(self, guest_name, check_in_date, room_number):
        self.guest_name = guest_name
        self.check_in_date = check_in_date
        self.room_number = room_number
        self.rooms = []

    def book_room(self):
        if self.room_number not in self.rooms:
            self.rooms.append(self.room_number)
            print(f"Room {self.room_number} has been booked by {self.guest_name}.")

        else:
            print(f"Room {self.room_number} has already been booked by {self.guest_name}.")

    def cancel_reservation(self):
        if self.room_number in self.rooms:
            self.rooms.remove(self.room_number)
            print(f"{self.guest_name} cancelled their reservation for room {self.room_number}.")

        else:
            print(f"Cannot cancel reservation for {self.guest_name} since he/she did not book a room.")

    def display_reservation_details(self):
        print("-"*60)
        print(f"Guest Name: {self.guest_name}\nCheck In Date: {self.check_in_date}\nRoom Number: {self.room_number}")




hotel = Hotel('Sheraton', 'Kampala', 30)

res1 = Reservation('Flixton', '2024-09-23', 'R100')
res2 = Reservation('John', '2024-10-12', 'R105')
res3 = Reservation('Mark', '2024-08-22', 'R110')

res1.book_room()
res2.book_room()
res2.book_room()
res3.cancel_reservation()

res2.cancel_reservation()

res1.display_reservation_details()
res2.display_reservation_details()
res3.display_reservation_details()
