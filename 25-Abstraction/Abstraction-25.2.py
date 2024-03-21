from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

class Tiger(Animal):
    def eat(self):
        print("eat non-veg")

class Cow(Animal):
    def eat(self):
        print("eat veg")

t = Tiger()
t.eat()    # eat non-veg

c = Cow()
c.eat()    # eat veg
