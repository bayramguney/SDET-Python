# python is not required to implement abstract methods of the parent but without implementing
# we can not create object of subclass
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def fly(self):
        pass

class Tiger(Animal):
    def eat(self):
        print("eat non-veg")
    def fly(self):
        print("can not fly")

class Cow(Animal):
    def eat(self):
        print("eat veg")

t = Tiger()
t.eat()
t.fly()

c = Cow()      # we can not create the object
c.eat()

class Goat(Cow):
    def fly(self):
        print("can not fly")

g = Goat()     # we can create object from Goat implementing the method Cow not implemented
g.eat()
g.fly()

