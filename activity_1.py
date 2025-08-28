# Superhero Class Example with Inheritance and Polymorphism

class Superhero:
    """Base class for all superheroes"""
    
    def __init__(self, name, power, suit_color):
        self.name = name
        self.power = power
        self.__suit_color = suit_color  # Private attribute (encapsulation)
        self.health = 100  # Default health

    def attack(self):
        print(f"{self.name} attacks using {self.power}!")

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"❌ {self.name} has been defeated!")
        else:
            print(f"💥 {self.name} took {damage} damage. Health left: {self.health}")

    def get_suit_color(self):
        """Getter method to access private data"""
        return self.__suit_color

    def set_suit_color(self, color):
        """Setter method to update private data"""
        self.__suit_color = color
        print(f"{self.name}'s suit color changed to {color}.")

    def intro(self):
        """Polymorphic method — will be overridden"""
        print(f"I am {self.name}, a hero ready to fight!")


# Child Class 1: IronMan
class IronMan(Superhero):
    def __init__(self, name, suit_model):
        super().__init__(name, "Repulsor Beams & Genius Intellect", "Red and Gold")
        self.suit_model = suit_model

    def intro(self):
        print(f"🤖 I am {self.name}! I am the genius behind the {self.suit_model} suit.")

    def fly(self):
        print(f"🚀 {self.name} is flying using jet propulsion!")


# Child Class 2: BlackWidow
class BlackWidow(Superhero):
    def __init__(self, name, weapon):
        super().__init__(name, "Martial Arts & Espionage", "Black")
        self.weapon = weapon

    def intro(self):
        print(f"🖤 I am {self.name}, highly trained spy and master of {self.weapon}.")

    def spy_mode(self):
        print(f"👀 {self.name} is gathering intel in stealth mode.")


# 🧪 Demo: Create Objects and Test
if __name__ == "__main__":
    # Create superhero objects
    tony = IronMan("Iron Man", "Mark 85")
    natasha = BlackWidow("Black Widow", "Widow's Bite")

    print("🌟 SUPERHERO BATTLE SIMULATION 🌟\n")

    # Polymorphism: Same method, different behavior
    for hero in [tony, natasha]:
        hero.intro()          # Calls overridden intro()
        hero.attack()
        hero.take_damage(30)
        print("-" * 40)

    # Encapsulation: Access private data safely
    print(f"{tony.name}'s suit color: {tony.get_suit_color()}")
    tony.set_suit_color("Neon Blue")

    # Unique methods
    tony.fly()
    natasha.spy_mode()

    print("\n🎉 Mission Complete!")