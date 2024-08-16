#Polymorphism allows objects of different classes to be treated as objects of a common super class

#Concept of Overriding


class Animal:
    def speak(self):
        raise NotImplementedError("Subclasses should implement this!")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())  # Output: Woof! Meow!
