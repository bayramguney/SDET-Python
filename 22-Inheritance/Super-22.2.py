# invoke from parent class variables
a,b = 55,66
class A:
    a,b = 10,20

class B(A):
    a,b = 5, 8
    def m1(self,a,b):
        print("This is a method from B",a+b)   # local
        print("This is a method from B", self.a + self.b)  # child class variable
        print("This is a method from B", super().a + super().b)  # parent class variable
        print("This is a method from B", globals()['a']+globals()['b'])  # global variable

bobj = B()
bobj.m1(6,6)   # This is a method from B 12   This is a method from B 13     This is a method from B 30    This is a method from B 121