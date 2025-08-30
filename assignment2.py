# Base class
class Mover:
    def move(self):
        raise NotImplementedError("Subclass must implement this method")


# Vehicle classes
class Car(Mover):
    def move(self):
        return "🚗 Driving on the road"


class Plane(Mover):
    def move(self):
        return "✈️ Flying in the sky"


class Boat(Mover):
    def move(self):
        return "⛵ Sailing on water"


# Animal classes
class Dog(Mover):
    def move(self):
        return "🐕 Running on land"


class Bird(Mover):
    def move(self):
        return "🐦 Flying in the air"


class Fish(Mover):
    def move(self):
        return "🐟 Swimming in the water"


# Demonstration of polymorphism
if __name__ == "__main__":
    movers = [Car(), Plane(), Boat(), Dog(), Bird(), Fish()]
    
    for mover in movers:
        print(mover.move())
