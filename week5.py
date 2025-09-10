# Week 5 Assignment
# Assignment 1: Design Your Own Class (Smartphone Example)

class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"Device: {self.brand} {self.model}"


class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)
        self.storage = storage
        self.battery = battery

    def make_call(self, number):
        return f"Calling {number} from {self.brand} {self.model}..."

    def charge(self):
        return f"{self.brand} {self.model} is charging..."


# Create objects
phone1 = Smartphone("Apple", "iPhone 14", "256GB", "85%")
phone2 = Smartphone("Samsung", "Galaxy S23", "512GB", "70%")

print(phone1.device_info())
print(phone1.make_call("0640994360"))
print(phone2.charge())


# Assignment 2: Polymorphism Challenge (Animals Example)

class Animal:
    def move(self):
        pass


class Dog(Animal):
    def move(self):
        return "The dog is running 🐕"


class Bird(Animal):
    def move(self):
        return "The bird is flying 🐦"


class Fish(Animal):
    def move(self):
        return "The fish is swimming 🐟"


# Create objects
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    print(animal.move())