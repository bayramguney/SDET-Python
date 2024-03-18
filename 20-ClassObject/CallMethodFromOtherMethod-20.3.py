class MyClass:

    def m1(self):
        print("this is m1 method")
        self.m2(100)

    def m2(self, a):
        print("this is m2 method", a)

mc = MyClass()
mc.m1()
