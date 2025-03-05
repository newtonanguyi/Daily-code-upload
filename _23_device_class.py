class Device:
    def __init__(self, device_name, model, status):
        self.device_name = device_name
        self.model = model
        self.status = status


class Smartphone(Device):
    def __init__(self, device_name, model, battery_level, storage_capacity, status='off'):
        super().__init__(device_name, model, status)
        self.battery_level = battery_level
        self.storage_capacity = storage_capacity

    def turn_on(self):
        if self.status == 'on':
            print(f"{self.device_name} {self.model} is already on.")
        else:
            self.status = 'on'
            print(f"{self.device_name} {self.model} has now been turned on")


smartphone = Smartphone('Samsung Galaxy', 'A73', '', 98, '128Gb')
smartphone.turn_on()
# smartphone.turn_on()

smartphone.status = 'off'
print(f"{smartphone.device_name} {smartphone.model} is now turned off.")