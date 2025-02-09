# Passenger class
class Passenger:
    def __init__(self, name, ticket_number, seat_number):
        self.name = name
        self.ticket_number = ticket_number
        self.seat_number = seat_number

# Flight class
class Flight:
    def __init__(self, flight_number, destination):
        self.flight_number = flight_number
        self.destination = destination
        self.passengers = {}  # Dictionary to store seat_number and passenger details

    def assign_seat(self, passenger):
        # Check if the seat is already taken
        if passenger.seat_number in self.passengers:
            print(f"Seat {passenger.seat_number} is already taken.")
        else:
            self.passengers[passenger.seat_number] = passenger
            print(f"Assigned seat {passenger.seat_number} to {passenger.name}.")

    def display_flight_info(self):
        print(f"Flight Number: {self.flight_number}, Destination: {self.destination}")
        print("Passenger List:")
        if self.passengers:
            for seat, passenger in self.passengers.items():
                print(f"Seat {seat}: {passenger.name} (Ticket: {passenger.ticket_number})")
        else:
            print("No passengers assigned yet.")

# Creating flight instance
flight1 = Flight("QF123", "New York")

# Creating passenger instances
passenger1 = Passenger("Alice", "TN001", 1)
passenger2 = Passenger("Bob", "TN002", 1)  # Same seat to demonstrate edge case

# Assign seats to passengers
flight1.assign_seat(passenger1)  # Should successfully assign
flight1.assign_seat(passenger2)  # Should show seat already taken message

# Display flight information
flight1.display_flight_info()
