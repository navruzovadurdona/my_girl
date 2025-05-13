class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
class Bird(Animal):
    def speak(self):
        return f"{self.name} says Tweet!"
class Fish(Animal):
    def speak(self):
        return f"{self.name} says Blub!"
class Horse(Animal):
    def speak(self):
        return f"{self.name} says Neigh!"
class Cow(Animal):
    def speak(self):
        return f"{self.name} says Moo!"
class Sheep(Animal):
    def speak(self):
        return f"{self.name} says Baa!"
class Pig(Animal):
    def speak(self):
        return f"{self.name} says Oink!"
class Lion(Animal):
    def speak(self):
        return f"{self.name} says Roar!"
class Elephant(Animal):
    def speak(self):
        return f"{self.name} says Trumpet!"
class Giraffe(Animal):
    def speak(self):
        return f"{self.name} says Bleat!"
class Monkey(Animal):   
    def speak(self):
        return f"{self.name} says Ooh Ooh Aah Aah!"
class Tiger(Animal):
    def speak(self):
        return f"{self.name} says Growl!"
class Bear(Animal):
    def speak(self):
        return f"{self.name} says Roar!"
class Wolf(Animal):
    def speak(self):
        return f"{self.name} says Howl!"
class Kangaroo(Animal):
    def speak(self):
        return f"{self.name} says Boing!"
class Zebra(Animal):
    def speak(self):
        return f"{self.name} says Neigh!"
class Rhino(Animal):
    def speak(self):
        return f"{self.name} says Grunt!"
