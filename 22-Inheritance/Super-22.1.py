# invoke from parent class methods
class A:
    def m1(self):
        print("This is a method from A")

class B(A):
    def m2(self):
        print("This is a method from B")
        super().m1()
b = B()
b.m2()   # This is a method from B   This is a method from A