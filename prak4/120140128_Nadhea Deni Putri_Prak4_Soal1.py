class Animal:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    
    def make_sound(self):
        pass
    
    def eat(self):
        print(f"{self.name} is eating.")
    
    def drink(self):
        print(f"{self.name} is drinking.")

class Cat(Animal):
    def make_sound(self):
        print(f"Cat {self.name} makes sound: Meow!")
    
    def eat(self):
        print(f"{self.name} is eating: fish")

class Dog(Animal):
    def make_sound(self):
        print(f"Dog {self.name} makes sound: Woof!")
    
    def eat(self):
        print(f"{self.name} is eating: bones")

# Contoh penggunaan
animal1 = Cat("Kiki", "Betina")
animal2 = Dog("Ichi", "Jantan")

animal1.make_sound()
animal1.eat()
animal1.drink()

print()

animal2.make_sound()
animal2.eat()
animal2.drink()
