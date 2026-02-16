from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Dog barks: Woof Woof")
class Cat(Animal):
    def sound(self):
        print("Cat meows: Meow Meow")
dog1 = Dog()
cat1 = Cat()

dog1.sound()
cat1.sound()
