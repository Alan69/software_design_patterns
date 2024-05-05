from abc import ABC, abstractmethod

# Product interface
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Concrete products
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Bird(Animal):
    def speak(self):
        return "Chirp!"

# Creator interface
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass

# Concrete creators
class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()

class BirdFactory(AnimalFactory):
    def create_animal(self):
        return Bird()

# Client code
def get_animal_sound(factory):
    animal = factory.create_animal()
    return animal.speak()

# Example usage
dog_factory = DogFactory()
cat_factory = CatFactory()
bird_factory = BirdFactory()

print(get_animal_sound(dog_factory))  # Output: Woof!
print(get_animal_sound(cat_factory))  # Output: Meow!
print(get_animal_sound(bird_factory)) # Output: Chirp!
