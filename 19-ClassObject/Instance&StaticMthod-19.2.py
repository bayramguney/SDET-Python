class MyClass:
    def m1(self):    # instance
        print("instance method")
    @staticmethod
    def m2():  # static     self is treated as parameter. not like self belong to class
        print("static method")

mc = MyClass()
mc.m1()

MyClass.m2()   # no need create object