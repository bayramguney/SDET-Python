# ABC is pre defined abstract class
from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def display(self):
        None

class B(A):
    def display(self):
        print("This is a display method")

obj = B()
obj.display()    # This is a display method
