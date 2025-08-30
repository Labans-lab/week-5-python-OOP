# Base class: Device
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"


# Derived class: Smartphone
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        # Call parent constructor using super()
        super().__init__(brand, model)
        self.__os = os          # private attribute (encapsulation)
        self.storage = storage  # public attribute
    
    # Getter for OS (encapsulation)
    def get_os(self):
        return self.__os
    
    # Setter for OS (encapsulation)
    def set_os(self, new_os):
        self.__os = new_os
    
    # Method to simulate making a call
    def make_call(self, number):
        return f" Calling {number} from {self.device_info()}"
    
    # Method to check storage
    def check_storage(self):
        return f"{self.device_info()} has {self.storage}GB storage left."
    
    # Polymorphism: overriding parent method
    def device_info(self):
        return f"Smartphone: {self.brand} {self.model} running {self.__os}"


# Another derived class: Tablet
class Tablet(Device):
    def __init__(self, brand, model, screen_size):
        super().__init__(brand, model)
        self.screen_size = screen_size
    
    def device_info(self):
        return f"Tablet: {self.brand} {self.model} with {self.screen_size}-inch screen"


# Example usage
if __name__ == "__main__":
    phone1 = Smartphone("Apple", "iPhone 14", "iOS", 128)
    phone2 = Smartphone("Samsung", "Galaxy S23", "Android", 256)
    tablet1 = Tablet("Lenovo", "Tab M10", 10.1)

    print(phone1.device_info())
    print(phone1.make_call("+123456789"))
    print(phone2.check_storage())
    print(tablet1.device_info())

    # Testing encapsulation (getter & setter)
    print("Old OS:", phone1.get_os())
    phone1.set_os("iOS 17")
    print("Updated OS:", phone1.get_os())
