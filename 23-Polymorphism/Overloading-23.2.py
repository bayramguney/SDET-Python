class Human:
    def sayHello(self,name=None):
        if name is not None:
            print("Hello"+" " +name)
        else:
            print("Hello")

obj = Human()
obj.sayHello()    # Hello
obj.sayHello("Robert")   # Hello Robert

class Bird:
    def fly(self,name=None):
        if name == "Parrot":
            print("Can fly")
        if name == "Penguin":
                print("Can not fly")
        if name is None:
                print("no input")

b = Bird()
b.fly()     # no input
b.fly("Parrot")    # Can fly
b.fly("Penguin")   # Can not fly
