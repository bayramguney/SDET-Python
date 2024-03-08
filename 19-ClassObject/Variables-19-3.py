class MyClass:
    a, b = 10, 200  # class variables

    def add(self):
        print(self.a+self.b)

    def mul(self):
        print(self.a*self.b)

mc = MyClass()
mc.add()    # 210
mc.mul()    # 2000
