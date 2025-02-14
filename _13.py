class Doctor:
    def __init__(self, name, specialization, years_of_experience):
        self.name = name
        self.specialization = specialization
        self.years_of_experience = years_of_experience
        self.appointments = []

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def display_appointments(self):
        print(f"Appointments for Dr. {self.name}:")
        for appointment in self.appointments:
            print(f"Patient: {appointment.patient_name}, Date: {appointment.date}, Status: {appointment.status}")

class Appointment:
    def __init__(self, patient_name, date, status="Scheduled"):
        self.patient_name = patient_name
        self.date = date
        self.status = status

    def schedule_appointment(self):
        self.status = "Scheduled"
        print(f"Appointment for {self.patient_name} on {self.date} has been scheduled.")
    
    def cancel_appointment(self):
        if self.status == "Scheduled":
            self.status = "Canceled"
            print(f"Appointment for {self.patient_name} on {self.date} has been canceled.")
        else:
            print(f"Appointment for {self.patient_name} on {self.date} was not scheduled or is already canceled.")

# Create a doctor
doctor = Doctor(name="Dr. John", specialization="Cardiologist", years_of_experience=10)

# Create two appointments
appointment1 = Appointment(patient_name="Alice", date="2024-12-20")
appointment2 = Appointment(patient_name="Bob", date="2024-12-21")

# Schedule both appointments
appointment1.schedule_appointment()
appointment2.schedule_appointment()

# Add appointments to doctor
doctor.add_appointment(appointment1)
doctor.add_appointment(appointment2)

# Cancel one appointment
appointment1.cancel_appointment()

# Display doctor's appointments
doctor.display_appointments()
