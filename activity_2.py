# Activity 2: Polymorphism Challenge! 🎭

class Animal:
    def move(self):
        pass  # Abstract method to be overridden

class Dog(Animal):
    def move(self):
        return "Running 🐕"  # Dogs run

class Bird(Animal):
    def move(self):
        return "Flying 🐦"  # Birds fly

class Fish(Animal):
    def move(self):
        return "Swimming 🐟"  # Fish swim

class Snake(Animal):
    def move(self):
        return "Slithering 🐍"  # Snakes slither

class Kangaroo(Animal):
    def move(self):
        return "Hopping 🦘"  # Kangaroos hop

# Create instances of different animals
animals = [
    Dog(),
    Bird(),
    Fish(),
    Snake(),
    Kangaroo()
]

# Demonstrate polymorphism - same method, different behaviors
print("🐾 Animal Movement Demonstration 🐾")
print("=" * 40)

for animal in animals:
    print(f"{animal.__class__.__name__}: {animal.move()}")

print("=" * 40)

# Alternative: Vehicle example
print("\n🚗 Vehicle Movement Demonstration 🚗")
print("=" * 40)

class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"

class Bicycle(Vehicle):
    def move(self):
        return "Pedaling 🚴"

class Train(Vehicle):
    def move(self):
        return "Chugging along 🚂"

# Create instances of different vehicles
vehicles = [
    Car(),
    Plane(),
    Boat(),
    Bicycle(),
    Train()
]

for vehicle in vehicles:
    print(f"{vehicle.__class__.__name__}: {vehicle.move()}")

print("=" * 40)

# Bonus: Function that accepts any object with move() method
def demonstrate_movement(obj):
    """Polymorphic function that works with any object that has a move() method"""
    print(f"The {obj.__class__.__name__.lower()} is {obj.move().lower()}")

print("\n🎯 Polymorphic Function Demonstration:")
demonstrate_movement(Dog())
demonstrate_movement(Plane())
demonstrate_movement(Fish())